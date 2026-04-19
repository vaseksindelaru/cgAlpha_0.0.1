# ADR adr-8c4e47f8

- Fecha: 2026-04-14T14:03:16.760960+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-14_14-03_01`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-cfb57fec

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-cfb57fec",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
