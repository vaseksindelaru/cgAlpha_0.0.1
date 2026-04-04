# ADR adr-08cda205

- Fecha: 2026-04-04T21:02:52.135411+00:00
- Trigger: `experiment_propose`
- Iteración: `2026-04-04_21-02`
- Nivel evento: `info`

## Contexto
EXPERIMENT: propuesta generada prop-c1d8eb83

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "proposal_id": "prop-c1d8eb83",
  "frictions": {
    "fee_taker_pct": 0.05,
    "fee_maker_pct": 0.02,
    "slippage_bps": 2.0,
    "latency_ms": 100.0
  },
  "walk_forward_windows": 3
}
```
