# ADR adr-f6b15ea3

- Fecha: 2026-04-19T11:27:40.707371+00:00
- Trigger: `kill_switch_arm`
- Iteración: `2026-04-19_11-27`
- Nivel evento: `warning`

## Contexto
KILL-SWITCH: solicitud de activación (paso 1 de 2)

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "kill_switch_status": "arming"
}
```
