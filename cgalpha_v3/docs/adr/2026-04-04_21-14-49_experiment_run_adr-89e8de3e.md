# ADR adr-89e8de3e

- Fecha: 2026-04-04T21:14:49.068193+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-04_21-14_01`
- Nivel evento: `critical`

## Contexto
EXPERIMENT: temporal leakage detectado ([DQ] TemporalLeakageError: 1 feature(s) con timestamp >= OOS start (1775297689.052992). Violación del protocolo OOS (Sección E).)

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "error": "[DQ] TemporalLeakageError: 1 feature(s) con timestamp >= OOS start (1775297689.052992). Violación del protocolo OOS (Sección E)."
}
```
