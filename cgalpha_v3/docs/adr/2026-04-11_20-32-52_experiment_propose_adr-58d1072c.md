# ADR adr-58d1072c

- Fecha: 2026-04-11T20:32:52.506108+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-11_20-32`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-c1942cea

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-c1942cea",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
