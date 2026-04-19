## §4 — EL ORCHESTRATOR v4: ESPECIFICACIÓN TÉCNICA

### 4.0 Definiciones previas — tipos de datos

Antes de cualquier método, los tipos que usa todo el Orchestrator:

```python
from dataclasses import dataclass, asdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any
import json
import logging

from cgalpha_v3.lila.llm.proposer import TechnicalSpec
from cgalpha_v3.lila.codecraft_sage import CodeCraftSage, ExecutionResult
from cgalpha_v3.lila.llm.assistant import LLMAssistant
from cgalpha_v3.lila.llm.llm_switcher import LLMSwitcher
from cgalpha_v3.learning.memory_policy import MemoryPolicyEngine, MemoryLevel
from cgalpha_v3.domain.models.signal import Proposal
from cgalpha_v3.application.experiment_runner import ExperimentResult

logger = logging.getLogger("orchestrator_v4")

# --- C19: EvolutionResult definido explícitamente ---
@dataclass
class EvolutionResult:
    category: int                    # 1 | 2 | 3
    status: str                      # "COMMITTED" | "REJECTED_NO_COMMIT" |
                                     # "QUEUED_FOR_APPROVAL" | "REQUIRES_HUMAN_SESSION"
    commit_sha: str | None = None    # Solo si status == "COMMITTED"
    proposal_id: str | None = None   # Solo si status en {"QUEUED_*", "REQUIRES_*"}
    escalated_from: int | None = None # Categoría original antes de escalar
```

**Schema de objetos externos verificados (C29):**

```python
# TechnicalSpec (lila/llm/proposer.py línea 6):
#   change_type: str        # "parameter" | "feature" | "optimization"
#   target_file: str        # fichero único (singular)
#   target_attribute: str
#   old_value: float
#   new_value: float
#   reason: str
#   causal_score_est: float
#   confidence: float

# Proposal (domain/models/signal.py línea 105):
#   proposal_id: str
#   hypothesis: str
#   changes: list[dict[str, Any]]  # ← verificado línea 121
#   status: Literal["pending", "validated", "rejected"]
#   (+ risk_assessment, approach_types_targeted, etc.)

# ExperimentResult (application/experiment_runner.py línea 53):
#   experiment_id: str
#   proposal_id: str             # ← verificado línea 55
#   metrics: dict[str, float]    # keys: "sharpe_like", "net_return_pct",
#                                #        "max_drawdown_pct", "trades", etc.
#   (+ walk_forward_windows, friction, etc.)

# ExecutionResult (lila/codecraft_sage.py línea 21):
#   status: str
#   proposal_id: str
#   commit_sha: Optional[str]
#   test_report_path: Optional[str]
#   error_message: Optional[str]

# CodeCraftSage.execute_proposal():
#   Firma real: execute_proposal(self, spec: TechnicalSpec,
#               ghost_approved: bool, human_approved: bool)
#   ← VERIFICADO contra codecraft_sage.py línea 51
```

### 4.1 Rol del Orchestrator

El Orchestrator v4 es el componente central que no existía en v3. Su función es **recibir propuestas de cualquier origen, clasificarlas y enrutarlas al ejecutor correcto**. Es el puente que conecta las 4 islas.

```
                    ┌─────────────────────┐
                    │  ORÍGENES            │
                    │  ChangeProposer      │
                    │  AutoProposer        │
                    │  Reflexiones Lila    │
                    │  Humano (manual)     │
                    └────────┬────────────┘
                             │ TechnicalSpec | Proposal (adaptado)
                             ▼
                    ┌─────────────────────┐
                    │  PASO 0: LLMSwitcher│
                    │  select_for_task()  │
                    └────────┬────────────┘
                             │
                             ▼
                    ┌─────────────────────┐
                    │  PASO 1: classify() │
                    │  Determinista       │
                    │  primero → LLM      │
                    │  como fallback      │
                    └────────┬────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
         ┌─────────┐   ┌─────────┐   ┌─────────┐
         │  Cat.1  │   │  Cat.2  │   │  Cat.3  │
         │ Automát.│   │ Semi-   │   │ Superv. │
         │         │   │ automát.│   │         │
         └────┬────┘   └────┬────┘   └────┬────┘
              │              │              │
              ▼              ▼              ▼
         ┌─────────┐   ┌─────────┐   ┌─────────┐
         │CodeCraft│   │ GUI     │   │ Sesión  │
         │ directo │   │ aproba- │   │ humana  │
         │ + test  │   │ ción    │   │ completa│
         └────┬────┘   └────┬────┘   └────┬────┘
              │              │              │
              └──────────────┼──────────────┘
                             │
                             ▼
                    ┌─────────────────────┐
                    │  PERSISTENCIA       │
                    │  memoria + git +    │
                    │  evolution_log      │
                    └─────────────────────┘
```

**Constructor del Orchestrator (C17 corregido):**

```python
class EvolutionOrchestrator_v4:
    EVOLUTION_LOG_PATH = Path("aipha_memory/evolutionary/evolution_log.jsonl")

    def __init__(self, switcher: LLMSwitcher, sage: CodeCraftSage,
                 proposer: 'AutoProposer', memory: MemoryPolicyEngine,
                 assistant: LLMAssistant):    # ← C17: assistant explícito
        self.switcher = switcher
        self.sage = sage
        self.proposer = proposer
        self.memory = memory
        self.assistant = assistant            # ← el LLMAssistant que genera texto
```

### 4.2 Las 3 Categorías — definición con ejemplos concretos

#### Categoría 1: Automático

**Criterio determinista:** `spec.change_type == "parameter"` AND `spec.causal_score_est >= 0.75`

**Qué incluye:**
- Ajuste de `volume_threshold` de 1.2 → 1.3
- Cambio de `quality_threshold` de 0.45 → 0.50
- Modificación de `min_confidence` del Oracle de 0.68 → 0.72
- Cualquier cambio que toque un solo valor numérico en un solo fichero

**Qué NO incluye:**
- Cambios con `causal_score_est < 0.75` → pasan a Cat.2
- Cualquier cambio que toque una string, una lista, o una estructura → Cat.2 mínimo

**Flujo de ejecución:**
```python
def _execute_automatic(self, spec: TechnicalSpec) -> EvolutionResult:
    # 1. Log de inicio en memoria nivel 0a (RAW)
    self.memory.ingest_raw(
        content=f"Cat.1 iniciada: {spec.target_attribute} "
                f"{spec.old_value} → {spec.new_value}",
        field="codigo", tags=["evolution", "cat_1", "in_progress"]
    )

    # 2. CodeCraftSage aplica el patch (firma verificada: codecraft_sage.py l.51)
    result = self.sage.execute_proposal(
        spec, ghost_approved=True, human_approved=True
    )

    # 3. Evaluar resultado
    if result.status == "COMMITTED":
        # Promover registro a nivel 1 (FACTS) — TTL 30 días
        self.memory.ingest_raw(
            content=f"Auto-evolution completada: {spec.target_attribute} "
                    f"{spec.old_value} → {spec.new_value} | "
                    f"commit: {result.commit_sha}",
            field="codigo",
            tags=["evolution", "cat_1", "committed"]
        )
        self._append_evolution_log(spec, result)

    elif result.status == "REJECTED_NO_COMMIT":
        self.memory.ingest_raw(
            content=f"Cat.1 RECHAZADA por tests: {spec.target_attribute}. "
                    f"Error: {result.error_message}",
            field="codigo",
            tags=["evolution", "cat_1", "test_failure"]
        )

    return EvolutionResult(
        category=1, status=result.status,
        commit_sha=getattr(result, 'commit_sha', None)
    )
```

**Guardrails de Cat.1:**
- Si un parámetro ha sido modificado por Cat.1 más de 3 veces en 7 días → escalada automática a Cat.2 (el sistema está "cazando" un valor sin convergencia)
- Si el cambio propuesto mueve el parámetro más de 2× su valor actual → escalada a Cat.2
- Si el target_attribute aparece en `SAFETY_THRESHOLDS` de `_contradicts_identity()` → escalada a Cat.3

#### Categoría 2: Semi-automático

**Criterio determinista:** Todo lo que no es Cat.1 ni Cat.3. En la práctica: `spec.change_type == "optimization"` o parámetros con `causal_score_est < 0.75`.

**Qué incluye:**
- Propuestas del ChangeProposer (hipótesis de trading)
- Cambios de tipo "optimization" (ajustan lógica, no solo valores)
- Parámetros con causal score bajo (evidencia insuficiente para auto)
- Creación de artefactos (Parameter Landscape Map)
- Fixes de bugs Cat.2 (BUG-5, BUG-3, BUG-8)

**Flujo de ejecución:**
```python
def _queue_semi_automatic(self, spec: TechnicalSpec) -> EvolutionResult:
    # 1. El LLM genera análisis de impacto (C17: usa self.assistant)
    self.switcher.select_for_task("category_2")
    impact_analysis = self.assistant.generate(
        prompt=f"Analiza el impacto del cambio: {spec.target_attribute} "
               f"{spec.old_value} → {spec.new_value} en {spec.target_file}. "
               f"Razón propuesta: {spec.reason}. "
               f"Evalúa: riesgo, tests afectados, rollback.",
        temperature=0.2, max_tokens=800
    )

    # 2. Crear PendingProposal en memoria nivel 2 (RELATIONS, TTL 90d)
    #    C34: usar RELATIONS en lugar de FACTS para evitar expiración
    #    prematura antes de la escalada Cat.2→Cat.3 a los 14 días
    from uuid import uuid4
    proposal_id = str(uuid4())
    proposal_entry = self.memory.ingest_raw(
        content=json.dumps({
            "type": "pending_proposal",
            "proposal_id": proposal_id,    # C22: ID compartido con ExperimentRunner
            "category": 2,
            "spec": asdict(spec),
            "impact_analysis": impact_analysis,
            "status": "awaiting_approval",
            "created_at": datetime.now(timezone.utc).isoformat()
        }),
        field="architect",
        tags=["evolution", "cat_2", "pending"]
    )
    # Promover a RELATIONS (TTL 90d en lugar de FACTS 30d)
    self.memory.promote(
        entry_id=proposal_entry.entry_id,
        target_level=MemoryLevel.RELATIONS,
        approved_by="Lila"
    )

    # 3. Retornar — el operador aprobará vía GUI
    return EvolutionResult(
        category=2, status="QUEUED_FOR_APPROVAL",
        proposal_id=proposal_entry.entry_id
    )
```

**Después de aprobación humana vía GUI:**
```python
def approve_proposal(self, proposal_id: str) -> EvolutionResult:
    entry = self.memory._must_get(proposal_id)  # C18: definido en §5.6
    data = json.loads(entry.content)
    spec = TechnicalSpec(**data["spec"])

    # Ejecutar como Cat.1 (el humano ya aprobó)
    result = self._execute_automatic(spec)

    # C24: Actualizar el entry original Y persistir a disco
    entry.tags.append("approved")
    entry.tags.append(f"result:{result.status}")
    self.memory._persist_memory_entry(entry)
    return result
```

#### Categoría 3: Supervisado

**Criterio determinista:** `spec.change_type == "feature"` O `_contradicts_identity(spec) == True`

**Qué incluye:**
- Añadir/eliminar features del modelo del Oracle
- Cambios que tocan umbrales de seguridad cerca de límites
- Propuestas que contradicen principios invariantes del mantra
- Modificaciones al propio prompt IDENTITY (reflexiones críticas promovidas)
- Cambios arquitectónicos (crear nuevo componente, eliminar existente)

**Flujo de ejecución:**
```python
def _queue_supervised(self, spec: TechnicalSpec) -> EvolutionResult:
    # 1. El LLM genera documento técnico completo (C17: usa self.assistant)
    self.switcher.select_for_task("category_3")
    technical_doc = self.assistant.generate(
        prompt=f"Genera un documento técnico completo para revisión humana. "
               f"Cambio propuesto: {spec.target_attribute} en {spec.target_file}. "
               f"Tipo: {spec.change_type}. Razón: {spec.reason}. "
               f"Incluye: análisis de riesgo detallado, tests necesarios, "
               f"plan de rollback, impacto en otros componentes, "
               f"y justificación causal.",
        temperature=0.3, max_tokens=2000
    )

    # 2. Verificar si contradice IDENTITY
    contradicts = self._contradicts_identity(spec)

    # 3. Crear PendingProposal en memoria nivel 2 (RELATIONS) con flag especial
    from uuid import uuid4
    proposal_id = str(uuid4())
    proposal_entry = self.memory.ingest_raw(
        content=json.dumps({
            "type": "pending_proposal",
            "proposal_id": proposal_id,   # C22: ID compartido
            "category": 3,
            "spec": asdict(spec),
            "technical_document": technical_doc,
            "contradicts_identity": contradicts,
            "status": "requires_human_session",
            "created_at": datetime.now(timezone.utc).isoformat()
        }),
        field="architect",
        tags=["evolution", "cat_3", "supervised",
              *(["tension_con_identidad"] if contradicts else [])]
    )
    self.memory.promote(
        entry_id=proposal_entry.entry_id,
        target_level=MemoryLevel.RELATIONS,
        approved_by="Lila"
    )

    return EvolutionResult(
        category=3, status="REQUIRES_HUMAN_SESSION",
        proposal_id=proposal_entry.entry_id
    )
```

### 4.3 El mecanismo de escalada

Las categorías no son estáticas. Una propuesta puede escalar automáticamente:

```
Cat.1 → Cat.2: si el parámetro fue modificado >3 veces en 7 días
                O si el cambio >2× del valor actual
Cat.2 → Cat.3: si la propuesta permanece en cola >14 días sin aprobación
Cat.3 → BLOQUEADA: si _contradicts_identity() Y no hay evidencia OOS
                    de 3+ ciclos que soporte la propuesta
```

> ⚠️ **C27 corregido:** La escalada Cat.2→Cat.3 eliminó el trigger vago "si el LLM detecta impacto en >3 componentes" por no tener especificación implementable. Solo queda el trigger determinista de 14 días.

La escalada nunca baja. Una propuesta que llegó a Cat.3 no puede volver a Cat.2 aunque el operador quiera. La razón: si el sistema consideró que necesita supervisión completa, reducir el escrutinio es un antipatrón.

**Implementación del tracking de repetición (C23 — persiste en evolution_log):**

```python
def _count_recent_modifications(self, attribute: str, days: int = 7) -> int:
    """Lee evolution_log.jsonl y cuenta modificaciones Cat.1 en los últimos N días."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    count = 0
    if not self.EVOLUTION_LOG_PATH.exists():
        return 0
    with open(self.EVOLUTION_LOG_PATH, "r", encoding="utf-8") as f:
        for line in f:
            try:
                entry = json.loads(line)
                if (entry.get("category") == 1
                        and entry["spec"].get("target_attribute") == attribute
                        and datetime.fromisoformat(entry["ts"]) > cutoff):
                    count += 1
            except (json.JSONDecodeError, KeyError):
                continue
    return count

def _check_proposal_escalations(self) -> None:
    """Llamado al inicio de cada run_cycle(). Escala propuestas pendientes vencidas."""
    cutoff_14d = datetime.now(timezone.utc) - timedelta(days=14)
    for entry in self.memory.get_pending_proposals():
        data = json.loads(entry.content)
        if (data.get("category") == 2
                and datetime.fromisoformat(data["created_at"]) < cutoff_14d):
            data["category"] = 3
            data["status"] = "escalated_to_cat3"
            entry.content = json.dumps(data)
            entry.tags.append("escalated")
            self.memory._persist_memory_entry(entry)
```

### 4.4 Adaptador ChangeProposer → Orchestrator

El `ChangeProposer` genera `Proposal` (definido en `domain/models/signal.py` línea 105), no `TechnicalSpec`. El Orchestrator necesita un adaptador:

```python
def adapt_proposal_to_specs(proposal: Proposal) -> list[TechnicalSpec]:  # C28: plural
    """
    Convierte una Proposal de alto nivel (hipótesis de trading)
    en una lista de TechnicalSpec ejecutables por CodeCraftSage.

    La conversión no es trivial: una Proposal puede implicar
    múltiples cambios. En ese caso, se genera una TechnicalSpec
    por cambio, y todas comparten el mismo proposal_id.

    Campos de Proposal verificados (signal.py l.105-129):
      proposal_id: str, hypothesis: str,
      changes: list[dict[str, Any]]  # l.121 — cada dict tiene keys libres
    """
    specs = []
    for change in proposal.changes:
        specs.append(TechnicalSpec(
            change_type=change.get("type", "optimization"),
            target_file=change.get("file", ""),
            target_attribute=change.get("attribute", ""),
            old_value=change.get("old_value", 0.0),
            new_value=change.get("new_value", 0.0),
            reason=proposal.hypothesis,
            causal_score_est=0.5,  # Default conservador
            confidence=0.5
        ))
    return specs
```

### 4.5 Retroalimentación del ExperimentRunner

El `ExperimentRunner` (507 líneas) ejecuta experimentos con walk-forward y fricciones. Actualmente sus resultados no regresan al sistema. El Orchestrator los conecta:

```python
def process_experiment_results(self, result: ExperimentResult):
    """
    Recibe resultados del ExperimentRunner y decide acción.

    Campos de ExperimentResult verificados (experiment_runner.py l.53-63):
      experiment_id: str, proposal_id: str,
      metrics: dict[str, float]  # keys: "sharpe_like" (NO "sharpe_neto"),
                                  #   "net_return_pct", "max_drawdown_pct", etc.
    """
    # 1. Persistir resultados en memoria nivel 1
    self.memory.ingest_raw(
        content=f"Experiment {result.experiment_id}: "
                f"sharpe={result.metrics.get('sharpe_like', 0):.3f}, "
                f"max_dd={result.metrics.get('max_drawdown_pct', 0):.3f}%",
        field="trading",
        tags=["experiment", result.proposal_id]
    )

    # 2. C25 corregido: criterio de auto-aprobación reforzado
    sharpe_ok = result.metrics.get("sharpe_like", 0) >= 0.5
    net_positive = result.metrics.get("net_return_pct", 0) > 0
    if sharpe_ok and net_positive:
        pending = self._find_pending_for_proposal(result.proposal_id)
        # Solo auto-aprobar Cat.1 con causal_score_est >= 0.75
        if pending and pending["category"] == 1:
            spec_data = pending.get("spec", {})
            if spec_data.get("causal_score_est", 0) >= 0.75:
                self.approve_proposal(pending["entry_id"])

    # 3. Si el experimento rechaza, registrar y aprender
    else:
        self.memory.ingest_raw(
            content=f"Experiment FALLÓ: {result.experiment_id}. "
                    f"Hipótesis rechazada por OOS.",
            field="trading",
            tags=["experiment", "rejected", result.proposal_id]
        )

def _find_pending_for_proposal(self, proposal_id: str) -> dict | None:
    """C22: Busca propuesta pendiente por proposal_id."""
    for entry in self.memory.get_pending_proposals():
        data = json.loads(entry.content)
        if data.get("proposal_id") == proposal_id:
            return {"entry_id": entry.entry_id, **data}
    return None
```

### 4.6 evolution_log — formato de persistencia

Cada acción completada por el Orchestrator se registra en `evolution_log.jsonl`:

```json
{
  "ts": "2026-04-19T02:00:00+00:00",
  "category": 1,
  "spec": {
    "change_type": "parameter",
    "target_file": "pipeline.py",
    "target_attribute": "volume_threshold",
    "old_value": 1.2,
    "new_value": 1.3
  },
  "status": "COMMITTED",
  "commit_sha": "abc123f",
  "approved_by": "auto",
  "llm_used": "ollama:qwen2.5:1.5b",
  "escalated_from": null,
  "memory_entry_id": "uuid",
  "duration_ms": 4200
}
```

**C20: Implementación de `_append_evolution_log()`:**

```python
def _append_evolution_log(self, spec: TechnicalSpec, result,
                           approved_by: str = "auto") -> None:
    """Escribe una entrada al evolution_log.jsonl."""
    self.EVOLUTION_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "category": getattr(result, 'category', 1) if isinstance(result, EvolutionResult)
                    else 1,
        "spec": asdict(spec),
        "status": result.status,
        "commit_sha": getattr(result, 'commit_sha', None),
        "approved_by": approved_by,
        "llm_used": getattr(self.assistant.provider, 'name', 'unknown'),
        "escalated_from": getattr(result, 'escalated_from', None),
        "memory_entry_id": None,
        "duration_ms": None,
    }
    with open(self.EVOLUTION_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
```

**Diferencia con bridge.jsonl:** `bridge.jsonl` registra **trades** (señales de mercado + ejecución + outcome). `evolution_log.jsonl` registra **cambios al sistema** (propuestas + clasificación + resultado). Son logs complementarios: bridge.jsonl alimenta al AutoProposer; evolution_log alimenta al meta-análisis de cómo evoluciona el sistema.

### 4.7 Endpoints GUI del Orchestrator

> ⚠️ **C26:** Todos los endpoints deben usar `@require_auth` igual que los endpoints existentes en `server.py`.

| Endpoint | Método | Función | Auth |
|---|---|---|---|
| `/api/evolution/proposals` | GET | Lista propuestas pendientes (Cat.2 y Cat.3) | @require_auth |
| `/api/evolution/proposal/<id>` | GET | Detalle de una propuesta con análisis de impacto | @require_auth |
| `/api/evolution/proposal/<id>/approve` | POST | Aprueba y ejecuta | @require_auth |
| `/api/evolution/proposal/<id>/reject` | POST | Registra rechazo con razón | @require_auth |
| `/api/evolution/log` | GET | Historial de evoluciones (últimas 50) | @require_auth |
| `/api/evolution/stats` | GET | Estadísticas: propuestas/día, ratio aprobación | @require_auth |
| `/api/evolution/escalations` | GET | Propuestas que escalaron de categoría | @require_auth |

**C43: Endpoint de rechazo con actualización de reflexiones:**
```python
@app.route('/api/evolution/proposal/<id>/reject', methods=['POST'])
@require_auth
def reject_evolution_proposal(id):
    reason = request.json.get("reason", "")
    entry = memory_engine._must_get(id)
    data = json.loads(entry.content)
    data["status"] = "rejected"
    data["rejection_reason"] = reason
    entry.content = json.dumps(data)
    entry.tags.append("rejected")
    memory_engine._persist_memory_entry(entry)

    # Si la propuesta provenía de una reflexión crítica, actualizar la reflexión
    if "mantra_amendment" in entry.tags:
        reflections = memory_engine.search(
            query=data.get("proposal_id", ""),
            level=MemoryLevel.RELATIONS
        )
        for ref in reflections:
            ref_data = json.loads(ref.content)
            if ref_data.get("type") == "critical_reflection":
                ref_data["status"] = "rejected_by_human"
                ref_data["rejection_reason"] = reason
                ref.content = json.dumps(ref_data)
                ref.tags.append("rejected_by_human")
                memory_engine._persist_memory_entry(ref)

    orchestrator._append_evolution_log(
        TechnicalSpec(**data["spec"]),
        EvolutionResult(category=data["category"], status="REJECTED"),
        approved_by="human_rejected"
    )
    return jsonify({"status": "rejected", "reason": reason})
```
