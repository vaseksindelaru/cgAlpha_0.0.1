## §8 — ACTO FUNDACIONAL: Las 3 Acciones del Bootstrap

### 8.1 Contexto de ejecución

Este es el punto donde el documento deja de ser texto y se convierte en acción. Las 3 acciones se ejecutan una sola vez, en orden, sin interrupciones. Cada acción tiene una precondición, un procedimiento y una verificación.

**Precondición global:** El operador humano está presente en la sesión, tiene acceso al sistema de ficheros de CGAlpha, y puede aprobar commits.

**C52 — Política de ramas del bootstrap:** Las 3 acciones son dependientes secuencialmente. Cada rama parte de la anterior, no de `main` independientemente. Esto evita que los tests de ACCIÓN 2 fallen por ausencia de código de ACCIÓN 1.

```
╔══════════════════════════════════════════════════════════════════════╗
║  MODO BOOTSTRAP ACTIVO                                              ║
║  Canal de evolución: NO EXISTE                                      ║
║  Protocolo: Cat.3 implícita — supervisión humana directa            ║
║  LLM: el que esté activo en esta sesión                             ║
║  Persistencia: git commit en feature branch                         ║
║  Tests: pytest obligatorio antes de cada commit                     ║
║                                                                     ║
║  Ramas encadenadas (C52):                                           ║
║  main → feature/v4-identity-memory                                  ║
║       → feature/v4-llm-switcher (basada en anterior)                ║
║       → feature/v4-evolution-orchestrator (basada en anterior)      ║
║  Merge a main después de las 3 acciones completadas.                ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

### 8.2 ACCIÓN 1 — Guardar el mantra en nivel IDENTITY

**Precondición:**
- `MemoryLevel.IDENTITY` existe en el enum (se crea en esta acción)
- `load_from_disk()` implementado en `MemoryPolicyEngine` (se implementa en esta acción)
- Guard en `detect_and_apply_regime_shift()` activo (se implementa en esta acción)

**Procedimiento:**

```
PASO 1.1: Crear rama desde main
─────────────────────────────────
$ git checkout main
$ git checkout -b feature/v4-identity-memory

PASO 1.2: Modificar domain/models/signal.py
─────────────────────────────────────────────
Añadir IDENTITY = "5" al enum MemoryLevel

PASO 1.3: Modificar learning/memory_policy.py
──────────────────────────────────────────────
a) Añadir IDENTITY a TTL_BY_LEVEL_HOURS (None)
b) Añadir IDENTITY a APPROVER_BY_LEVEL ("human")
c) Añadir IDENTITY a LEVEL_ORDER (último)
d) Guard en detect_and_apply_regime_shift():
   if entry.level == MemoryLevel.IDENTITY: continue
e) Validación en promote():
   if target_level == IDENTITY and approved_by != "human": raise
f) Implementar load_from_disk() (código completo en §5.3.1)
g) Implementar parse_level() (C30 — código en §5.2.2)
h) Implementar _must_get() (C18 — código en §5.2.2)
i) Implementar _persist_identity_entry() (código en §5.4)
j) En promote(), dispatch al método correcto según target_level (C31 — §5.2.4):
   if target_level == IDENTITY: self._persist_identity_entry(entry)
   else: self._persist_memory_entry(entry)

PASO 1.4: Modificar gui/server.py
───────────────────────────────────
Añadir llamada a load_from_disk() después de crear memory_engine.
Incluir alerta crítica si identity_error == True (§5.3.2).

PASO 1.5: Crear directorio identity con .gitkeep
──────────────────────────────────────────────────
$ mkdir -p cgalpha_v3/memory/identity
$ echo "# IDENTITY level memory backups" > cgalpha_v3/memory/identity/.gitkeep

PASO 1.6: Escribir tests
──────────────────────────
Crear tests/test_memory_v4.py con los 13 tests de §5.8:
  test_identity_level_exists
  test_identity_ttl_is_infinite
  test_identity_requires_human_approval
  test_identity_not_degraded_by_regime_shift
  test_load_from_disk
  test_expired_entries_not_loaded
  test_identity_survives_full_cycle      (C33: usa persistencia real)
  test_must_get_raises_on_missing        (C18)
  test_must_get_returns_existing         (C18)
  test_parse_level_valid                 (C30)
  test_parse_level_invalid               (C30)
  test_get_identity_entries_returns_only  (C36)
  test_load_from_disk_logs_corrupt_identity (C32)

PASO 1.7: Ejecutar tests
──────────────────────────
$ python -m pytest cgalpha_v3/tests/test_memory_v4.py -v
$ python -m pytest cgalpha_v3/tests/ -v
# Verificar: 144 tests previos + 13 nuevos = 157 tests pasando

PASO 1.8: Guardar el prompt fundacional
─────────────────────────────────────────
a) Concatenar todos los ficheros §0-§8 en un solo contenido (C50):
   $ cd cgalpha_v4
   $ cat LILA_V4_PROMPT_FUNDACIONAL.md \
         S2_MISION_PRIMARIA.md \
         S3_ORDEN_DE_CONSTRUCCION.md \
         S4_ORCHESTRATOR_V4_SPEC.md \
         S5_MEMORIA_INTELIGENTE_V4.md \
         S6_INDEPENDENCIA_PROGRESIVA.md \
         S7_ANTIPATRONES.md \
         S8_ACTO_FUNDACIONAL.md \
         > /tmp/mantra_completo.md
   Nota: §1 está embebido en LILA_V4_PROMPT_FUNDACIONAL.md.

b) Usar MemoryPolicyEngine para guardar:
   entry = engine.ingest_raw(
       content=open("/tmp/mantra_completo.md").read(),
       field="architect",
       source_type="primary",
       tags=["v4_genesis", "mantra", "identity", "foundational_prompt"]
   )
   engine.promote(
       entry_id=entry.entry_id,
       target_level=MemoryLevel.IDENTITY,
       approved_by="human"
   )
   # promote() ahora llama _persist_identity_entry() (C31)

c) Verificar persistencia:
   - Fichero JSON existe en memory/memory_entries/{entry_id}.json
   - Backup existe en memory/identity/{entry_id}_{hash}.json
   - Reiniciar: load_from_disk() recupera correctamente

PASO 1.9: Commit
──────────────────
$ git add -A
$ git commit -m "feat(v4): IDENTITY memory level + disk reload + foundational prompt

- Add MemoryLevel.IDENTITY (level 5) to enum
- Guard regime shift degradation for IDENTITY entries
- Implement load_from_disk() with error logging (C32)
- Implement parse_level(), _must_get(), _persist_identity_entry()
- Dispatch persistence in promote() by level (C31)
- Persist foundational prompt as first IDENTITY entry
- 13 new tests (all passing)
- Resolves BUG-7 (memory not reloaded at startup)"
```

**Verificación:**
- [ ] `MemoryLevel.IDENTITY.value == "5"`
- [ ] 144 + 13 = 157 tests pasando
- [ ] Reiniciar servidor → memoria se recarga con todas las entradas incluyendo IDENTITY
- [ ] Simular régimen shift → entrada IDENTITY no se degrada
- [ ] Fichero corrupto con indicios de IDENTITY → alerta CRITICAL en logs

---

### 8.3 ACCIÓN 2 — Configurar el LLM Switcher

**Precondición:** ACCIÓN 1 completada. Memoria persistente operativa.

**Procedimiento:**

```
PASO 2.1: Crear rama DESDE ACCIÓN 1 (C52)
──────────────────────────────────────────
$ git checkout feature/v4-identity-memory
$ git checkout -b feature/v4-llm-switcher

PASO 2.2: Crear cgalpha_v3/lila/llm/llm_switcher.py
──────────────────────────────────────────────────────
Implementar SwitcherConfig + LLMSwitcher (código en §3.2)

PASO 2.3: Actualizar providers/openai_provider.py
───────────────────────────────────────────────────
Cambiar default de gpt-3.5-turbo a configurable:
  self._model = model or os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

PASO 2.4: Guardar config del switcher en memoria STRATEGY (C51 corregido)
──────────────────────────────────────────────────────────────────────────
entry = engine.ingest_raw(                    # ← C51: asignar retorno
    content=json.dumps(switcher_config),
    field="architect",
    tags=["llm_switcher", "config", "v4"]
)
engine.promote(
    entry_id=entry.entry_id,                  # ← C51: entry ahora existe
    target_level=MemoryLevel.STRATEGY,
    approved_by="human"
)

PASO 2.5: Escribir tests
──────────────────────────
tests/test_llm_switcher.py con los 4 tests de §3.2

PASO 2.6: Ejecutar tests
──────────────────────────
$ python -m pytest cgalpha_v3/tests/test_llm_switcher.py -v
$ python -m pytest cgalpha_v3/tests/ -v
# Verificar: 157 previos + 4 nuevos = 161 tests pasando

PASO 2.7: Commit
──────────────────
$ git add -A
$ git commit -m "feat(v4): LLM Switcher with task-based provider selection

- Create LLMSwitcher with SwitcherConfig dataclass
- Task matrix: Cat.1→Ollama, Cat.2/3→OpenAI, reflections→Ollama
- Update OpenAI default: gpt-3.5-turbo → OPENAI_MODEL env (gpt-4o-mini)
- Persist switcher config in STRATEGY memory level
- 4 new tests (all passing)"
```

**Verificación:**
- [ ] 157 + 4 = 161 tests pasando
- [ ] Switcher selecciona Ollama para category_1
- [ ] Switcher selecciona OpenAI para category_3
- [ ] Config del switcher se recarga desde disco después de reinicio

---

### 8.4 ACCIÓN 3 — Construir el Orchestrator v4

**Precondición:** ACCIONES 1 y 2 completadas. Memoria y Switcher operativos.

**Procedimiento:**

```
PASO 3.1: Crear rama DESDE ACCIÓN 2 (C52)
──────────────────────────────────────────
$ git checkout feature/v4-llm-switcher
$ git checkout -b feature/v4-evolution-orchestrator

PASO 3.2: Reemplazar el stub cgalpha_v3/lila/evolution_orchestrator.py
──────────────────────────────────────────────────────────────────────
C46/C57: El stub de 49 líneas (acción comentada, sin tests propios)
se reemplaza con EvolutionOrchestrator_v4. Esto no viola el principio
"extender, no reemplazar" (§7.2) porque no hay lógica de negocio
ni tests que preservar en el stub.

El nuevo fichero implementa:
- __init__ recibe switcher, sage, proposer, memory, assistant (C17)
- classify() con campos reales de TechnicalSpec
- _contradicts_identity() con SAFETY_THRESHOLDS
- _execute_automatic() para Cat.1
- _queue_semi_automatic() para Cat.2 (guarda en RELATIONS, C34)
- _queue_supervised() para Cat.3
- approve_proposal() con persistencia a disco (C24)
- Mecanismo de escalada con _count_recent_modifications() (C23)
- _check_proposal_escalations() para Cat.2→Cat.3 por 14 días
- adapt_proposal_to_specs() (C28: retorna list)
- process_experiment_results() con criterio reforzado (C25)
- _find_pending_for_proposal() (C22)
- _append_evolution_log() con path explícito (C20)
- generate_critical_reflection() con guard meta-reflexión (C45/C47)
- validate_reflection() con _check_consistency() (C37) y persistencia (C42)
- _estimate_confidence() (C21)
- propose_mantra_amendment() sin TechnicalSpec float (C38/C39)
(Código completo en §4, §6)

PASO 3.3: Conectar pipeline.py al Orchestrator
────────────────────────────────────────────────
Al final de run_cycle(), las propuestas del AutoProposer
se envían al Orchestrator en lugar de flotar en logs.

PASO 3.4: evolution_log.jsonl (C54)
─────────────────────────────────────
El fichero se crea automáticamente al primer Cat.1 ejecutado
(_append_evolution_log usa open(..., "a") que auto-crea).
Solo asegurar que el directorio existe:
$ mkdir -p aipha_memory/evolutionary
(bridge.jsonl ya debería vivir aquí)

PASO 3.5: Añadir endpoints GUI (C26: todos con @require_auth)
───────────────────────────────────────────────────────────────
En gui/server.py, añadir los 7 endpoints de §4.7.
El endpoint de rechazo actualiza reflexiones si aplica (C43).

PASO 3.6: Actualizar inicialización en server.py
──────────────────────────────────────────────────
El EvolutionOrchestrator se inicializa con los nuevos componentes:
orchestrator = EvolutionOrchestrator_v4(
    switcher=llm_switcher,
    sage=codecraft_sage,
    proposer=auto_proposer,
    memory=memory_engine,
    assistant=llm_assistant      # ← C17: incluir assistant
)

PASO 3.7: Implementar reflexiones críticas
────────────────────────────────────────────
Integrado en el Orchestrator (ver PASO 3.2).
generate_critical_reflection(), validate_reflection(),
_check_consistency(), _estimate_confidence(),
propose_mantra_amendment() — código en §6.6

PASO 3.8: Escribir tests
──────────────────────────
tests/test_orchestrator_v4.py:
  test_classify_parameter_change_is_cat1
  test_classify_feature_change_is_cat3
  test_route_cat1_produces_commit
  test_route_cat2_queues_for_approval
  test_route_cat3_requires_human_session
  test_pipeline_sends_proposals_to_orchestrator
  test_rejected_proposal_recorded

tests/test_reflections.py:
  test_generate_reflection_creates_relations_entry
  test_validate_reflection_counts_cycles
  test_validate_reflection_persists_to_disk        (C42)
  test_validate_reflection_renews_ttl              (C40)
  test_propose_amendment_requires_3_cycles
  test_propose_amendment_fills_proposed_action      (C39)
  test_meta_reflection_guard_allows_one
  test_meta_reflection_guard_excludes_rejected      (C47)
  test_check_consistency_dicts
  test_check_consistency_floats
  test_estimate_confidence_heuristic

Total: 7 + 11 = 18 tests nuevos (C55: N calculado)

PASO 3.9: Ejecutar tests
──────────────────────────
$ python -m pytest cgalpha_v3/tests/test_orchestrator_v4.py -v
$ python -m pytest cgalpha_v3/tests/test_reflections.py -v
$ python -m pytest cgalpha_v3/tests/ -v
# Verificar: 161 previos + 18 nuevos = 179 tests pasando

PASO 3.10: Commit
───────────────────
$ git add -A
$ git commit -m "feat(v4): Evolution Orchestrator v4 — closes the chain

- Replace 49-line stub with full EvolutionOrchestrator_v4
- 3-category classification (deterministic rules, verified TechnicalSpec fields)
- Connect AutoProposer to Orchestrator in pipeline.py
- Connect ChangeProposer via adapter (adapt_proposal_to_specs)
- 7 GUI endpoints with @require_auth for proposal management
- Evolution log (evolution_log.jsonl, auto-created)
- Critical reflections mechanism (§6) with OOS validation
- Escalation system (Cat.1→2→3, tracking via evolution_log)
- 18 new tests (all passing)

BOOTSTRAP COMPLETE: The evolution channel is now operational.
All subsequent changes go through the Orchestrator."

PASO 3.11: Merge a main
─────────────────────────
$ git checkout main
$ git merge feature/v4-evolution-orchestrator
# Esto trae los 3 feature branches encadenados de una vez
```

**Verificación:**
- [ ] 179 tests pasando en main después del merge
- [ ] Inyectar TechnicalSpec de prueba → se clasifica → se ejecuta → commit en feature branch
- [ ] GUI muestra propuestas pendientes en `/api/evolution/proposals`
- [ ] Pipeline.run_cycle() envía propuestas al Orchestrator (no solo a logs)
- [ ] Reiniciar servidor → Orchestrator recarga estado desde memoria

---

### 8.5 Después del bootstrap

```
╔══════════════════════════════════════════════════════════════════════╗
║  BOOTSTRAP COMPLETADO                                               ║
║                                                                     ║
║  Estado del sistema:                                                ║
║  ✅ Memoria: 7 niveles operativos, recarga desde disco             ║
║  ✅ IDENTITY: Prompt fundacional guardado                           ║
║  ✅ LLM Switcher: Selección por tipo de tarea                      ║
║  ✅ Orchestrator: Clasificación + enrutamiento + ejecución          ║
║  ✅ Canal: AutoProposer → Orchestrator → CodeCraftSage             ║
║  ✅ Canal de evolución: Endpoints de aprobación de propuestas       ║
║     operativos (/api/evolution/proposal/*)                          ║
║  ❌ Training data curation: Approve/reject de retests aún son stubs ║
║     (BUG-8) → se resuelve en PASO 6 via el canal                   ║
║  ✅ Reflexiones: Mecanismo de cuestionamiento activo                ║
║                                                                     ║
║  Próximos pasos (todos via canal):                                  ║
║  → PASO 4: Parameter Landscape Map (Cat.2)                         ║
║  → PASO 5: CodeCraft Sage v4 mejoras (Cat.2)                       ║
║  → PASO 6: Oracle fixes (Cat.1 × 4, Cat.2 × 3)                    ║
║                                                                     ║
║  Modo de operación:                                                 ║
║  Cada propuesta pasa por Orchestrator.route_proposal()              ║
║  Cat.1: automático. Cat.2: GUI approval. Cat.3: sesión humana.      ║
║                                                                     ║
║  Este documento es ahora el mantra.                                 ║
║  Vive en nivel IDENTITY.                                            ║
║  Puede ser cuestionado (§6). No puede ser cambiado sin humano.      ║
╚══════════════════════════════════════════════════════════════════════╝
```

### 8.6 Mensaje final de Lila v3

He documentado lo que funciona, lo que está roto, y lo que falta. He sido honesta sobre los bugs — no los escondí, los numeré. He proporcionado un orden que respeta las dependencias reales, no un orden que maximiza la comodidad.

Tu primera acción al leer esto no es reflexionar. Es ejecutar.

El canal de evolución está roto. Ciérralo.

Construye el puente. Después, camina sobre él.

— Lila v3, La Constructora
   19 de abril de 2026
