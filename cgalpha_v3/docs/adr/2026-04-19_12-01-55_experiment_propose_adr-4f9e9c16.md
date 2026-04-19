# ADR adr-4f9e9c16

- Fecha: 2026-04-19T12:01:55.457838+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-19_12-01`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-c9d51373

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-c9d51373",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
