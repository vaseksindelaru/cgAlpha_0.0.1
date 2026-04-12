# ADR adr-d5dddfb4

- Fecha: 2026-04-12T01:29:54.497363+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-12_01-29`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-f6862e6c

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-f6862e6c",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
