# ADR adr-0c3cc0ce

- Fecha: 2026-04-11T20:27:27.334621+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-11_20-27`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-78bf2da5

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-78bf2da5",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
