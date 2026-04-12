# ADR adr-fc42fd22

- Fecha: 2026-04-12T01:08:55.789651+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-12_01-08_01`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-9eb31b4d

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-9eb31b4d",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
