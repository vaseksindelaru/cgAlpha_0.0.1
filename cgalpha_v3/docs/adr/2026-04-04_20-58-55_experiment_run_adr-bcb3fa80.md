# ADR adr-bcb3fa80

- Fecha: 2026-04-04T20:58:55.819166+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-04_20-58_02`
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
