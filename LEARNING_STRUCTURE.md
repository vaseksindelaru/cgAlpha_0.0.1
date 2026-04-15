# ESTRUCTURA PROFESIONAL DE APRENDIZAJE: CGAlpha v3

## Visión General

```
┌────────────────────────────────────────────────────────────────────────┐
│                    SISTEMA DE APRENDIZAJE CONECTADO                      │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   ┌─────────────────┐          ┌─────────────────┐                  │
│   │    USUARIO      │◄────┬────►│     LILA        │                  │
│   │   (Aprendiz)    │     │     │  (Constructora) │                  │
│   └────────┬────────┘     │     └────────┬────────┘                  │
│            │              │              │                            │
│            │   PUENTE DE   │              │   APRENDIZAJE              │
│            │   COMPRENSIÓN │              │   AUTÓNOMO                │
│            │              │              │                            │
│            └──────────────┴──────────────┘                            │
│                         │                                              │
│                         ▼                                              │
│              ┌─────────────────────────┐                              │
│              │    LEARNING ORCHESTRATOR  │                              │
│              │    (Coordinador común)    │                              │
│              └─────────────────────────┘                              │
└────────────────────────────────────────────────────────────────────────┘
```

---

## PARTE 1: RUTA DE APRENDIZAJE DEL USUARIO

### 1.1 Materias Fundamentales

| Materia | Orientación | Recursos CGAlpha | Meta |
|---------|-------------|----------------|------|
| **Python** | Retroingeniería de CGAlpha | Código fuente en `cgalpha_v3/` | Comprender estructura, patrones, arquitectura |
| **Trading Algorítmico** | Microestructura + Señales | Documentación estratégica | Entender el motor de decisión |
| **Matemáticas Aplicadas** | DML + Causal Inference | Lopez de Prado + EconML | Comprender ΔCausal y validación |

### 1.2 Ruta Estructurada de Progresión

#### Fase 1: Fundamentos de Python (CGAlpha-centric)

```
SECUENCIA DE APRENDIZAJE:
[
  1.1] Python básico → estructuras de datos
  1.2] Patrones de diseño en Python
  1.3] Async/await y websockets (Binance)
  1.4] DuckDB y dataframes
  1.5] Type hints y Pydantic models
]

OBJETIVOS POR FASE:
- Fase 1.1: Poder leer y modificar archivos en `cgalpha_v3/infrastructure/`
- Fase 1.2: Entender Factory, Observer, Builder patterns
- Fase 1.3: Comprender BinanceVisionFetcher
- Fase 1.4: Manipular datos de trading
- Fase 1.5: Entender el sistema de tipos de CGAlpha
```

**Archivos clave para estudio:**

| Archivo | Propósito | Tema de aprendizaje |
|---------|-----------|-------------------|
| `infrastructure/binance_websocket_manager.py` | WS connection | Async Python |
| `domain/models/signal.py` | Modelos de señales | Pydantic + Types |
| `infrastructure/binance_data.py` | Fetch data | Data handling |
| `lila/llm/providers/base.py` | Proveedores LLM | Abstract base classes |

#### Fase 2: Trading Algorítmico

```
SECUENCIA DE APRENDIZAJE:
[
  2.1] Microestructura de mercado (VWAP, OBI, CumDelta)
  2.2] Triple Coincidence Strategy
  2.3] Zone Physics Monitor
  2.4] Oracle y Meta-Labeling
  2.5] Risk Management y barreras
]

OBJETIVOS POR FASE:
- Fase 2.1: Entender los 3 pilares de la Trinity
- Fase 2.2: Comprender detection de zonas
- Fase 2.3: Entender physics de re-test
- Fase 2.4: Comprender el rol del Oracle como filtro
- Fase 2.5: Entender protección de capital
```

**Archivos clave para estudio:**

| Archivo | Propósito | Tema de aprendizaje |
|---------|-----------|-------------------|
| `infrastructure/signal_detector/triple_coincidence.py` | Detección de señales | Estrategia core |
| `indicators/zone_monitors.py` | Monitoreo de zonas | Physics de precio |
| `scripts/phase1_oracle_training.py` | Entrenamiento Oracle | Meta-Labeling |
| `risk/risk_manager.py` | Gestión de riesgo | Barreras y exposure |

#### Fase 3: Matemáticas Aplicadas

```
SECUENCIA DE APRENDIZAJE:
[
  3.1] Causal Inference (DML) - Fundamentos
  3.2] Triple Barrier Method
  3.3] Meta-Labeling (López de Prado)
  3.4] Backtest Overfitting
  3.5] CATE Estimation
]

OBJETIVOS POR FASE:
- Fase 3.1: Entender causalidad en trading
- Fase 3.2: Comprender labeling de trades
- Fase 3.3: Entender filtrado probabilístico
- Fase 3.4: Evitar overfitting en backtests
- Fase 3.5: Medir efecto causal de decisiones
```

**Recursos mathematicales en CGAlpha:**

| Recurso | Contenido | Tema |
|---------|-----------|------|
| `legacy_vault/documentation/docs/CODECRAFT_PHASES_1_6_COMPANION.md` | CodeCraft fases | Metodología |
| `legacy_vault/bible/codecraft_sage/phase8_deep_causal_v03.md` | Causal inference | DML profundo |

---

## PARTE 2: RUTA DE APRENDIZAJE DE LILA

### 2.1 Principios de Aprendizaje Autonomo

Lila aprende de forma diferente al usuario. Su aprendizaje es:

1. **Por experimentación**: Ejecuta -> Analiza -> Propone -> Valida
2. **Por observación**: Analiza bridge.jsonl para detectar patrones
3. **Por propuesta**: AutoProposer genera ajustes paramétricos

### 2.2 Ciclo de Aprendizaje de Lila

```
                    ┌─────────────────────┐
                    │   OBSERVACIÓN       │
                    │   (Ghost Architect)│
                    └──────────┬──────────┘
                               │
                               ▼
┌─────────────────────┐  ┌──────────────┐  ┌─────────────────────┐
│  PROPUESTA          │◄─┤  ANÁLISIS    │◄─┤  RESULTADOS         │
│  (AutoProposer)    │  │  (Causal)    │  │  (bridge.jsonl)     │
└──────────┬──────────┘  └──────────────┘  └──────────┬──────────┘
           │                                            │
           ▼                                            ▼
┌─────────────────────┐                       ┌─────────────────────┐
│  VALIDACIÓN        │                       │  APRENDIZAJE         │
│  (CodeCraft)       │                       │  (Memory Policy)    │
└──────────┬──────���─��─┘                       └─────────────────────┘
           │
           ▼
┌─────────────────────┐
│  INTEGRACIÓN       │
│  (Nexus Gate)     │
└─────────────────────┘
```

### 2.3 Territorios de Exploración de Lila

| Territorio | Descripción | Estado en v3 |
|------------|-------------|--------------|
| **Simple Foundation Strategy** | Ensamblar 7 componentes | En construcción |
| **Oracle Evolution** | Mejorar accuracy del Oracle | Activo |
| **Parameter Tuning** | Ajuste paramétrico automático | Fase 6 |
| **Vault Purification** | Purga de Capa 1 | En proceso |

---

## PARTE 3: MECANISMO DE CONEXIÓN

### 3.1 El Puente de Comprensión

El usuario necesita entender (superficialmente) lo que Lila hace. Para esto:

**Nivel 1: Resumen Ejecutivo (siempre visible)**

- Dashboard muestra: fase actual de Lila, componentes activos, métricas clave
- No requiere conocimiento profundo

**Nivel 2: Contexto Técnico (bajo demanda)**

- El usuario puede pedir: "explícame este componente"
- Lila responde con explicación simplificada
- Referencia a archivos relevantes para estudio

**Nivel 3:Profundización (activo)**

- El usuario estudiar archivos referenciados
- Puede hacer preguntas específicas
- Propone caminos de aprendizaje opcionales

### 3.2 Interface de Consulta

```
CONSULTAS PERMITIDAS:

1. "¿En qué fase está Lila?"
   → Lila responde con estado actual y métricas

2. "¿Qué componente está analizando?"
   → Lila muestra componente + propósito + archivos relevantes

3. "¿Qué significa [concepto]?"
   → Lila da definición + ejemplo en CGAlpha + archivo referencia

4. "¿Puedes explicarme este archivo?"
   → Lila resume estructura + puntos clave + temas a estudiar

5. "¿Qué propone Lila ahora?"
   → Lila muestra propuesta actual + justificación causal

6. "¿Puedo proponer un camino alternativo?"
   → Sistema de propuestas (Parte 4)
```

### 3.3 Portal de Conexión

El usuario tiene acceso a:

```
┌──────────────────────────────────────────────────────────┐
│              PANEL DE CONEXIÓN USUARIO-LILA              │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ESTADO ACTUAL DE LILA                                    │
│  ───────────────────                                     │
│  Fase: Simple Foundation Strategy / Componente 5 de 7   │
│  Componente: OracleTrainer (Meta-Labeling)              │
│  Estado OOS: Semana 1/2 de validación                  │
│  ΔCausal estimado: 0.78                                 │
│                                                          │
│  ───────────────────────────────────────────────────────  │
│  ÚLTIMA PROPUESTA DE LILA                                │
│  ────────────────────────────────────                   │
│  Ajuste: volume_threshold 80 → 85                        │
│  Razón: Falsos positivos en sesión asiática             │
│  Causal Score: 0.78                                     │
│                                                          │
│  ───────────────────────────────────────────────────────  │
│  RESÚMENES DE APRENDIZAJE (últimos 7 días)              │
│  ────────────────────────────────────────────────────   │
│  [2026-04-12] Oracle aprendió: sesión asiática = baja    │
│              volumen institucional                        │
│  [2026-04-10] Detección mejorada: zone physics en       │
│              timeframe 1m                                │
│  [2026-04-08] Purga completada: oracle_v1.joblib       │
│                                                          │
│  ───────────────────────────────────────────────────────  │
│  ACCIONES DISPONIBLES                                    │
│  ──────────────────────                                   │
│  [Ver más detalles]  [Pedir explicación]              │
│  [Proponer camino alternativo]  [Estudio dirigido]   │
└──────────────────────────────────────────────────────────┘
```

---

## PARTE 4: PROTOCOLO DE PROPUESTAS OPCIONALES

### 4.1 Flujo de Propuesta

```
PROTOCOLO DE PROPUESTA:

1. USUARIO detecta oportunidad o necesidad
   │
   ▼
2. USUARIO formula propuesta
   │   Formato: {área, problema, solución propuesta, justificación}
   ▼
3. LILA evalúa la propuesta
   │   Criterios:
   │   - ¿Es técnicamente viable?
   │   - ¿Contraevidencias connues?
   │   - ¿Causal score estimado?
   ▼
4. LILA responde:
   │   a) ADOPTAR → integra en su pipeline
   │   b) RECHAZAR → explicación + justificación
   │   c) ADAPTAR → propone versión modificada
   ▼
5. Si ADOPTAR/ADAPTAR → validación OOS → integración
   Si RECHAZAR → registrado para aprendizaje futuro
```

### 4.2 Estructura de Propuesta

```
FORMATO DE PROPUESTA:

{
  "propuesta_id": "prop_YYYYMMDD_HHMMSS",
  "autor": "usuario",
  "timestamp": "ISO 8601",
  
  "área": {
    "módulo": "oracle|signal|risk|storage|...",
    "componente": "nombre",
    "parámetro": "nombre (si aplica)"
  },
  
  "problema": {
    "descripción": "Qué está mal o falta",
    "evidencia": "Datos o observación",
    "impacto": "Alcance del problema"
  },
  
  "solución": {
    "descripción": "Qué propone",
    "implementación": "Cómo funcionaría",
    "alternativas": "Opciones consideradas"
  },
  
  "justificación": {
    "razón": "Por qué esto solucionaría el problema",
    "evidencia": "Referencias a código/documentación",
    "curso_de_aprendizaje": "Ruta sugerida para el usuario"
  }
}

RESPUESTA DE LILA:

{
  "propuesta_id": "ref a la propuesta",
  "respuesta": "ADOPTAR|RECHAZAR|ADAPTAR",
  
  "adoptar": {
    "integración": "Cómo se integra",
    "validación": "Plan de validación OOS"
  },
  
  "rechazar": {
    "razón": "Por qué no viable",
    "contraevidencia": "Por qué no funciona",
    "nota": "Consideración para futuro"
  },
  
  "adaptar": {
    "cambios": "Qué se modifica",
    "justificación": "Por qué adaptación",
    "versión_propuesta": "Nueva versión"
  }
}
```

### 4.3 Ejemplo de Propuesta

```
EJEMPLO:

USUARIO propone:
{
  "propuesta_id": "prop_20260412_143000",
  "área": {
    "módulo": "oracle",
    "componente": "OracleTrainer"
  },
  "problema": {
    "descripción": "El Oracle falla en sesiones de baja liquidez",
    "evidencia": "Hit-rate cae 15% en sesión asiática",
    "impacto": "Señales falsas en horas fuera de mercado US"
  },
  "solución": {
    "descripción": "Añadir признак de sesión al feature set",
    "implementación": "session_hour como feature ordinal"
  },
  "justificación": {
    "razón": "El Oracle no tiene información de sesión",
    "evidencia": "oracle.py no recibe timestamp como feature",
    "curso_de_aprendizaje": "Estudiar phase1_oracle_training.py + añadir session features"
  }
}

LILA responde:
{
  "propuesta_id": "prop_20260412_143000",
  "respuesta": "ADOPTAR",
  "adoptar": {
    "integración": "Añadir session_hour a Phase1OracleTraining._build_features()",
    "validación": "OOS 2 semanas con datos de sesión"
  }
}

--- OBIEN ---

LILA responde:
{
  "propuesta_id": "prop_20260412_143000",
  "respuesta": "RECHAZAR",
  "rechazar": {
    "razón": "El Oracle ya recibe timestamp como feature",
    "contraevidencia": "Ver phase1_oracle_training.py línea 87: y['timestamp'] = df['close_time']",
    "nota": "Possibly el problema es cómo se usa la información de sesión"
  }
}
```

---

## PARTE 5: LEARNING ORCHESTRATOR

### 5.1 Responsabilidades del Orchestrator

El Learning Orchestrator coordina todo el sistema:

```
RESPONSABILIDADES:

1. RASTREO DE PROGRESO
   - Usuario: qué fase/materia ha completado
   - Lila: qué territorio ha explorado
   
2. SINCRONIZACIÓN DE CONTEXTO
   - Cuando usuario pregunta, asegura contexto relevante
   - Cuando Lila propone, notifica al usuario
   
3. GESTIÓN DE PROPUESTAS
   - Recibe propuestas del usuario
   - Las canaliza a Lila
   - Registra respuestas
   
4. GENERACIÓN DE RESÚMENES
   - Diario: resumen de actividad
   - Semanal: progreso de ambos
   - Mensual: evaluación de efectividad
```

### 5.2 Archivo de Estado de Learning

```
LEARNING_STATE_FILE = "aipha_memory/learning_state.jsonl"

Schema:
{
  "timestamp": "ISO 8601",
  "entidad": "usuario|lila|orchestrator",
  "evento": {
    "tipo": "consulta|propuesta|respuesta|progress|exploración",
    "materia": "python|trading|math|lila_territory",
    "detalle": "string"
  },
  "estado": "completado|en_progreso|bloqueado|propuesta_pendiente",
  "referencias": ["archivos relacionados"]
}
```

### 5.3 Comandos de Learning

```
COMANDOS DISPONIBLES:

# Estado
learning status                    # Ver progreso general
learning status usuario             # Ver mi progreso
learning status lila              # Ver progreso de Lila

# Progreso
learning advance <materia>       # Avanzar a siguiente fase
learning study <archivo>          # Estudiar archivo específico
learning checkpoint <nota>         # Guardar checkpoint

# Conexión
learning ask <pregunta>            # Hacer pregunta a Lila
learning explain <concepto>        # Pedir explicación
learning show-lila-phase         # Ver fase actual de Lila

# Propuestas
learning propose <json>           # Hacer propuesta
learning proposals                # Ver mis propuestas
learning proposal <id> status     # Ver estado de propuesta

# Resúmenes
learning summary                  # Resumen diario
learning summary --weekly        # Resumen semanal
-learning summary --monthly      # Resumen mensual
```

---

## PARTE 6: EVALUACIÓN Y MEJORA CONTINUA

### 6.1 Métricas de Efectividad

```
MÉTRICAS DEL SISTEMA:

1. PARA EL USUARIO:
   - Temas completados por semana
   - Archivos estudiados
   - Consultas feitas
   - Propuestas feitas
   - Tasa de adopción de propuestas
   
2. PARA LILA:
   - Componentes completados
   - Propuestas propias
   - Propuestas del usuario adoptadas
   - ΔCausal mejoras
   
3. PARA EL SISTEMA:
   - Tasa de comprensión (preguntas respondidas)
   - Tasa de propuesta aceptada
   - Tiempo de respuesta a propuestas
   - Coherencia entre rutas
```

### 6.2 Revisión Periódica

```
REVISIÓN SEMANAL:

1. Revisar progreso del usuario
2. Revisar actividad de Lila
3. Evaluar propuestas pendientes
4. Ajustar rutas si necesario

REVISIÓN MENSUAL:

1. Evaluación de efectividad del sistema
2. Ajustes de estructura
3. Documentación de aprendizajes
4. Plan de siguiente mes
```

---

## ANEXO: ÍNDICE DE MATERIALES POR MATERIA

### Python

| Archivo | Tema | Nivel |
|---------|------|-------|
| `infrastructure/binance_websocket_manager.py` | Async/WS | Básico-Intermedio |
| `domain/models/signal.py` | Pydantic | Básico |
| `lila/llm/providers/base.py` | Abstract Classes | Intermedio |
| `application/pipeline.py` | Pipeline Pattern | Intermedio |
| `data_quality/gates.py` | Gate Pattern | Intermedio |

### Trading Algorítmico

| Archivo | Tema | Nivel |
|---------|------|-------|
| `infrastructure/signal_detector/triple_coincidence.py` | Triple Coincidencia | Intermedio |
| `indicators/zone_monitors.py` | Zone Physics | Intermedio |
| `risk/risk_manager.py` | Risk Barriers | Intermedio-Avanzado |
| `scripts/phase1_oracle_training.py` | Oracle Training | Avanzado |
| `infrastructure/signal_detector/triple_coincidence.py` | Microestructura | Intermedio |

### Matemáticas

| Archivo | Tema | Nivel |
|---------|------|-------|
| `legacy_vault/documentation/docs/promotion_criteria.md` | Causal Metrics | Intermedio |
| `legacy_vault/documentation/docs/CODECRAFT_PHASES_1_6_COMPANION.md` | Metodología | Intermedio |
| `legacy_vault/bible/codecraft_sage/phase8_deep_causal_v03.md` | DML | Avanzado |
| Post-mortems en `docs/post_mortems/` | Casos reales | Intermediate-Advanced |