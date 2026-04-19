# ADR adr-be06e6b5

- Fecha: 2026-04-14T14:03:13.399098+00:00
- Trigger: `library_ingest`
- Iteración: `2026-04-14_14-03_01`
- Nivel evento: `warning`

## Contexto
LILA: ingesta duplicada [secondary] src-6797b127

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "source_id": "src-6797b127",
  "source_type": "secondary",
  "is_new": false,
  "title": "Same Paper"
}
```
