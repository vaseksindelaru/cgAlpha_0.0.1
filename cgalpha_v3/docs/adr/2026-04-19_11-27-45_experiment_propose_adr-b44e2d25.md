# ADR adr-b44e2d25

- Fecha: 2026-04-19T11:27:45.477768+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-19_11-27_01`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-cf7bc8bb

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-cf7bc8bb",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
