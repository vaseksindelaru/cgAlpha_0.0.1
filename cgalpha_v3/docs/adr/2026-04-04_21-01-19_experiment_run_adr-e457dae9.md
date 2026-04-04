# ADR adr-e457dae9

- Fecha: 2026-04-04T21:01:19.118640+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-04_21-01_01`
- Nivel evento: `critical`

## Contexto
EXPERIMENT: temporal leakage detectado ([DQ] TemporalLeakageError: 1 feature(s) con timestamp >= OOS start (1775296879.114716). Violación del protocolo OOS (Sección E).)

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "error": "[DQ] TemporalLeakageError: 1 feature(s) con timestamp >= OOS start (1775296879.114716). Violación del protocolo OOS (Sección E)."
}
```
