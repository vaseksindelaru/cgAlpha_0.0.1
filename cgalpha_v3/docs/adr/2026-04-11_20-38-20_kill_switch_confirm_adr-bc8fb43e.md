# ADR adr-bc8fb43e

- Fecha: 2026-04-11T20:38:20.872541+00:00
- Trigger: `kill_switch_confirm`
- Iteración: `2026-04-11_20-38_01`
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
