# ADR adr-aacb7044

- Fecha: 2026-04-04T21:19:43.259186+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-04_21-19`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-bb39ed1b

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-bb39ed1b",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
