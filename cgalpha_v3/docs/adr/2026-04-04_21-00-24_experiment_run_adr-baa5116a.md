# ADR adr-baa5116a

- Fecha: 2026-04-04T21:00:24.605699+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-04_21-00_04`
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
