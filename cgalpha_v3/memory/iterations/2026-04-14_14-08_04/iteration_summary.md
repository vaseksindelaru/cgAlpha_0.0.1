# Iteración: 2026-04-14_14-08_04 — FASE_0

## Objetivo
Registro automático de ciclo real GUI disparado por `learning_memory_promote`.

## Estado rápido

- Generado en: 2026-04-14T14:08:00.948853+00:00
- Último evento: LEARNING: memoria promovida 36adfa4b-d7c7-47a4-9b4f-7c52d669137e -> 4
- Kill-switch: armed
- Circuit breaker: inactive
- Data quality: valid

- Incidentes abiertos: 4
- ADR acumulados: 17

## Parámetros de riesgo vigentes

- max_drawdown_session_pct: 5.0
- max_position_size_pct: 2.0
- max_signals_per_hour: 10
- min_signal_quality_score: 0.65

## Eventos recientes GUI

| Timestamp UTC | Nivel | Evento |
|---|---|---|
| 2026-04-14T14:08:00.948723+00:00 | info | LEARNING: memoria promovida 36adfa4b-d7c7-47a4-9b4f-7c52d669137e -> 4 |
| 2026-04-14T14:08:00.942972+00:00 | info | LEARNING: memoria promovida 36adfa4b-d7c7-47a4-9b4f-7c52d669137e -> 3 |
| 2026-04-14T14:08:00.938787+00:00 | info | LEARNING: memoria ingestada 36adfa4b-d7c7-47a4-9b4f-7c52d669137e (math/0b) |
| 2026-04-14T14:08:00.870590+00:00 | critical | EXPERIMENT: temporal leakage detectado (Simulated leakage) |
| 2026-04-14T14:08:00.863865+00:00 | info | EXPERIMENT: propuesta generada prop-4fe3c06c |
| 2026-04-14T14:07:57.165487+00:00 | info | LILA: ingesta nueva [secondary] src-32082dff |
| 2026-04-14T14:07:57.159753+00:00 | info | LILA: ingesta nueva [primary] src-6e7173e1 |

## Riesgos identificados

- Sin riesgos críticos nuevos detectados en este ciclo GUI.

## Próximos pasos

1. Revisar CHECKLIST_IMPLEMENTACION para confirmar gate objetivo.
2. Continuar el siguiente ciclo desde GUI manteniendo trazabilidad automática.
