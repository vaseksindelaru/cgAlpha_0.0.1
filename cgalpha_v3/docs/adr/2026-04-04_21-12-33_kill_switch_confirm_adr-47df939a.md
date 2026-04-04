# ADR adr-47df939a

- Fecha: 2026-04-04T21:12:33.202411+00:00
- Trigger: `kill_switch_confirm`
- Iteración: `2026-04-04_21-12_01`
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
