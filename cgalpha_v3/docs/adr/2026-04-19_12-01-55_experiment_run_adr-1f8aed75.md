# ADR adr-1f8aed75

- Fecha: 2026-04-19T12:01:55.469280+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-19_12-01_01`
- Nivel evento: `critical`

## Contexto
EXPERIMENT: temporal leakage detectado ([DQ] TemporalLeakageError: 1 feature(s) con timestamp >= OOS start (1776560515.460064). Violación del protocolo OOS (Sección E).)

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "error": "[DQ] TemporalLeakageError: 1 feature(s) con timestamp >= OOS start (1776560515.460064). Violación del protocolo OOS (Sección E)."
}
```
