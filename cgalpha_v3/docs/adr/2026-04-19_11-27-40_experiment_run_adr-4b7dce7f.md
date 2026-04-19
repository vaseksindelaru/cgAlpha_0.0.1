# ADR adr-4b7dce7f

- Fecha: 2026-04-19T11:27:40.624803+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-19_11-27_01`
- Nivel evento: `critical`

## Contexto
EXPERIMENT: temporal leakage detectado ([DQ] TemporalLeakageError: 1 feature(s) con timestamp >= OOS start (1776558460.619053). Violación del protocolo OOS (Sección E).)

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "error": "[DQ] TemporalLeakageError: 1 feature(s) con timestamp >= OOS start (1776558460.619053). Violación del protocolo OOS (Sección E)."
}
```
