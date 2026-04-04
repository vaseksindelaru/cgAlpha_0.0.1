# ADR adr-bb9aebc8

- Fecha: 2026-04-04T21:01:19.707281+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-04_21-01_07`
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
