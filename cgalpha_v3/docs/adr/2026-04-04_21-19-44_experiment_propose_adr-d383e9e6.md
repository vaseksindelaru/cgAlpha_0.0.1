# ADR adr-d383e9e6

- Fecha: 2026-04-04T21:19:44.465102+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-04_21-19_07`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-bc6b1621

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-bc6b1621",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
