# ADR adr-ae32f4a4

- Fecha: 2026-04-04T21:01:10.610043+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-04_21-01_03`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-fded6fe1

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-fded6fe1",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
