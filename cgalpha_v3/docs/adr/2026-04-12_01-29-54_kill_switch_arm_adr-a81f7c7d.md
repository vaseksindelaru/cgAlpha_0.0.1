# ADR adr-a81f7c7d

- Fecha: 2026-04-12T01:29:54.678378+00:00
- Trigger: `kill_switch_arm`
- Iteración: `2026-04-12_01-29`
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
