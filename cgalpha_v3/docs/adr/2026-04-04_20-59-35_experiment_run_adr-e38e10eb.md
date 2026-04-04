# ADR adr-e38e10eb

- Fecha: 2026-04-04T20:59:35.366900+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-04_20-59_04`
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
