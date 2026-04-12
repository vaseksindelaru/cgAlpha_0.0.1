# ADR adr-bebdf8fd

- Fecha: 2026-04-12T01:08:51.162073+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-12_01-08`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-b2398434

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-b2398434",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
