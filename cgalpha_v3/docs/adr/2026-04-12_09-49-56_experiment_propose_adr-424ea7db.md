# ADR adr-424ea7db

- Fecha: 2026-04-12T09:49:56.742631+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-12_09-49_01`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-67f5023e

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-67f5023e",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
