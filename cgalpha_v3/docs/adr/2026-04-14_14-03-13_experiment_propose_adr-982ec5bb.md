# ADR adr-982ec5bb

- Fecha: 2026-04-14T14:03:13.212602+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-14_14-03`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-7fe3c987

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-7fe3c987",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
