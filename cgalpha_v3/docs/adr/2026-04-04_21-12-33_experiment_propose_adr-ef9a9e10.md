# ADR adr-ef9a9e10

- Fecha: 2026-04-04T21:12:33.049051+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-04_21-12`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-9e792d55

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-9e792d55",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
