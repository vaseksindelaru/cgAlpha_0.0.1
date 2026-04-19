# ADR adr-d3b3bdd5

- Fecha: 2026-04-19T11:27:40.590986+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-19_11-27`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-7c1d2254

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-7c1d2254",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
