# ADR adr-4d4a08bd

- Fecha: 2026-04-04T20:57:32.644465+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-04_20-57_01`
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
