## §3 — EL ORDEN DE CONSTRUCCIÓN (secuencia canónica, no negociable)

### 3.0 Resolución de la paradoja del bootstrap

Existe una dependencia circular: el Orchestrator clasifica propuestas de construcción, pero la primera propuesta de construcción es "construir el Orchestrator". ¿Quién clasifica esa propuesta?

**Resolución:** Las 3 primeras acciones se ejecutan en **modo bootstrap manual**. No pasan por ningún canal automático porque el canal no existe todavía. Se ejecutan como Categoría 3 directa con aprobación humana, usando el protocolo de CodeCraft Sage v3 existente (`codecraft_sage.py`, 190 líneas).

```
MODO BOOTSTRAP (acciones 1-3)
═══════════════════════════════════════════════════════

  Protocolo: CodeCraft Sage v3 manual
  Clasificación: Categoría 3 implícita (supervisado por humano)
  LLM: el que esté activo en la sesión actual
  Memoria: ficheros JSON en disco (sin MemoryPolicyEngine todavía)
  Persistencia: git commit en feature branch
  
  El Orchestrator v4 NO EXISTE durante los pasos 1-3.
  El Orchestrator v4 EXISTE al final del paso 3.
  Después del paso 3, todos los pasos siguientes pasan por el canal.
```

### 3.1 PASO 1 — Nivel IDENTITY en memoria (bootstrap)

**Objetivo:** Crear el nivel 5 de memoria para que este prompt pueda guardarse de forma persistente e inmune a degradación.

**Cambios técnicos requeridos:**

1. **Modificar `MemoryLevel` enum** en `domain/models/signal.py` (línea 162):
   ```python
   class MemoryLevel(str, Enum):
       RAW        = "0a"
       NORMALIZED = "0b"
       FACTS      = "1"
       RELATIONS  = "2"
       PLAYBOOKS  = "3"
       STRATEGY   = "4"
       IDENTITY   = "5"   # ← NUEVO: TTL=∞, inmune a degradación de régimen
   ```

2. **Actualizar `MemoryPolicyEngine`** en `learning/memory_policy.py`:
   - Añadir `MemoryLevel.IDENTITY` a `TTL_BY_LEVEL_HOURS` con valor `None`
   - Añadir `MemoryLevel.IDENTITY` a `APPROVER_BY_LEVEL` con valor `"human"`
   - Añadir `MemoryLevel.IDENTITY` a `LEVEL_ORDER` (después de STRATEGY)
   - **Guard en `detect_and_apply_regime_shift()`** (línea 199): 
     ```python
     for entry in self.entries.values():
         if entry.level == MemoryLevel.IDENTITY:
             continue  # ← GUARD: nivel IDENTITY nunca se degrada
         if entry.level == MemoryLevel.STRATEGY:
             # ... lógica existente
     ```

3. **Implementar recarga de memoria al inicio** (resuelve BUG-7):
   - Añadir método `load_from_disk(directory: str)` a `MemoryPolicyEngine`
   - Llamarlo en la inicialización del servidor (`server.py`) después de crear la instancia
   - El método lee todos los `*.json` de `memory/memory_entries/`, deserializa cada uno, y lo añade a `self.entries`

4. **Guardar este prompt como primera entrada IDENTITY:**
   ```python
   engine.ingest_raw(
       content="[contenido completo del prompt fundacional]",
       field="architect",
       source_type="primary",
       tags=["v4_genesis", "mantra", "identity"]
   )
   # Promover directamente a IDENTITY
   engine.promote(
       entry_id=entry.entry_id,
       target_level=MemoryLevel.IDENTITY,
       approved_by="human"
   )
   ```

**Validación:** Reiniciar el servidor y verificar que la entrada IDENTITY se recarga desde disco.

**Tests mínimos requeridos:**
- `test_identity_level_exists`
- `test_identity_not_degraded_by_regime_shift`
- `test_memory_loads_from_disk`
- `test_identity_entry_survives_restart`

**Persistencia:** Git commit en `feature/v4-identity-memory`

---

### 3.2 PASO 2 — LLM Switcher (bootstrap)

**Objetivo:** Configurar la selección inteligente de LLM por tipo de tarea, para que el Orchestrator (paso 3) pueda elegir el modelo adecuado para cada categoría.

**Cambios técnicos requeridos:**

1. **Crear `llm_switcher.py`** en `cgalpha_v3/lila/llm/`:
   ```python
   @dataclass
   class SwitcherConfig:
       enabled: bool = True
       manual_override: bool = False
       forced_llm: str | None = None

   class LLMSwitcher:
       def __init__(self, assistant: LLMAssistant, config: SwitcherConfig = None):
           self.assistant = assistant
           self.config = config or SwitcherConfig()
       
       def select_for_task(self, task_type: str) -> LLMProvider:
           if self.config.manual_override and self.config.forced_llm:
               self.assistant.switch_provider(self.config.forced_llm)
               return self.assistant.provider
           
           TASK_MATRIX = {
               "category_1": "ollama",      # coste=0, latencia baja
               "category_2": "openai",      # contexto medio, precio razonable
               "category_3": "openai",      # razonamiento arquitectónico
               "critical_reflection": "ollama",  # síntesis interna
               "semantic_search": None,      # no necesita LLM generativo
           }
           provider_name = TASK_MATRIX.get(task_type, "ollama")
           if provider_name:
               self.assistant.switch_provider(provider_name)
           return self.assistant.provider
   ```

2. **Guardar configuración del switcher en memoria** (nivel STRATEGY, TTL indefinido):
   ```json
   {
     "llm_switcher_enabled": true,
     "manual_override": false,
     "forced_llm": null,
     "task_matrix": {
       "category_1": "ollama",
       "category_2": "openai",
       "category_3": "openai",
       "critical_reflection": "ollama"
     }
   }
   ```

3. **Actualizar `openai_provider.py`** línea 17: Cambiar default de `gpt-3.5-turbo` a un modelo configurable via env var:
   ```python
   def __init__(self, api_key=None, model=None):
       self._model = model or os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
   ```

**Validación:** El switcher selecciona Ollama para tarea "category_1" y OpenAI para "category_3".

**Tests mínimos:**
- `test_switcher_selects_ollama_for_cat1`
- `test_switcher_selects_openai_for_cat3`
- `test_manual_override_forces_provider`
- `test_switcher_config_persists_in_memory`

**Persistencia:** Git commit en `feature/v4-llm-switcher`

---

### 3.3 PASO 3 — Orchestrator v4 (bootstrap → canal operativo)

**Objetivo:** Reemplazar el stub de 49 líneas (`evolution_orchestrator.py`) con un Orchestrator que clasifique, enrute y ejecute propuestas de evolución a través de las 3 categorías.

**Este es el paso que cierra el bootstrap.** Al final de este paso, el canal de evolución existe y todos los pasos posteriores pasan por él.

**Cambios técnicos requeridos:**

1. **Reescribir `evolution_orchestrator.py`** (~200-300 líneas):

   ```python
   class EvolutionOrchestrator_v4:
       def __init__(self, switcher: LLMSwitcher, sage: CodeCraftSage,
                    proposer: AutoProposer, memory: MemoryPolicyEngine):
           self.switcher = switcher
           self.sage = sage
           self.proposer = proposer
           self.memory = memory
       
       def route_proposal(self, spec: TechnicalSpec) -> EvolutionResult:
           # PASO 0: Seleccionar LLM
           category = self.classify(spec)
           llm = self.switcher.select_for_task(f"category_{category}")
           
           # PASO 1: Ejecutar según categoría
           if category == 1:
               return self._execute_automatic(spec)
           elif category == 2:
               return self._queue_semi_automatic(spec)
           else:
               return self._queue_supervised(spec)
       
       def classify(self, spec: TechnicalSpec) -> int:
           """
           Clasifica propuesta en categoría 1/2/3.
           Reglas deterministas primero, LLM como fallback.
           
           Campos reales de TechnicalSpec (proposer.py línea 6):
             change_type: str     # "parameter" | "feature" | "optimization"
             target_file: str     # fichero único (singular, no plural)
             target_attribute: str
             old_value: float
             new_value: float
             causal_score_est: float
           """
           # Cat.1: Cambio de un solo parámetro numérico con causal score alto
           if spec.change_type == "parameter" and spec.causal_score_est >= 0.75:
               return 1
           
           # Cat.3: Cambio de tipo "feature" (añade/elimina feature del modelo)
           if spec.change_type == "feature":
               return 3
           
           # Cat.3: Propuesta que contradice principio invariante
           if self._contradicts_identity(spec):
               return 3
           
           # Cat.2: Todo lo demás ("optimization", parámetros con causal bajo)
           return 2
       
       def _contradicts_identity(self, spec: TechnicalSpec) -> bool:
           """
           Determina si una propuesta contradice un principio invariante
           del mantra IDENTITY. Criterios concretos:
           
           1. Propone eliminar la Triple Barrera de tests
           2. Propone escribir directamente a main (viola CodeCraft contrato)
           3. Propone cambiar umbrales de seguridad por debajo de mínimos:
              - min_causal_accuracy < 0.55
              - min_oracle_confidence < 0.70
              - max_blind_test_ratio > 0.25
           4. Propone desactivar human_approval para niveles PLAYBOOKS+
           """
           SAFETY_THRESHOLDS = {
               "min_causal_accuracy": ("min", 0.55),
               "min_oracle_confidence": ("min", 0.70),
               "max_blind_test_ratio": ("max", 0.25),
           }
           if spec.target_attribute in SAFETY_THRESHOLDS:
               direction, limit = SAFETY_THRESHOLDS[spec.target_attribute]
               if direction == "min" and spec.new_value < limit:
                   return True
               if direction == "max" and spec.new_value > limit:
                   return True
           return False
   ```

2. **Conectar las 4 islas:**

   ```python
   # En pipeline.py, al final de run_cycle():
   proposals = self.proposer.analyze_drift(cycle_metrics)
   for spec in proposals:
       result = self.orchestrator.route_proposal(spec)
       self.memory.ingest_raw(
           content=f"Propuesta {spec.target_attribute}: {result.status}",
           field="architect",
           tags=["evolution", f"cat_{result.category}"]
       )
   ```

3. **Conectar `ChangeProposer` y `ExperimentRunner` al canal:**
   - Las `Proposal` del `ChangeProposer` se convierten en `TechnicalSpec` adaptadas
   - Los resultados del `ExperimentRunner` se retroalimentan al Oracle y al Orchestrator
   - El Orchestrator recibe tanto `TechnicalSpec` (del AutoProposer) como `Proposal` (del ChangeProposer) a través de un adaptador común

4. **Implementar `_execute_automatic()` (Cat.1):**
   ```python
   def _execute_automatic(self, spec: TechnicalSpec) -> EvolutionResult:
       # 1. CodeCraftSage aplica el patch
       result = self.sage.execute_proposal(
           spec, ghost_approved=True, human_approved=True
       )
       
       # 2. Si tests pasan, persistir
       if result.status == "COMMITTED":
           self.memory.ingest_raw(
               content=f"Auto-evolution: {spec.target_attribute} "
                       f"{spec.old_value} → {spec.new_value}",
               field="codigo",
               tags=["auto_evolution", "cat_1"]
           )
       
       return EvolutionResult(
           category=1, status=result.status,
           commit_sha=result.commit_sha
       )
   ```

5. **Implementar `_queue_semi_automatic()` (Cat.2) y `_queue_supervised()` (Cat.3):**
   - Ambos crean un `PendingProposal` en memoria nivel FACTS
   - Cat.2 se muestra en la GUI con botones [APROBAR] [RECHAZAR]
   - Cat.3 genera un documento técnico completo para revisión en sesión

6. **Endpoint GUI para aprobación de propuestas:**
   ```python
   @app.route('/api/evolution/proposals', methods=['GET'])
   # Lista propuestas pendientes de Cat.2 y Cat.3
   
   @app.route('/api/evolution/proposal/<id>/approve', methods=['POST'])
   # Aprueba y ejecuta con flujo Cat.1
   
   @app.route('/api/evolution/proposal/<id>/reject', methods=['POST'])
   # Registra rechazo y razón en bridge.jsonl
   ```

**Validación end-to-end:** Inyectar un `TechnicalSpec` de prueba, verificar que se clasifica, se enruta al `CodeCraftSage`, y produce un commit en feature branch.

**Tests mínimos:**
- `test_classify_parameter_change_is_cat1`
- `test_classify_structural_change_is_cat3`
- `test_route_cat1_produces_commit`
- `test_route_cat2_queues_for_approval`
- `test_route_cat3_requires_human_session`
- `test_pipeline_sends_proposals_to_orchestrator`
- `test_rejected_proposal_recorded_in_bridge`

**Persistencia:** Git commit en `feature/v4-evolution-orchestrator`

**⚠️ A PARTIR DE ESTE PUNTO EL BOOTSTRAP HA TERMINADO.** El Orchestrator existe. Todo cambio posterior se propone, clasifica y ejecuta a través del canal.

---

### 3.4 PASO 4 — Parameter Landscape Map (via canal, Cat.2)

**Objetivo:** Crear un mapa de calor de todos los parámetros configurables del sistema, con su sensibilidad medida y su impacto causal estimado. Esta es la **primera prueba real del canal**: una propuesta que nace en el sistema, pasa por el Orchestrator, y produce un artefacto útil.

**Por qué Cat.2:** Crear un mapa de parámetros requiere escanear múltiples ficheros y generar un artefacto nuevo (no es un simple ajuste de valor), pero no cambia la estructura del sistema ni toca la identidad.

**Flujo esperado:**
```
1. Lila v4 genera TechnicalSpec:
   type: "optimization"
   target: "parameter_landscape_map.json"
   description: "Escaneo de todos los parámetros configurables del pipeline"

2. Orchestrator clasifica: Cat.2 (semi-automático)
   → Switcher selecciona GPT/Gemini para análisis

3. Generación híbrida (principio: "Determinista primero, LLM como fallback"):
   
   a) AST/grep estático (determinista) extrae datos factuales:
      - Nombre del parámetro, fichero, línea, valor actual, tipo
      - No se delega al LLM lo que puede calcularse
   
   b) LLM aporta solo estimaciones cualitativas:
      - sensitivity ("high"/"medium"/"low")
      - causal_impact_est (0.0-1.0)
      - Basado en contexto del NORTH_STAR y bridge.jsonl
   
   Resultado:
   {
     "parameters": [
       {
         "name": "volume_threshold",
         "file": "pipeline.py",
         "line": 61,                    // ← AST, no LLM
         "current_value": 1.2,          // ← AST, no LLM
         "type": "float",               // ← AST, no LLM
         "sensitivity": "high",         // ← LLM
         "causal_impact_est": 0.72,     // ← LLM
         "auto_proposer_refs": 3        // ← grep cuenta de refs
       },
       ...
     ]
   }

4. Operador revisa → aprueba → mapa se guarda en memoria nivel 2

5. AutoProposer usa el mapa para priorizar sus propuestas futuras
```

**Validación:** El mapa tiene al menos 15 parámetros identificados con sus ficheros y líneas reales.

---

### 3.5 PASO 5 — CodeCraft Sage v4 (via canal, Cat.2)

**Objetivo:** Mejorar el `CodeCraftSage` existente para trabajar de forma nativa con el Orchestrator. El Sage actual funciona (190 líneas, regex patching), pero puede extenderse para soportar:

- Patches más complejos que un solo parámetro (AST-based)
- Rollback automático si los tests fallan post-merge
- Feedback loop al Orchestrator con el resultado de la ejecución

**Por qué Cat.2:** Mejora un componente existente sin cambiar la arquitectura.

**Flujo:** Se propone como `TechnicalSpec` al Orchestrator → se clasifica Cat.2 → operador aprueba → se implementa.

---

### 3.6 PASO 6 — Oracle fixes (via canal, Cat.1 y Cat.2)

**Objetivo:** Arreglar los 6 bugs del Oracle y sus pipelines upstream. Cada fix es una propuesta independiente al Orchestrator.

**Mapa de fixes y su categoría estimada:**

| Bug | Fix | Categoría |
|---|---|---|
| BUG-1: Sin train/test split | Añadir `train_test_split(X, y, test_size=0.2)` en `train_model()` | Cat.1 — cambio localizado en un fichero |
| BUG-2: Sin persistencia | Llamar `save_to_disk()` después de `train_model()` y `load_from_disk()` al iniciar | Cat.1 — dos invocaciones nuevas |
| BUG-3: Class imbalance | Implementar SMOTE o ajustar threshold dinámicamente | Cat.2 — requiere análisis |
| BUG-4: Placeholder indistinguible | Añadir `is_placeholder: bool` a `OraclePrediction` | Cat.1 — un campo nuevo |
| BUG-5: Outcome labeling | Reescribir `_determine_outcome()` usando `zone_top`/`zone_bottom` | Cat.2 — cambia la lógica de etiquetado |
| BUG-6: Pipeline no reentrena | Añadir `self.oracle.train_model()` después de `load_training_dataset()` | Cat.1 — una línea |
| BUG-8: GUI stubs | Implementar persistencia en `training_approvals.jsonl` | Cat.2 — requiere nuevo schema |

**Nota:** BUG-5 debe arreglarse ANTES que BUG-3. Balancear labels basura produce un modelo que aprende basura equilibrada. Primero corregir los labels, después balancear las clases.

**Orden de ejecución recomendado (Cat.1 primero, con justificación):**
```
BUG-4 (Cat.1) → Primero: añade is_placeholder a OraclePrediction.
                 Sin esta flag, no hay forma de saber si los fixes
                 posteriores (BUG-2, BUG-6, BUG-1) realmente cambiaron
                 el comportamiento del Oracle. Es el sensor de observabilidad.

BUG-2 (Cat.1) → Segundo: activa save/load_from_disk().
                 Sin persistencia, los fixes siguientes se pierden
                 al reiniciar. Depende de BUG-4 para verificar que
                 el modelo cargado desde disco es real, no placeholder.

BUG-6 (Cat.1) → Tercero: añade train_model() en pipeline.
                 Ahora que el modelo se persiste (BUG-2) y se puede
                 distinguir de placeholder (BUG-4), reentrenar tiene
                 efecto duradero.

BUG-1 (Cat.1) → Cuarto: añade train_test_split.
                 Ahora que el pipeline reentrena (BUG-6), el split
                 produce métricas OOS reales por primera vez.

→ Luego los Cat.2, secuenciales:
BUG-5 (Cat.2) → Reescribir _determine_outcome() con zone limits.
                 ANTES de BUG-3: labels correctos antes de balancear.
BUG-3 (Cat.2) → Implementar SMOTE o threshold dinámico.
                 Ahora las clases tienen labels correctos.
BUG-8 (Cat.2) → Implementar persistencia approve/reject.
                 Habilita curación manual del dataset.
```

Los Cat.1 se pueden ejecutar en paralelo. Los Cat.2 requieren aprobación humana secuencial.

---

### 3.7 Resumen visual de la secuencia

```
FASE BOOTSTRAP (manual, Cat.3 implícita, sin canal)
══════════════════════════════════════════════════════

PASO 1 ─── IDENTITY Memory ──────── feature/v4-identity-memory
  │         └── BUG-7 fix incluido
  │         └── Prompt guardado en nivel 5
  ▼
PASO 2 ─── LLM Switcher ─────────── feature/v4-llm-switcher
  │         └── Matriz de selección por tipo de tarea
  │         └── gpt-3.5-turbo → gpt-4o-mini default
  ▼
PASO 3 ─── Orchestrator v4 ──────── feature/v4-evolution-orchestrator
            └── 4 islas conectadas
            └── 3 categorías operativas
            └── GUI endpoints para aprobación

═══════ BOOTSTRAP COMPLETO ═══════ CANAL OPERATIVO ═════════

FASE CANAL (propuestas vía Orchestrator)
══════════════════════════════════════════════════════

PASO 4 ─── Parameter Landscape Map ── Cat.2 → aprobación → artefacto

PASO 5 ─── CodeCraft Sage v4 ──────── Cat.2 → aprobación → mejora

PASO 6 ─── Oracle fixes ──────────── Cat.1 × 4 + Cat.2 × 3
            └── Orden: BUG-4 → BUG-2 → BUG-6 → BUG-1
            └── Luego: BUG-5 → BUG-3 → BUG-8
```

### 3.8 Invariante de la secuencia

**Ningún paso puede adelantarse a su predecesor.** La justificación es un orden topológico de dependencias:

| Paso | Depende de | Razón |
|---|---|---|
| 1 (IDENTITY) | Nada | Primer paso absoluto |
| 2 (Switcher) | Paso 1 | La config del switcher se guarda en memoria. Sin persistencia, se pierde. |
| 3 (Orchestrator) | Pasos 1 y 2 | El Orchestrator usa el Switcher (paso 0 interno) y persiste resultados en memoria. |
| 4 (Landscape) | Paso 3 | Primera propuesta real que pasa por el canal. Sin canal, no hay cómo ejecutarla formalmente. |
| 5 (Sage v4) | Paso 3 | Mejora propuesta como Cat.2 al Orchestrator. |
| 6 (Oracle) | Pasos 3, 4 y 5 | Los fixes se priorizan con el Parameter Landscape Map y se implementan con el Sage mejorado. |

Si en algún momento te ves tentada a saltar un paso porque "es rápido", recuerda: v3 hizo exactamente eso — implementó componentes capaces en orden aleatorio y terminó con 4 islas desconectadas. El orden es el puente.
