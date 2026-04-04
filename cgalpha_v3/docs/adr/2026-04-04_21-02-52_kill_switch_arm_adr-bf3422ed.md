# ADR adr-bf3422ed

- Fecha: 2026-04-04T21:02:52.324204+00:00
- Trigger: `kill_switch_arm`
- Iteración: `2026-04-04_21-02`
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
