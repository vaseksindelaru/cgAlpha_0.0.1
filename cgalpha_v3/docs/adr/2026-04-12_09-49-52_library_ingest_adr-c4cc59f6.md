# ADR adr-c4cc59f6

- Fecha: 2026-04-12T09:49:52.473255+00:00
- Trigger: `library_ingest`
- Iteración: `2026-04-12_09-49_01`
- Nivel evento: `warning`

## Contexto
LILA: ingesta duplicada [secondary] src-516547ba

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "source_id": "src-516547ba",
  "source_type": "secondary",
  "is_new": false,
  "title": "Same Paper"
}
```
