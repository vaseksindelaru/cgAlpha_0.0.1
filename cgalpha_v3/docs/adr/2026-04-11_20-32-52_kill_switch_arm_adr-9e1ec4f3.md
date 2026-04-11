# ADR adr-9e1ec4f3

- Fecha: 2026-04-11T20:32:52.658315+00:00
- Trigger: `kill_switch_arm`
- Iteración: `2026-04-11_20-32`
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
