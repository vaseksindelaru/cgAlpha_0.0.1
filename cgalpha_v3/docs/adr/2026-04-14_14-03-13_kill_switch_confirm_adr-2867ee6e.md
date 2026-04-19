# ADR adr-2867ee6e

- Fecha: 2026-04-14T14:03:13.302822+00:00
- Trigger: `kill_switch_confirm`
- Iteración: `2026-04-14_14-03_01`
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
