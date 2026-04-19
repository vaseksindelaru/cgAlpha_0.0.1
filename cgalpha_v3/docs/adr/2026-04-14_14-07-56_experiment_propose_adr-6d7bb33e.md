# ADR adr-6d7bb33e

- Fecha: 2026-04-14T14:07:56.907269+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-14_14-07`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-a6beff0f

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-a6beff0f",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
