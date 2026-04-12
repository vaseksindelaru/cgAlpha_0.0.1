# ADR adr-2914f9d4

- Fecha: 2026-04-12T09:50:48.717745+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-12_09-50`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-94d3e8b6

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-94d3e8b6",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
