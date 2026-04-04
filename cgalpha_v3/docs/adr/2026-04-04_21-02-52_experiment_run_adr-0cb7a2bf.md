# ADR adr-0cb7a2bf

- Fecha: 2026-04-04T21:02:52.203519+00:00
- Trigger: `experiment_run`
- Iteración: `2026-04-04_21-02_01`
- Nivel evento: `critical`

## Contexto
EXPERIMENT: temporal leakage detectado ([DQ] TemporalLeakageError: 1 feature(s) con timestamp >= OOS start (1775296972.18694). Violación del protocolo OOS (Sección E).)

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "error": "[DQ] TemporalLeakageError: 1 feature(s) con timestamp >= OOS start (1775296972.18694). Violación del protocolo OOS (Sección E)."
}
```
