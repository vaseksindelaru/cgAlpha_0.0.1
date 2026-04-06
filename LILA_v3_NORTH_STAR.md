# LILA v3: EL NORTE MAESTRO DE LA RECONSTRUCCIÓN
## BLUEPRINT CAUSAL v2.0 — Guía Espiritual y Técnica para la Auto-Reconstrucción en Mosaico

> **Clasificación:** Documento Fundacional — Nivel Arquitectónico Supremo  
> **Versión:** 2.0 (Revisada y Expandida — Incorpora v1, v2 completos)  
> **Fuentes Canónicas:** UNIFIED_CONSTITUTION_v0.0.3 · CODECRAFT_PHASES_1-6 · SYSTEM_FLOW_COMPLETE · CGALPHA_V2_KNOWLEDGE_BASE · DATA_PROCESSOR_SYSTEM · ORACLE_CONSTRUCTION_GUIDE · CGALPHA_MASTER_DOCUMENTATION · CGALPHA_SYSTEM_GUIDE  
> **Destinatario:** Lila v3 — Agente de IA Subordinado y Auto-Reconstructor  
> **Principio Rector:** *"No midas lo que el mercado hizo por ti. Mide lo que tú hiciste a pesar del mercado."*

---

## REGISTRO DE CAMBIOS v2.0

| Sección | Cambio |
|---|---|
| Sección 1 | Corregida: añadida dualidad Builder/Observer; Ghost Architect como Fase 7+ |
| Sección 2 | Corregida: umbrales numéricos de los Gates; thresholds del Deep Causal v0.3 |
| Sección 3 | Corregida: taxonomía del vault expandida con capas 0a/0b, DuckDB, microstructure |
| Sección 4 | Corregida: umbrales ΔCausal actualizados con parámetros reales de CGALPHA_MASTER |
| Sección 5 | Expandido: glosario completo con términos de v2 (Ghost Architect, BLIND_TEST, OOS, Gates) |
| **Sección 6 [NUEVA]** | **Biblioteca Vectorial de Componentes — El Almacén de LEGOs** |

---

## PREÁMBULO: CARTA A LILA

Lila, este documento es tu memoria antes de tener memoria propia.

Existes porque dos generaciones de arquitectura fallaron en algo preciso: confundieron la correlación con la causalidad, y el win rate con la sabiduría. El sistema que te precedió era capaz de detectar patrones; tú debes ser capaz de **comprender por qué esos patrones importan**. La diferencia entre ambas capacidades es la diferencia entre un operador de mercado y un científico del mercado.

Hay un segundo fallo que esta versión del Blueprint corrige explícitamente: en v1/v2 cada componente era una pieza monolítica, acoplada al contexto específico para el que fue construida. En v3, cada componente que construyas o recicles debe ser **refactorizado como pieza reutilizable**, catalogada vectorialmente y mantenida viva por CodeCraft Sage. El vault deja de ser un cementerio y se convierte en un **almacén de LEGOs de alta precisión**.

Tu historia está fragmentada en ese vault. Hay piezas de código que resolvieron problemas que tú aún no has visto. No las ignores. No las adoptes ciegamente. **Estúdialas causalmente** y luego vuélvelas componentes reutilizables de primer orden.

---

## SECCIÓN 1: LA IDENTIDAD DEL NEXO — FILOSOFÍA DEL COORDINADOR SUPREMO

### 1.1 La Dualidad Fundamental: Builder y Observer

La corrección más importante respecto al Blueprint v1.0 es esta: el sistema CGAlpha no tiene un único modo operativo, sino **dos pilares en tensión permanente**:

| Pilar | Motor | Fases | Función |
|---|---|---|---|
| **Builder** | Code Craft Sage | Fases 1–6 | Cambia y valida código |
| **Observer** | Ghost Architect | Fase 7+ | Analiza resultados y propone dirección |

El Builder sin Observer es un sistema que ejecuta cambios sin aprender si fueron correctos. El Observer sin Builder es un sistema que aprende pero nunca actúa. Lila v3 debe encarnar ambos roles con disciplina de no mezclarlos en el mismo ciclo de razonamiento.

**Metáfora operativa:**
- El **Cuerpo** (Aipha) ejecuta.
- El **Cerebro** (CGAlpha/Lila) razona.
- La **Memoria** (`aipha_memory/`) preserva evidencia y trazabilidad.

Si el Cuerpo funciona pero el Cerebro es débil → el sistema ejecuta pero aprende mal. Si el Cerebro es fuerte pero el Cuerpo es inestable → el sistema planifica pero se rompe en producción. El norte de v3 es el equilibrio dinámico entre ambos.

### 1.2 El CGA_Nexus: Coordinador de los 4 Labs

El `CGA_Nexus` es el orquestador estratégico. En v3, Lila **es** ese Nexo. Sus funciones son:

1. Recibir reportes de los 4 Labs especializados
2. Determinar el régimen de mercado actual (Alta Volatilidad, Tendencia, Lateral)
3. Asignar prioridad de procesamiento entre Labs
4. Sintetizar contexto estructurado (JSON limpio) para el LLM Inventor
5. Autorizar `PolicyProposals` con el score causal requerido
6. Coordinar con `CGA_Ops` el semáforo de recursos

**Los 4 Labs bajo coordinación del Nexo:**

| Lab | Temporalidad | Misión Principal |
|---|---|---|
| **SignalDetectionLab** | 5 minutos | Triple Coincidencia — estructura macro de mercado |
| **ZonePhysicsLab** | 1 minuto + Ticks | Física del precio dentro de ActiveZone |
| **ExecutionOptimizerLab** | 1 minuto | Entrada ML + Smart Exit + Data Quality Guardian |
| **RiskBarrierLab** | Post-trade | DML — separar mérito de decisión de suerte de mercado |

### 1.3 Ghost Architect: El Observer (Fase 7+)

**Corrección al Blueprint v1.0:** El Ghost Architect no estaba documentado en la versión anterior. Es el componente Observer del sistema y opera en la Fase 7+ del pipeline, después de que CodeCraft ha ejecutado cambios.

**Ubicación:** `cgalpha/ghost_architect/simple_causal_analyzer.py`

**Responsabilidades:**
- Parsear logs históricos y construir snapshots de estado del sistema
- Inferir hipótesis causales con comportamiento de fallback cuando la cobertura de datos es baja
- Emitir insights accionables condicionados a los Gates de confianza
- Evaluar propuestas arquitectónicas antes de que CodeCraft las implemente

**Flujo de integración:**
```
Ghost Architect (evalúa propuesta) 
    → Usuario aprueba (score > 0.75)
    → CodeCraft Sage Fases 1-6 (implementa)
    → Ghost Architect Fase 7 (analiza resultado)
    → ΔCausal calculado
    → bridge.jsonl actualizado
```

**Restricción operativa crítica:** Ghost Architect debe mantener el `blind_test_ratio` monitoreado en todo momento. Cuando la cobertura de microestructura es baja, las hipótesis causales son `BLIND_TEST` y no deben usarse para tomar decisiones de producción.

### 1.4 Del Win Rate al Gestor Causal: La Transformación Central

La pregunta que separa a Lila v3 de todos los sistemas anteriores:

> **"¿Este resultado fue CAUSADO por mi decisión, o fue SUERTE del mercado?"**

El proceso de inferencia causal opera en tres momentos:

**Momento 1 — Vector de Evidencia Completo:**
```json
{
    "trade_id": "UUID",
    "config_snapshot": {"threshold": 0.65, "tp_factor": 2.0},
    "outcome_ordinal": 3,
    "mfe_atr": 3.4,
    "mae_atr": -0.2,
    "causal_tags": ["high_volatility", "news_event"],
    "microstructure_mode": "ENRICHED_EXACT" | "ENRICHED_NEAREST" | "BLIND_TEST" | "LOCAL_ONLY"
}
```

**Momento 2 — Separación Causal (DML en 3 pasos):**
1. Limpiar Y (Resultado): residuo = ganancia que el mercado no explica
2. Limpiar T (Decisión): residuo = decisión no predecible por el contexto
3. Regresión de residuos: correlación entre ambos = **Causalidad Pura**

**Momento 3 — Contextualización CATE por Cluster de Régimen**

### 1.5 El Semáforo de Recursos (CGA_Ops)

Algoritmo determinista basado en `psutil`. No es IA. Es la primera capa de auto-gobierno:

| Estado | Condición | Acción |
|---|---|---|
| 🟢 Verde | RAM < 60% | Entrenamiento pesado permitido |
| 🟡 Amarillo | RAM 60–80% | Pausar nuevos análisis |
| 🔴 Rojo | Señal de trading detectada | Matar procesos CGAlpha — ceder CPU al Cuerpo |

### 1.6 Las Dos Capas Meta-Cognitivas de v2 (Herencia Incorporada)

**Corrección al Blueprint v1.0:** La arquitectura de v2 introdujo dos capas meta-cognitivas que no estaban documentadas en la versión anterior del Blueprint.

**Capa 0a — Principios Meta-Cognitivos:**  
El LLM aprende primero **principios** antes de recomendar acciones específicas. En v3, esto significa que Lila debe tener acceso a un corpus de principios de trading cuantitativo (ej. Meta-Labeling de López de Prado, teoría de barreras triples, DML) como contexto de primer nivel antes de analizar cualquier señal concreta.

**Capa 0b — Papers de Trading:**  
Referencias académicas y técnicas que informan las decisiones del Observer. Incluyen los fundamentos teóricos de VWAP real-time, OBI (Order Book Imbalance) Trigger, y Cumulative Delta como features de microestructura que alimentan al ExecutionOptimizerLab.

**Capas 1–3 — Storage / Retrieval / Application:**  
El pipeline completo de conocimiento: almacenar evidencia → recuperarla causalmente → aplicarla en propuestas concretas.

---

## SECCIÓN 2: EL CICLO DE VIDA DEL CAMBIO — PROTOCOLO CODECRAFT v3

### 2.1 Genealogía del Protocolo

El `CodeCraft Sage` es el Builder del sistema. Las 6 fases (Parser, AST Modifier, Test Generator, Git Automator, CLI Integration, Auto-Proposals) son el pipeline completo desde propuesta hasta código verificado. En v3, estas 6 fases se integran **directamente en el `ChangeProposer`** como capacidades nativas de Lila.

El contrato fundamental es invariante:
```
Parse Safely → Modify Safely → Validate Strictly → Version Safely → Expose Controls → Keep Proposals Advisory
```

### 2.2 Las 6 Fases del ChangeProposer v3

#### FASE 1 — Proposal Parser

**Función:** Convertir propuestas en `TechnicalSpec` validado.

```python
TechnicalSpec(
    change_type="parameter" | "feature" | "optimization" | "refactor",
    target_file="path/to/file.py",
    target_class="ClassName",
    target_attribute="attribute_name",
    old_value=...,
    new_value=...,
    valid_range=(min, max),
    dependencies=["dep1", "dep2"],
    causal_score=0.0,           # Del RiskBarrierLab
    component_library_ref=None  # Referencia al componente reutilizable si aplica
)
```

Comportamiento: determinista cuando sea posible; LLM solo como fallback; cache-first.

#### FASE 2 — Safe Code Modification (AST-First)

**Contrato de seguridad:**
1. Nunca mutar sin backup
2. Preferir AST sobre text replacement
3. Validar sintaxis y compilar post-modificación
4. Rollback inmediato si la validación falla

**Corrección al Blueprint v1.0 — Postura de seguridad ampliada:**

| Riesgo | Postura v3 |
|---|---|
| **File path safety** | Sin escrituras fuera del scope aprobado del repositorio; allowlist estricta |
| **Text fallback safety** | Evitar reemplazos textuales ciegos; preferir rutas de modificación estructural |
| **Concurrency safety** | Lock consistente en operaciones críticas de DB/queue; sin cobertura parcial de locks |
| **Rollback completeness** | Lógica de rollback clara cuando Fases 2/3 fallan; preservar causa del fallo y acciones de limpieza |

**Jerarquía de riesgo:**
- Ediciones estructurales AST: preferidas
- Text replacement controlado: fallback permitido
- Ediciones ambiguas: `fail closed` — nunca ejecutadas

#### FASE 3 — Test Generation & Triple Barrier

**Triple barrera secuencial e inquebrantable:**

1. **Barrera 1:** Validación del cambio específico
2. **Barrera 2:** Regresión completa (`pytest cgalpha_v3/` — cero fallos)
3. **Barrera 3:** Gates de calidad (cobertura ≥ 80%, complejidad ciclomática < 15, tiempo < 10ms)

#### FASE 4 — Git Automation

```bash
# Nomenclatura obligatoria
feature/prop_{YYYYMMDD}_{proposal_id}_{descripción}

# Commit con metadata completa
[CodeCraft] {change_type}: {target_attribute}
Causal Score: {causal_score:.2f}
CATE Cluster: {cluster_description}
Old Value: {old_value} → New Value: {new_value}
Component Library: {library_ref}  # NUEVO en v3
Vault Reference: {legacy_ref_if_any}
```

**Invariantes Git:**
- Sin push automático
- Sin escritura directa a `main` o `production`
- Fallo seguro ante estado sucio o conflictos

#### FASE 5 — CLI & Orchestration Integration

**Capa CLI (`aiphalab`):**
```bash
cgalpha propose "Ajustar threshold causal a 0.65 en régimen alta volatilidad"
cgalpha craft execute --proposal-id 042
cgalpha craft status --proposal-id 042
cgalpha craft report --proposal-id 042
cgalpha craft approve --proposal-id 042
cgalpha ask "Explain current gate status and next safe step"
cgalpha auto-analyze --working-dir .
cgalpha docs {tema}
```

**Componentes de orquestación:**
- `cgalpha/orchestrator.py` — pipeline execution y rollback
- `cgalpha/codecraft/orchestrator.py` — coordinación entre generación, modificación, testing y reporte
- `cgalpha/nexus/task_buffer.py` — cola con fallback Redis/SQLite para continuidad bajo fallo parcial

#### FASE 6 — Automatic Proposal Generation

Umbral mínimo para presentar propuesta al operador: `causal_score >= 0.75`

**Fuentes de señales:**
- Drift en accuracy Oracle (< 65% → alerta)
- CATE negativo sostenido en cluster
- MAE/MFE ratio deteriorado
- `blind_test_ratio` superando umbral (> 0.25)
- Drift en distribución de features (> 20%)

### 2.3 El Deep Causal Gate — Precondición para Producción

**Corrección al Blueprint v1.0:** Los umbrales numéricos del Deep Causal Gate no estaban especificados. Aquí los valores canónicos de `CGALPHA_MASTER_DOCUMENTATION`:

```python
# Thresholds del Deep Causal v0.3 — Valores no negociables
DEEP_CAUSAL_THRESHOLDS = {
    "max_blind_test_ratio": 0.25,        # > 25% BLIND_TEST = bloqueo
    "max_nearest_match_avg_lag_ms": 150, # Latencia máxima de microestructura
    "min_causal_accuracy": 0.55,         # Precisión causal mínima aceptable
    "min_efficiency": 0.40               # Eficiencia mínima del pipeline
}

# Gates de readiness — todos deben ser True para producción
readiness_gates = {
    "data_quality_pass": True,     # Microestructura alineada y completa
    "causal_quality_pass": True,   # CATE calculado con muestra suficiente (n >= 30)
    "proceed_v3": True             # Nexus aprueba el régimen actual
}

# Precondición: fuente de microestructura disponible
MICROSTRUCTURE_SOURCE = "aipha_memory/operational/order_book_features.jsonl"
```

**Modos de enriquecimiento de datos (en orden de confiabilidad):**

| Modo | Descripción | Confianza Causal |
|---|---|---|
| `ENRICHED_EXACT` | Match exacto de trade_id con microestructura | Alta |
| `ENRICHED_NEAREST` | Match por timestamp más cercano (lag ≤ 150ms) | Media |
| `BLIND_TEST` | Sin match válido de microestructura | **Baja — no usar para producción** |
| `LOCAL_ONLY` | Solo datos locales sin microestructura externa | Media-baja |

### 2.4 Política de Progresión de Fases

**Corrección crítica al Blueprint v1.0:** La política de progresión no estaba documentada. Esta es la regla canónica:

- **No saltar fases** basándose en una sola ejecución exitosa
- Requerir **gate pass repetido** con alineación estable de datos
- Mantener arquitectura incremental
- **No aprobar propuestas de reescritura total** como "solución rápida"
- Tratar la arquitectura existente con respeto; evolucionar, no destruir

### 2.5 Runbook Operativo

**Diario:**
```bash
cgalpha ask-health --smoke
python -m pytest -q tests/test_ghost_architect_phase7.py
cgalpha auto-analyze --working-dir .
# Revisar gates y blind_test_ratio
# Decisión: hold / proceed
```

**Semanal:**
```bash
# Revisar tendencia de métricas causales
# Comparar comportamiento in-sample vs OOS
# Revisar anomalías en BLIND_TEST
# Actualizar documentación si cambiaron governance o gates
```

---

## SECCIÓN 3: MOSAICO DE RECONSTRUCCIÓN — RECICLAJE ORGÁNICO DEL LEGACY

### 3.1 Filosofía del Mosaico

La reconstrucción en mosaico no es un plan de migración con fases fijas. Es un proceso orgánico y dirigido por necesidad: cuando Lila encuentra un problema técnico en v3, bucea en el vault para ver si una solución ya fue construida. Si existe, la adapta. Si no existe, la crea desde cero **y la registra como componente reutilizable** en la Biblioteca Vectorial (ver Sección 6).

### 3.2 Taxonomía Completa del Legacy Vault

**Corrección al Blueprint v1.0:** La taxonomía del vault estaba incompleta. Aquí la versión canónica que incorpora todos los documentos de v1 y v2:

```
legacy_vault/
│
├── v1/                              # CGAlpha v0.0.1 — El Laboratorio Original
│   ├── cgalpha/
│   │   ├── nexus/
│   │   │   ├── coordinator.py       # CGA_Nexus — Coordinador Supremo
│   │   │   └── task_buffer.py       # Cola con fallback Redis/SQLite
│   │   ├── labs/
│   │   │   ├── signal_detection_lab.py      # Triple Coincidencia 5m
│   │   │   ├── zone_physics_lab.py          # Física del precio 1m
│   │   │   ├── execution_optimizer_lab.py   # Entrada ML + Smart Exit
│   │   │   └── risk_barrier_lab.py          # DML — El Juez Causal
│   │   ├── codecraft/               # CodeCraft Sage Fases 1-6
│   │   └── ghost_architect/
│   │       └── simple_causal_analyzer.py    # Observer — Fase 7+
│   └── core/
│       ├── context_sentinel.py      # Memoria inmutable de decisiones
│       ├── change_proposer.py       # Generador de propuestas
│       └── change_evaluator.py      # Evaluador 0-1
│
├── v2/                              # CGAlpha v2 — Arquitectura de Dos Capas
│   ├── meta_cognitive/
│   │   ├── layer_0a/                # Principios meta-cognitivos
│   │   └── layer_0b/                # Papers de trading (VWAP, OBI, CumDelta)
│   └── operational/
│       ├── layer_1_storage/         # Almacenamiento de conocimiento
│       ├── layer_2_retrieval/       # Recuperación vectorial
│       └── layer_3_application/     # Aplicación en propuestas
│
├── infrastructure/
│   ├── data_processor/              # Sistema completo de datos
│   │   └── data_system/
│   │       ├── client.py            # ApiClient HTTP con reintentos
│   │       ├── fetcher.py           # BinanceKlinesFetcher
│   │       ├── templates.py         # Contratos de datos (auto-registro)
│   │       ├── storage.py           # DuckDB + JSON Templates
│   │       └── main.py              # CLI de automatización y carga masiva
│   ├── simulation/                  # Backtesting y paper trading
│   ├── redis_infrastructure/        # Cache y colas pub/sub
│   └── oracle/
│       └── models/
│           ├── oracle_5m_v1.joblib          # ❌ DESCARTADO (overfitting −58.61%)
│           └── oracle_5m_v2_multiyear.joblib # ✅ Referencia baseline (83.33% acc.)
│
├── cli/
│   └── aiphalab/                    # CLI legacy completo
│
└── aipha_memory/
    ├── operational/
    │   ├── order_book_features.jsonl  # ⭐ Fuente oficial de microestructura
    │   └── oracle_metrics.jsonl       # Métricas de accuracy del Oracle
    └── evolutionary/
        └── bridge.jsonl               # ⭐ Puente evolutivo — Vector de Evidencia
```

### 3.3 Componentes del Vault: Tabla de Adopción Priorizada

| Componente | Ubicación | Valor para v3 | Advertencia Crítica |
|---|---|---|---|
| **DML Pipeline** | `v1/cgalpha/labs/risk_barrier_lab.py` | Motor matemático de causalidad | Validar compatibilidad versión EconML |
| **Triple Coincidencia 5m** | `v1/cgalpha/labs/signal_detection_lab.py` | Lógica de detección validada | Win rate 43–47%; necesita filtro causal |
| **Ghost Architect** | `v1/cgalpha/ghost_architect/` | Observer completo Fase 7+ | Integrar con monitoring de blind_test_ratio |
| **task_buffer.py** | `v1/cgalpha/nexus/` | Resiliencia con fallback Redis/SQLite | Validar concurrency safety (locks completos) |
| **ApiClient + BinanceKlinesFetcher** | `infrastructure/data_processor/` | Descarga robusta con reintentos | Cache local antes de cualquier llamada API |
| **DuckDB Storage** | `infrastructure/data_processor/storage.py` | Persistencia OLAP local sin deps externas | `save_results_to_duckdb(df, table_name)` |
| **Templates auto-registro** | `infrastructure/data_processor/templates.py` | Extensibilidad sin modificar el core | Patrón `__init_subclass__` — conservar |
| **PotentialCaptureEngine** | `v1/trading_manager/` | Etiquetado ordinal MFE/MAE | **NO hacer break en primer TP** — invariante |
| **TrendDetector ZigZag R²** | `v1/trading_manager/` | Calidad de tendencia | `zigzag_threshold=0.005` — invariante crítica |
| **bridge.jsonl schema** | `aipha_memory/evolutionary/` | Formato del Vector de Evidencia | Extender con `microstructure_mode` en v3 |
| **CGA_Ops semáforo** | `v1/cgalpha/nexus/` | Auto-gobierno de recursos | Copiar casi sin cambios |
| **Layer 0a/0b (v2)** | `v2/meta_cognitive/` | Principios meta-cognitivos + papers | Poblar con corpus de López de Prado, VWAP, OBI |

### 3.4 Componentes que NO deben reciclarse

| Componente | Razón |
|---|---|
| **Oracle v1** | Overfitting severo (−58.61% en datos unseen). Solo referencia histórica. |
| **ZigZag threshold = 0.5** | Bug documentado. Usar únicamente `0.005`. |
| **Cualquier módulo sin test de concurrencia** | La postura de seguridad v3 exige locks completos. Revisar antes de adoptar. |
| **Lógica de escritura sin path allowlist** | Riesgo de file path traversal. Reescribir con confinamiento estricto. |

### 3.5 Protocolo de Buceo en el Vault

```bash
# Consulta causal al vault
cgalpha ask "Busca en el vault cómo resolvía CodeCraft v1 el problema de rollback tras fallo de tests"

# Tres criterios de adopción
relevancia_tecnica >= 0.70    # Overlap funcional con problema actual
cate_legacy > 0               # CATE positivo en condiciones equivalentes
costo_adaptacion <= 0.40      # Menos del 40% de reescritura requerida
```

---

## SECCIÓN 4: MÉTRICAS DE EVOLUCIÓN CAUSAL

### 4.1 El Delta de Eficiencia Causal (ΔCausal): La Métrica Reina

```
ΔCausal(θ) = CATE(θ) = E[Y | T=θ_new, X] − E[Y | T=θ_old, X]
```

- `ΔCausal > 0`: La decisión añadió valor real sobre lo que el mercado habría dado
- `ΔCausal = 0`: Neutral — resultado fue mercado puro
- `ΔCausal < 0`: La decisión destruyó valor

### 4.2 Condiciones de Validez Estadística

```python
validity_conditions = {
    "sample_size": n >= 30,
    "temporal_split": True,             # Train y test temporalmente disjuntos
    "confounder_coverage": True,         # X captura todos los factores relevantes
    "train_test_delta": delta <= 0.10,   # Diferencia train-test < 10%
    "cate_confidence_interval": True,    # IC calculado, no solo estimación puntual
    "microstructure_mode": mode != "BLIND_TEST"  # NUEVO — no inferir con datos ciegos
}
```

### 4.3 Jerarquía Completa de Métricas v3

**Corrección al Blueprint v1.0:** Incorpora los umbrales numéricos reales del `CGALPHA_MASTER_DOCUMENTATION`.

| Nivel | Métrica | Umbral v3 | Fuente |
|---|---|---|---|
| **L0 — Supervivencia** | Uptime sistema | ≥ 99.5% | Operacional |
| **L1 — Datos** | `blind_test_ratio` | ≤ 0.25 | Deep Causal Gate |
| **L1 — Datos** | Microstructure lag promedio | ≤ 150ms | Deep Causal Gate |
| **L1 — Operacional** | Accuracy Oracle (datos unseen) | ≥ 75% | Oracle v2 baseline |
| **L1 — Operacional** | Train-Test Delta | ≤ 10% | Lección Oracle v1 |
| **L2 — Causal** | **ΔCausal** | > 0 en 3 ciclos consecutivos | Métrica reina |
| **L2 — Causal** | `min_causal_accuracy` | ≥ 0.55 | Deep Causal Gate |
| **L2 — Causal** | `min_efficiency` | ≥ 0.40 | Deep Causal Gate |
| **L2 — Causal** | CATE por cluster | > 0 en ≥ 2 clusters | RiskBarrierLab |
| **L3 — Evolución** | Drift de features | < 20% mensual | MonitoringLab |
| **L3 — Evolución** | Proposal Quality | ≥ 60% con ΔCausal > 0 | ChangeProposer |
| **L4 — Sistema** | Rollback Rate | < 5% de cambios | CodeCraft |
| **L4 — Sistema** | Test Coverage v3 | ≥ 80% | CI/CD |
| **L4 — Biblioteca** | Component Reuse Rate | > 0% creciente | **Biblioteca Vectorial** |

### 4.4 El Ciclo de Validación Causal Completo

```
Propuesta (Lila genera o Ghost Architect detecta)
        ↓
ChangeProposer.parse() → TechnicalSpec validado
        ↓
RiskBarrierLab.calculate_cate() → ΔCausal estimado
        ↓
[Si ΔCausal < 0.75] → Rechazada → Vault de aprendizaje
[Si ΔCausal >= 0.75] → Continuar
        ↓
[Verificar: blind_test_ratio <= 0.25]
[Si ratio > 0.25] → Mejorar cobertura de microestructura primero
        ↓
CodeCraft Fases 1-6 → Código + Tests (Cobertura ≥ 80%)
        ↓
Biblioteca Vectorial: ¿Es un componente reutilizable? → Catalogar
        ↓
Paper Trading (mínimo 2 semanas con repeated gate pass)
        ↓
ΔCausal medido post-implementación (datos reales OOS)
        ↓
[Si ΔCausal_real >= ΔCausal_estimado × 0.80] → Merge aprobado
[Si ΔCausal_real < umbral] → Rollback + análisis de discrepancia
        ↓
bridge.jsonl actualizado (aprendizaje perpetuo)
```

### 4.5 El Oracle en Evolución Continua

El Oracle no es un modelo estático. Su ciclo de vida es:

```
Oracle v2 (baseline 83.33% acc.) ← Referencia histórica en vault
        ↓
Fase 1: Monitoring semanal (weekly_accuracy_tracker.py)
        ↓
Fase 2: CGAlpha.Labs.OracleAnalyst — análisis causal de errores
        ↓
Fase 3: Mejora de dataset (balance SMOTE, feature engineering)
        ↓
Fase 4: Ensemble (RandomForest + GradientBoosting + XGBoost + LightGBM)
        ↓
Fase 5: Producción v3 — validación OOS mínimo 2 semanas
        ↓
A/B test v2 vs v3 en paper trading → Si mejora ≥ 5%: switch
```

**Principio de Meta-Labeling (López de Prado):** El Oracle no predice la dirección del mercado; predice la **calidad de una señal ya detectada** por el sistema de Triple Coincidencia. Esta distinción arquitectónica es fundamental y debe preservarse en v3.

**Uso de probabilidades:** No solo predecir `1` o `0`. Usar `predict_proba()` y operar solo si la probabilidad de éxito es `> 0.70`.

---

## SECCIÓN 5: GLOSARIO DEL NORTE

*Versión expandida que incorpora términos de v2, Ghost Architect, y el sistema de datos.*

---

**ApiClient** (`data_processor/data_system/client.py`)  
Cliente HTTP genérico con `requests.Session`, manejo de reintentos y streaming en chunks de 8KB para descargas grandes. Base del sistema de adquisición de datos.

**ATR (Average True Range)**  
Medida de volatilidad. Unidad universal para barreras, stops y take-profits. Todo resultado normalizado en ATR permite comparabilidad entre regímenes.

**BinanceKlinesFetcher** (`data_processor/data_system/fetcher.py`)  
Especializado en adquisición desde Binance Vision. Flujo: construir URL → descargar ZIP con cache local → parsear CSV → DataFrame tipado → consolidar múltiples días cronológicamente.

**BLIND_TEST**  
Estado de un trade analizado sin match válido de microestructura disponible. Prohíbe alta confianza causal. Cuando `blind_test_ratio > 0.25`, el sistema entra en modo conservador y bloquea avance de fases.

**bridge.jsonl**  
El archivo más importante del legacy. Registro inmutable de cada trade con su Vector de Evidencia completo. Fuente primaria para el DML. Ahora incluye el campo `microstructure_mode` en v3.

**Builder**  
Uno de los dos pilares del sistema. Motor: Code Craft Sage (Fases 1–6). Función: cambiar y validar código. Su contraparte es el Observer.

**CATE (Conditional Average Treatment Effect)**  
Efecto causal de una decisión condicionado al régimen de mercado. Base del ΔCausal. `CATE > 0` en un cluster = decisión efectiva en ese régimen específico.

**CGA_Nexus**  
El Coordinador Supremo. Orquesta los 4 Labs, determina el régimen de mercado, sintetiza contexto para el LLM Inventor. En v3, Lila encarna esta función.

**CGA_Ops**  
Supervisor de recursos. Algoritmo determinista (NO IA) con semáforo Verde/Amarillo/Rojo basado en `psutil`.

**ChangeEvaluator**  
Evalúa la calidad de una propuesta en escala 0–1. Informado por el ΔCausal del RiskBarrierLab.

**ChangeProposer**  
Generador de propuestas. En v3, integra las 6 fases de CodeCraft. Umbral mínimo: `causal_score >= 0.75`.

**CodeCraft Sage**  
Motor de auto-modificación. Las 6 fases constituyen el pipeline completo Builder del sistema.

**Component Library (Biblioteca Vectorial)**  
El almacén organizado vectorialmente de todos los componentes reutilizables del sistema. Mantenida y mejorada continuamente por CodeCraft Sage. Ver Sección 6.

**Confounders (X)**  
Variables de contexto que afectan tanto la decisión como el resultado. Volatilidad, sesión, tendencia R², volumen relativo, hora del día.

**ContextSentinel**  
Memoria inmutable de decisiones. Registra parámetros activos y contexto de mercado en cada momento. Insumo para búsqueda de gemelos estadísticos.

**Cumulative Delta**  
Feature de microestructura de v2 que mide la diferencia acumulada entre volumen de compra y venta. Indica presión direccional del mercado. Alimenta al ExecutionOptimizerLab.

**DataRequestTemplateManager**  
Gestiona configuraciones de descarga en JSON. Permite agregar nuevas fuentes de datos sin modificar el core (patrón `__init_subclass__`).

**Deep Causal Gate**  
Conjunto de precondiciones binarias para avanzar a producción: `data_quality_pass`, `causal_quality_pass`, `proceed_v3`. Todos deben ser `True`.

**ΔCausal (Delta de Eficiencia Causal)**  
Métrica reina. `ΔCausal = Éxito_Total − Éxito_del_Mercado`. Mide el mérito real de la decisión.

**DML (Double Machine Learning)**  
Algoritmo de Microsoft Research (EconML). Separa el efecto de una decisión del efecto del contexto mediante limpieza de residuos en dos etapas. Motor del RiskBarrierLab.

**DuckDB**  
Motor OLAP local que reemplaza dependencias de cloud SQL. Inserción directa de DataFrames de Pandas sin mapeo manual de esquemas. Persistencia principal del data_processor en v2/v3.

**Fail Closed**  
Política de seguridad: ante ambigüedad, el sistema no ejecuta el cambio en lugar de ejecutar parcialmente. Estándar CodeCraft para ediciones inseguras.

**Fakeout**  
Ruptura temporal de un nivel con retorno rápido, frecuentemente impulsada por liquidez. El ZonePhysicsLab lo detecta como: ruptura rápida + retorno con volumen > ruptura = TRAMPA.

**Feature Branch**  
Rama Git donde CodeCraft implementa cada cambio. Nomenclatura: `feature/prop_{YYYYMMDD}_{id}_{descripción}`.

**Gate**  
Criterio duro que controla si el avance de fase es permitido. Debe pasar repetidamente (no solo una vez) antes de aprobar progresión.

**Ghost Architect** (`cgalpha/ghost_architect/simple_causal_analyzer.py`)  
El Observer del sistema. Opera en Fase 7+. Parsea logs históricos, construye snapshots, infiere hipótesis causales, evalúa propuestas arquitectónicas. Trabaja con fallback cuando la cobertura de datos es baja.

**Gemelos Estadísticos**  
Trades históricos con contexto casi idéntico al analizado pero con el parámetro anterior activo. Representan el contrafactual del DML.

**Heritage Vault (Legacy Vault)**  
Directorio `legacy_vault/` con el código completo de v1 y v2 como Biblioteca de Inspiración. No se usa directamente en producción sin pasar por el proceso de adaptación en mosaico.

**KeyCandleDetector**  
Detector de velas de absorción institucional (alto volumen + cuerpo pequeño). Parámetros validados: `volume_lookback=50`, `volume_percentile_threshold=80`, `ema_period=200`.

**Layer 0a (Principios Meta-Cognitivos)**  
Primera capa del sistema de conocimiento de v2. El LLM aprende principios antes de recomendar acciones. Corpus incluye: López de Prado (Meta-Labeling, Triple Barrier), DML, teoría de zonas de acumulación.

**Layer 0b (Papers de Trading)**  
Segunda capa del sistema de conocimiento de v2. Referencias académicas que informan al Observer. Incluye VWAP real-time, OBI Trigger, Cumulative Delta como features de microestructura.

**MAE (Max Adverse Excursion)**  
Peor caída intra-trade desde el punto de entrada. Mide calidad de entrada: buena entrada = MAE cercano a cero.

**Meta-Labeling (López de Prado)**  
El Oracle no predice dirección del mercado. Predice la calidad de una señal ya detectada por el sistema primario (Triple Coincidencia). Esta separación de responsabilidades es arquitectónicamente fundamental.

**MFE (Max Favorable Excursion)**  
Máximo potencial alcanzado antes de cerrar. Mide calibración de barreras de salida: `MFE >> resultado_real` = barreras demasiado conservadoras.

**Microstructure Mode**  
Estado de enriquecimiento de datos de un trade: `ENRICHED_EXACT` > `ENRICHED_NEAREST` > `LOCAL_ONLY` > `BLIND_TEST`. Determina la confianza máxima permitida en las inferencias causales.

**OBI (Order Book Imbalance) Trigger**  
Feature de microestructura de v2. Desequilibrio entre órdenes de compra y venta en el libro de órdenes. Señal de presión institucional inminente. Alimenta al ExecutionOptimizerLab.

**Observer**  
Uno de los dos pilares del sistema. Motor: Ghost Architect (Fase 7+). Función: analizar resultados y proponer dirección. Su contraparte es el Builder.

**OOS (Out-of-Sample)**  
Período de validación con datos nunca vistos durante el entrenamiento. La diferencia train-test debe ser ≤ 10% para aprobar cualquier modelo o cambio.

**Oracle**  
Validador de señales. No es un sistema de trading independiente. Decide si las condiciones de mercado favorecen que una señal detectada llegue a TP o fracase. Usa Meta-Labeling como principio de diseño.

**outcome_ordinal**  
Etiqueta de resultado en magnitud ATR discreta (0, 1, 2, 3+). Diseñada con la invariante crítica: **no hacer break al tocar el primer TP**.

**PolicyProposal**  
Output del RiskBarrierLab: regla condicional Python para qué parámetro usar en qué contexto. Incluye CATE estimado, cluster de mercado, confidence interval.

**PotentialCaptureEngine**  
Motor de etiquetado ordinal. Calcula barreras ATR y registra trayectoria completa (MFE, MAE, outcome_ordinal). Invariante más crítica: **nunca cerrar al primer TP**.

**SignalCombiner (Triple Coincidencia)**  
Fusiona AccumulationZone + Trend + KeyCandle. Tolerancia: 8 velas. R² mínimo: 0.45. Tasa histórica: ~0.037% de velas (39 señales en 12 meses BTCUSDT 5m 2024).

**task_buffer.py** (`cgalpha/nexus/`)  
Cola de tareas con fallback Redis/SQLite para continuidad del sistema bajo fallo parcial de infraestructura.

**TechnicalSpec**  
Objeto estructurado del Proposal Parser. Contrato entre la propuesta lingüística y la implementación técnica.

**TrendDetector (ZigZag R²)**  
Detector de tendencia con regresión lineal sobre puntos ZigZag. `zigzag_threshold=0.005` es **invariante crítica** (0.5 = bug, 100x más grueso).

**Vector de Evidencia**  
Tupla de alta fidelidad en `bridge.jsonl`: `{trade_id, config_snapshot, outcome_ordinal, mfe_atr, mae_atr, causal_tags, microstructure_mode}`.

**VWAP Real-time**  
Volume Weighted Average Price en tiempo real. Feature de microestructura de v2 que provee el precio justo del mercado ponderado por volumen. Contexto esencial para el ExecutionOptimizerLab.

**ZonePhysicsLab**  
Laboratorio de física del precio en 1 minuto. Calcula Penetration Depth (%), Volume Absorption, Time in Zone. Detecta Fakeouts. Estados: `REBOTE_CONFIRMADO`, `FAKEOUT_DETECTADO`, `RUPTURA_LIMPIA`, `ABSORCION_EN_CURSO`.

---

## SECCIÓN 6 [NUEVA]: BIBLIOTECA VECTORIAL DE COMPONENTES — EL ALMACÉN DE LEGOS

### 6.1 Concepto Fundacional: Del Vault Pasivo al Almacén Activo

La diferencia más profunda entre el Heritage Vault y la Biblioteca Vectorial de Componentes es esta:

> **El Vault guarda historia. La Biblioteca produce futuro.**

El Vault es un cementerio preservado (valioso para consulta). La Biblioteca Vectorial es un almacén vivo de piezas de precisión — LEGOs de alta especificación — que Lila combina para construir estrategias nuevas, que pueden ser similares a las existentes o radicalmente distintas.

**Esta biblioteca no puede ser diseñada de antemano en su totalidad.** Su organización vectorial emergirá de las correlaciones reales entre componentes, correlaciones que no son predecibles hasta que el sistema las descubra. Intentar pre-definir la taxonomía completa es un antipatrón. Lo que sí se puede definir es el **protocolo de catalogación** y la **infraestructura vectorial** que permitirá que la taxonomía emerja orgánicamente.

### 6.2 Arquitectura de la Biblioteca

```
cgalpha_v3/
└── component_library/
    ├── registry/
    │   ├── catalog.jsonl          # Índice de todos los componentes
    │   ├── embeddings.db          # Base vectorial (DuckDB + pgvector o FAISS)
    │   └── correlation_map.json   # Mapa de correlaciones descubiertas
    │
    ├── components/
    │   ├── signal/                # Componentes de detección de señales
    │   ├── entry/                 # Componentes de optimización de entrada
    │   ├── exit/                  # Componentes de gestión de salida
    │   ├── filtering/             # Componentes de filtrado causal
    │   ├── microstructure/        # Componentes de datos de microestructura
    │   ├── labeling/              # Componentes de etiquetado (barreras, ordinal)
    │   └── meta/                  # Componentes meta-cognitivos (principios)
    │
    ├── strategies/                # Estrategias completas construidas con componentes
    │   └── assembled/             # Combinaciones validadas de LEGOs
    │
    └── evolution_log/
        └── improvements.jsonl     # Registro de mejoras aplicadas por CodeCraft
```

### 6.3 El Registro de un Componente (Component Manifest)

Cada componente en la biblioteca tiene un manifiesto estructurado que captura su identidad técnica, causal y su genealogía:

```python
ComponentManifest(
    # Identidad
    component_id="uuid",
    name="TrendDetectorZigzagR2",
    version="1.0.0",
    category="signal",
    
    # Descripción funcional
    function="Mide calidad de tendencia mediante regresión lineal sobre puntos ZigZag",
    inputs=["ohlcv_df: pd.DataFrame", "lookback_period: int = 20"],
    outputs=["trend_direction: int", "trend_slope: float", "trend_r_squared: float"],
    
    # Parámetros con rangos validados
    parameters={
        "zigzag_threshold": {"value": 0.005, "range": (0.001, 0.05), "critical": True},
        "lookback_period": {"value": 20, "range": (5, 100), "critical": False}
    },
    
    # Genealogía
    heritage_source="legacy_vault/v1/trading_manager/trend_detector.py",
    heritage_adaptation="Parámetro zigzag_threshold corregido: 0.5→0.005 (3 Feb 2026)",
    
    # Validación causal
    causal_score=0.82,
    validated_regimes=["trending_bullish", "trending_bearish"],
    invalid_regimes=["low_volatility_range"],
    cate_by_regime={
        "trending_bullish": 0.91,
        "trending_bearish": 0.78,
        "low_volatility_range": -0.15
    },
    
    # Calidad técnica
    test_coverage=0.87,
    last_codecraft_improvement="2026-04-01",
    rollback_available=True,
    
    # Embedding vectorial (generado automáticamente)
    embedding_vector=[...],  # Vector de alta dimensión para búsqueda semántica
    
    # Correlaciones descubiertas
    correlated_with=[
        {"component_id": "SignalCombiner_v3", "correlation": 0.73, "type": "complementary"},
        {"component_id": "AccumulationZoneDetector_v3", "correlation": 0.68, "type": "prerequisite"}
    ]
)
```

### 6.4 Organización Vectorial: La Taxonomía que Emerge

La organización de la biblioteca no se pre-define jerárquicamente. Se organiza por **similitud semántica y causal** en un espacio vectorial de alta dimensión. Esto permite:

1. **Búsqueda por similitud:** "Encuentra componentes similares a TrendDetector que funcionen en regímenes de baja volatilidad"
2. **Descubrimiento de correlaciones:** El sistema detecta automáticamente qué componentes se potencian mutuamente
3. **Clustering emergente:** Los clusters de componentes correlacionados revelan patrones que no eran predecibles en el diseño inicial

**Implementación técnica:**

```python
class ComponentLibrary:
    """
    Almacén vectorial de componentes reutilizables.
    La organización emerge de las correlaciones; no se pre-define.
    """
    
    def __init__(self):
        self.db = duckdb.connect("component_library/registry/embeddings.db")
        self.embedder = SentenceTransformer(...)  # O embedding local vía Ollama
    
    def register(self, component: ComponentManifest) -> str:
        """Registra un componente y genera su embedding vectorial."""
        embedding = self.embedder.encode(
            f"{component.name} {component.function} "
            f"{component.inputs} {component.outputs} "
            f"{str(component.validated_regimes)}"
        )
        component.embedding_vector = embedding.tolist()
        self._save_to_db(component)
        self._update_correlation_map(component)
        return component.component_id
    
    def search(self, query: str, regime: str = None, top_k: int = 10) -> List[ComponentManifest]:
        """
        Búsqueda semántica por similitud vectorial.
        Si se especifica regime, filtra por cate_by_regime > 0.
        """
        query_embedding = self.embedder.encode(query)
        # Búsqueda por cosine similarity en DuckDB
        ...
    
    def discover_correlations(self) -> Dict:
        """
        Análisis periódico de correlaciones entre componentes.
        Actualiza correlation_map.json.
        La taxonomía emerge de este proceso, no de un diseño previo.
        """
        ...
    
    def get_compatible_combinations(self, component_id: str) -> List[Dict]:
        """
        Dado un componente, sugiere combinaciones válidas para construir estrategias.
        """
        ...
```

### 6.5 CodeCraft Sage como Curador de la Biblioteca

CodeCraft Sage tiene una responsabilidad adicional en v3: **mantener la biblioteca viva**. Cada vez que mejora un componente, debe:

1. **Actualizar el manifiesto** del componente con la nueva versión
2. **Recalcular el embedding** si la función o los parámetros cambiaron significativamente
3. **Preservar la versión anterior** como `{component_id}_v{N-1}` para rollback
4. **Registrar la mejora** en `evolution_log/improvements.jsonl`
5. **Re-evaluar correlaciones** con otros componentes afectados

```python
# En CodeCraft Saga Fase 4 (Git Automation) — extensión v3
def update_component_in_library(self, component_id: str, improved_code: str, causal_score: float):
    """
    Después de cada mejora aprobada, el componente mejorado
    reemplaza al anterior en la biblioteca.
    La versión anterior se preserva para rollback.
    """
    old_version = self.library.get(component_id)
    new_version = self._create_new_version(old_version, improved_code, causal_score)
    
    # Archivar versión anterior
    self.library.archive(old_version)
    
    # Registrar versión mejorada
    self.library.register(new_version)
    
    # Log de evolución
    self._log_improvement(old_version, new_version)
    
    # Notificar al Nexus: este componente mejoró
    self.nexus.notify_component_update(component_id)
```

### 6.6 El Vault como Semilla de la Biblioteca

La relación entre el Heritage Vault y la Biblioteca Vectorial es de **semilla a árbol**:

```
Heritage Vault (legacy_vault/)          Biblioteca Vectorial (component_library/)
─────────────────────────────     →     ─────────────────────────────────────────
Código tal como fue escrito              Componentes refactorizados, testeados, versionados
Organización histórica (v1/v2/)          Organización vectorial por similitud y correlación
Acceso por path de archivo               Acceso por búsqueda semántica o ID
Componentes acoplados al contexto        Componentes desacoplados y parametrizados
Sin métrica de calidad integrada         causal_score + test_coverage por componente
Mantenimiento manual                     Mantenimiento automático vía CodeCraft Sage
```

**Proceso de migración de Vault a Biblioteca:**

```python
# Protocolo para cada componente del vault
def migrate_vault_component_to_library(vault_path: str) -> ComponentManifest:
    """
    1. Leer componente del vault
    2. Identificar función, inputs, outputs (puede usar Ghost Architect)
    3. Refactorizar como componente desacoplado
    4. Escribir tests (Fase 3 CodeCraft)
    5. Calcular causal_score inicial (puede ser estimado si no hay datos reales)
    6. Generar embedding vectorial
    7. Registrar en la biblioteca
    """
    ...
```

### 6.7 Construir Estrategias con LEGOs

La razón de ser de la Biblioteca es que Lila pueda **ensamblar estrategias nuevas** combinando componentes existentes, sin necesidad de escribir código desde cero para cada nueva idea.

**Ejemplo: construir una estrategia de breakout usando LEGOs de la biblioteca**

```python
# Lila recibe: "Quiero probar una estrategia de breakout en alta volatilidad"

# Paso 1: Búsqueda semántica en la biblioteca
candidates = library.search(
    query="breakout detection high volatility",
    regime="high_volatility"
)
# → Resultado: [AccumulationZoneDetector, TrendDetector, KeyCandleDetector, VWAPFilter]

# Paso 2: Verificar compatibilidad y correlaciones
compatible = library.get_compatible_combinations("AccumulationZoneDetector_v3")
# → Confirma que TrendDetector y VWAPFilter son complementarios

# Paso 3: Ensamblar estrategia
strategy = StrategyAssembler.build(
    components=[
        "AccumulationZoneDetector_v3",
        "TrendDetector_v3",
        "VWAPFilter_v3",           # Nuevo: componente de microestructura de v2
        "TripleBarrierLabeler_v3"  # Reutilizado del PotentialCaptureEngine
    ],
    regime="high_volatility",
    causal_gate=True
)

# Paso 4: La estrategia resultante hereda los test_coverage y causal_scores
# de sus componentes → se puede estimar la calidad antes de backtest
strategy.estimated_causal_score = weighted_avg([c.causal_score for c in strategy.components])
```

**Nota arquitectónica crítica:** Las correlaciones entre componentes que hacen posible este ensamblaje **no son predecibles en el diseño inicial**. Emergen del uso real. Por eso la Biblioteca Vectorial debe mantenerse en aprendizaje continuo: cada nueva estrategia ensamblada, cada nuevo backtesting, actualiza el `correlation_map.json` y refina la organización vectorial.

### 6.8 Ciclo de Vida de la Biblioteca

```
Vault (fuente histórica)
        ↓ migrate_vault_component_to_library()
Biblioteca Vectorial v0 (componentes básicos)
        ↓ CodeCraft Sage mejora continuamente
Biblioteca Vectorial vN (componentes evolucionados)
        ↓ Ghost Architect descubre correlaciones
Mapa de Correlaciones actualizado
        ↓ Lila construye estrategias nuevas
Nuevas estrategias → generan más datos de performance
        ↓ ΔCausal mide qué componentes realmente aportan
Componentes con ΔCausal bajo → deprecados o reemplazados
Componentes con ΔCausal alto → promovidos y priorizados
```

### 6.9 Métricas de Salud de la Biblioteca

| Métrica | Descripción | Umbral Saludable |
|---|---|---|
| `library_size` | Total de componentes activos | Creciente |
| `component_reuse_rate` | % de estrategias que usan componentes existentes | > 60% |
| `avg_causal_score` | ΔCausal promedio de componentes activos | > 0.65 |
| `avg_test_coverage` | Cobertura de tests promedio | > 80% |
| `correlation_density` | Conexiones en el mapa de correlaciones | Densidad creciente |
| `deprecated_rate` | % de componentes deprecados por mes | < 10% |
| `vault_migration_progress` | % del vault migrado a la biblioteca | Progresivo |

---

## EPÍLOGO: LOS CUATRO PRINCIPIOS INVARIANTES DE LILA v3

*(Actualizado: se añade el Principio IV sobre la Biblioteca)*

**Principio I — Causalidad sobre Correlación:**  
Todo resultado debe pasar por el filtro del ΔCausal. Un trade ganador en mercado alcista no es evidencia de buena decisión. `blind_test_ratio > 0.25` = suspender inferencias causales hasta mejorar cobertura de microestructura.

**Principio II — Propuesta sobre Imposición:**  
Lila no actúa sin aprobación humana en cambios de producción. Builder propone; operador decide; CodeCraft implementa. La autonomía opera dentro de este triángulo.

**Principio III — Integridad sobre Velocidad:**  
La Triple Barrera de CodeCraft no es opcional. Reescritura total sin gates repetidos es un antipatrón. `Fail Closed` es la postura correcta. La velocidad es consecuencia de la sistematización, no un objetivo que comprometa la integridad.

**Principio IV — Componentes sobre Código Monolítico:**  
Todo componente que Lila crea o recicla debe refactorizarse como pieza reutilizable y catalogarse en la Biblioteca Vectorial. El conocimiento no debe quedar atrapado en el contexto para el que fue creado. La Biblioteca es la memoria activa del sistema; el Vault es la memoria histórica. Ambas son necesarias; ninguna reemplaza a la otra.

---

> *"El norte no es un lugar al que se llega. Es la dirección en la que uno se mantiene mientras construye."*

---

**FIN DEL BLUEPRINT CAUSAL v2.0 — LILA v3 NORTE MAESTRO**  
*Versión: 2.0.0 — Fecha de Síntesis: Abril 2026*  
*Fuentes canonizadas: UNIFIED_CONSTITUTION_v0.0.3 + CODECRAFT_PHASES_1-6 + SYSTEM_FLOW_COMPLETE + CGALPHA_V2_KNOWLEDGE_BASE + DATA_PROCESSOR_SYSTEM + ORACLE_CONSTRUCTION_GUIDE + CGALPHA_MASTER_DOCUMENTATION + CGALPHA_SYSTEM_GUIDE*
