# ADR adr-b7c28da9

- Fecha: 2026-04-11T20:27:28.260022+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-11_20-27_01`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-7a6a8e56

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-7a6a8e56",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
