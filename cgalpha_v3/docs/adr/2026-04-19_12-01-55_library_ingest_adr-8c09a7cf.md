# ADR adr-8c09a7cf

- Fecha: 2026-04-19T12:01:55.733596+00:00
- Trigger: `library_ingest`
- Iteración: `2026-04-19_12-01_01`
- Nivel evento: `warning`

## Contexto
LILA: ingesta duplicada [secondary] src-3e59be4d

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "source_id": "src-3e59be4d",
  "source_type": "secondary",
  "is_new": false,
  "title": "Same Paper"
}
```
