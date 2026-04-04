# ADR adr-a1c8e0c8

- Fecha: 2026-04-04T21:12:33.195775+00:00
- Trigger: `kill_switch_arm`
- Iteración: `2026-04-04_21-12`
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
