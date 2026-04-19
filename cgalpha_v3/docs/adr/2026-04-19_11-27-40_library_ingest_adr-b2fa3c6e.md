# ADR adr-b2fa3c6e

- Fecha: 2026-04-19T11:27:40.827897+00:00
- Trigger: `library_ingest`
- Iteración: `2026-04-19_11-27_01`
- Nivel evento: `warning`

## Contexto
LILA: ingesta duplicada [secondary] src-4188d0f5

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "source_id": "src-4188d0f5",
  "source_type": "secondary",
  "is_new": false,
  "title": "Same Paper"
}
```
