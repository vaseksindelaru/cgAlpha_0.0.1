# ADR adr-81ef1fd3

- Fecha: 2026-04-04T20:57:40.619626+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-04_20-57_03`
- Nivel evento: `critical`

## Contexto
EXPERIMENT: temporal leakage detectado (Simulated leakage)

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "error": "Simulated leakage"
}
```
