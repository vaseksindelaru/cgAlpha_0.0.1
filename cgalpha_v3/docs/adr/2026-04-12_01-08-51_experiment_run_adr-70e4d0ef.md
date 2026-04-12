# ADR adr-70e4d0ef

- Fecha: 2026-04-12T01:08:51.174580+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-12_01-08_01`
- Nivel evento: `critical`

## Contexto
EXPERIMENT: temporal leakage detectado ([DQ] TemporalLeakageError: 1 feature(s) con timestamp >= OOS start (1775916531.166103). Violación del protocolo OOS (Sección E).)

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "error": "[DQ] TemporalLeakageError: 1 feature(s) con timestamp >= OOS start (1775916531.166103). Violación del protocolo OOS (Sección E)."
}
```
