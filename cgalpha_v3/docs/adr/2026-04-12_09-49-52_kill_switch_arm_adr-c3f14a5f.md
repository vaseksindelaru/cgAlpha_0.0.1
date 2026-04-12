# ADR adr-c3f14a5f

- Fecha: 2026-04-12T09:49:52.320189+00:00
- Trigger: `kill_switch_arm`
- Iteración: `2026-04-12_09-49`
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
