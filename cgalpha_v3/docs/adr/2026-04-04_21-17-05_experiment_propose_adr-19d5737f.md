# ADR adr-19d5737f

- Fecha: 2026-04-04T21:17:05.438407+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-04_21-17`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-5e2a208d

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-5e2a208d",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
