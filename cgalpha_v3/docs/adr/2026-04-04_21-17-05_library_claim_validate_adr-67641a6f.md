# ADR adr-67641a6f

- Fecha: 2026-04-04T21:17:05.844893+00:00
- Trigger: `library_claim_validate`
- Iteración: `2026-04-04_21-17_01`
- Nivel evento: `warning`

## Contexto
LILA: primary_source_gap detectado

## Decisión
- Registrar decisión runtime para trazabilidad.

## Consecuencias
- Revisión futura en auditoría de iteraciones.

## Evidencia
```json
{
  "claim": "Momentum intradia robusto",
  "source_ids": [
    "src-2576c4c7"
  ],
  "primary_source_gap": true,
  "claim_ok": false,
  "validation_message": "claim 'Momentum intradia robusto' apoyado solo en fuentes ['tertiary'] — se requiere ≥1 primaria",
  "sources_total": 1,
  "primary_count": 0,
  "missing_source_ids": [],
  "backlog_item_id": "bl-0fa86efb"
}
```
