# ADR adr-2f2cebd0

- Fecha: 2026-04-12T01:08:51.147387+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-12_01-08_01`
- Nivel evento: `info`

## Contexto
EXPERIMENT: ejecución completada exp-0422c4e4

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "experiment_id": "exp-0422c4e4",
  "proposal_id": "prop-3188b593",
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
