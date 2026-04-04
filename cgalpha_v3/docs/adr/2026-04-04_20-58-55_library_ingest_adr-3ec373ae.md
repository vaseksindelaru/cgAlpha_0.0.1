# ADR adr-3ec373ae

- Fecha: 2026-04-04T20:58:55.319442+00:00
- Trigger: `library_ingest`
- Iteración: `2026-04-04_20-58_01`
- Nivel evento: `warning`

## Contexto
LILA: ingesta duplicada [secondary] src-fabfa654

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "source_id": "src-fabfa654",
  "source_type": "secondary",
  "is_new": false,
  "title": "Same Paper"
}
```
