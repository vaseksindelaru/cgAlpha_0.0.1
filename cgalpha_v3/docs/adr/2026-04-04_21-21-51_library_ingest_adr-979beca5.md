# ADR adr-979beca5

- Fecha: 2026-04-04T21:21:51.845573+00:00
- Trigger: `library_ingest`
- Iteración: `2026-04-04_21-21`
- Nivel evento: `info`

## Contexto
LILA: ingesta nueva [primary] src-ab433973

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "source_id": "src-ab433973",
  "source_type": "primary",
  "is_new": true,
  "title": "Primary paper"
}
```
