# ADR adr-9ea267df

- Fecha: 2026-04-12T01:29:54.521757+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-12_01-29_01`
- Nivel evento: `info`

## Contexto
EXPERIMENT: ejecución completada exp-1447cceb

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "experiment_id": "exp-1447cceb",
  "proposal_id": "prop-f6862e6c",
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
