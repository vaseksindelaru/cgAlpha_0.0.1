# ADR adr-f7f216b4

- Fecha: 2026-04-12T09:49:52.327755+00:00
- Trigger: `kill_switch_confirm`
- Iteración: `2026-04-12_09-49_01`
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
