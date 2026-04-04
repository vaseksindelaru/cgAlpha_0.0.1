# ADR adr-6901caa7

- Fecha: 2026-04-04T21:01:19.699722+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-04_21-01_06`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-e81214bf

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-e81214bf",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
