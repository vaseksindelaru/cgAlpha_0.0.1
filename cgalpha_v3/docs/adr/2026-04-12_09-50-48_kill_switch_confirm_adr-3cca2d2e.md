# ADR adr-3cca2d2e

- Fecha: 2026-04-12T09:50:48.800954+00:00
- Trigger: `kill_switch_confirm`
- Iteración: `2026-04-12_09-50_01`
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
