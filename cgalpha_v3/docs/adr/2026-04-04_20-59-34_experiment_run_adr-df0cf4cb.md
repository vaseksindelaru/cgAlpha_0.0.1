# ADR adr-df0cf4cb

- Fecha: 2026-04-04T20:59:34.442841+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-04_20-59_01`
- Nivel evento: `info`

## Contexto
EXPERIMENT: ejecución completada exp-a043e9f3

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "experiment_id": "exp-a043e9f3",
  "proposal_id": "prop-c4633b94",
  "metrics": {
    "gross_return_pct": -0.1318,
    "friction_cost_pct": 1.001,
    "net_return_pct": -1.1328,
    "sharpe_like": -8.0759,
    "max_drawdown_pct": 0.2414,
    "trades": 33.0,
    "walk_forward_windows": 3.0
  },
  "walk_forward_windows": 3,
  "no_leakage_checked": true
}
```
