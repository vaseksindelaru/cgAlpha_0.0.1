# ADR adr-2a856eab

- Fecha: 2026-04-12T01:30:01.674595+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-12_01-30`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-41b32c44

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-41b32c44",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
