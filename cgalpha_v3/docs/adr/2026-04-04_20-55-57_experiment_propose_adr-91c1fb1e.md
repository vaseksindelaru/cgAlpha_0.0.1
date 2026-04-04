# ADR adr-91c1fb1e

- Fecha: 2026-04-04T20:55:57.154739+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-04_20-55`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-e5e7aaa0

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-e5e7aaa0",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
