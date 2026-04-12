# ADR adr-ff0f6e38

- Fecha: 2026-04-12T01:30:01.685858+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-12_01-30_01`
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
