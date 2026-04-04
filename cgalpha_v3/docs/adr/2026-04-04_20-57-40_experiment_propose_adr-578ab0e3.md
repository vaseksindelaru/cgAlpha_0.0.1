# ADR adr-578ab0e3

- Fecha: 2026-04-04T20:57:40.613528+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-04_20-57_02`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-16bc2756

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-16bc2756",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
