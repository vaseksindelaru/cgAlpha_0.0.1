# ADR adr-07cdafa6

- Fecha: 2026-04-12T09:50:52.470276+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-12_09-50_02`
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
