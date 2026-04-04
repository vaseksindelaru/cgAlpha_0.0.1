# ADR adr-b8c05c2c

- Fecha: 2026-04-04T21:02:52.533189+00:00
- Trigger: `library_ingest`
- Iteración: `2026-04-04_21-02_01`
- Nivel evento: `warning`

## Contexto
LILA: ingesta duplicada [secondary] src-6813da53

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "source_id": "src-6813da53",
  "source_type": "secondary",
  "is_new": false,
  "title": "Same Paper"
}
```
