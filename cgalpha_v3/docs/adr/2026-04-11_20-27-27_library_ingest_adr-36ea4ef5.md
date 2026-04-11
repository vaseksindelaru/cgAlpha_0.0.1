# ADR adr-36ea4ef5

- Fecha: 2026-04-11T20:27:27.691425+00:00
- Trigger: `library_ingest`
- Iteración: `2026-04-11_20-27_01`
- Nivel evento: `warning`

## Contexto
LILA: ingesta duplicada [secondary] src-cb2d35bd

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "source_id": "src-cb2d35bd",
  "source_type": "secondary",
  "is_new": false,
  "title": "Same Paper"
}
```
