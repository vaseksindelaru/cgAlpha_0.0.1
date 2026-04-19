# ADR adr-c82a56b1

- Fecha: 2026-04-14T14:08:00.867770+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-14_14-08`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-4fe3c06c

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-4fe3c06c",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
