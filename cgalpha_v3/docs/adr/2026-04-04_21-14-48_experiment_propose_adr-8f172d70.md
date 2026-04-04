# ADR adr-8f172d70

- Fecha: 2026-04-04T21:14:48.994107+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-04_21-14`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-b53cdbb9

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-b53cdbb9",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
