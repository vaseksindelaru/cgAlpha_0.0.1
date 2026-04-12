# ADR adr-6f7441dd

- Fecha: 2026-04-12T09:49:52.234650+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-12_09-49`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-ba8edbce

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-ba8edbce",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
