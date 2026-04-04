# ADR adr-7838a66d

- Fecha: 2026-04-04T21:01:35.953081+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-04_21-01`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-2a5a4272

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-2a5a4272",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
