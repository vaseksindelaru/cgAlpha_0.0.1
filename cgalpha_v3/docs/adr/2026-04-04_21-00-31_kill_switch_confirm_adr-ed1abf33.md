# ADR adr-ed1abf33

- Fecha: 2026-04-04T21:00:31.846962+00:00
- Trigger: `kill_switch_confirm`
- Iteración: `2026-04-04_21-00_01`
- Nivel evento: `critical`

## Contexto
KILL-SWITCH: ACTIVADO — señales suspendidas

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "kill_switch_status": "triggered",
  "system_status": "kill-switch-active"
}
```
