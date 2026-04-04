# ADR adr-c3dd00f2

- Fecha: 2026-04-04T21:00:07.428318+00:00
- Trigger: `library_ingest`
- Iteración: `2026-04-04_21-00_01`
- Nivel evento: `warning`

## Contexto
LILA: ingesta duplicada [secondary] src-157242f7

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "source_id": "src-157242f7",
  "source_type": "secondary",
  "is_new": false,
  "title": "Same Paper"
}
```
