# ADR adr-0d2e08eb

- Fecha: 2026-04-12T09:50:48.967714+00:00
- Trigger: `library_ingest`
- Iteración: `2026-04-12_09-50`
- Nivel evento: `info`

## Contexto
LILA: ingesta nueva [tertiary] src-1ebf6ce3

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "source_id": "src-1ebf6ce3",
  "source_type": "tertiary",
  "is_new": true,
  "title": "Blog only signal claim"
}
```
