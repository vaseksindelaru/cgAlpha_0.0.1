# ADR adr-a9b17cff

- Fecha: 2026-04-04T21:12:33.020632+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-04_21-12_01`
- Nivel evento: `info`

## Contexto
EXPERIMENT: ejecución completada exp-bf1f37b0

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "experiment_id": "exp-bf1f37b0",
  "proposal_id": "prop-090deb8e",
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
