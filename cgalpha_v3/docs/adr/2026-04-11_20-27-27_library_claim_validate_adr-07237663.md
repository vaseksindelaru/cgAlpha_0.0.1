# ADR adr-07237663

- Fecha: 2026-04-11T20:27:27.872042+00:00
- Trigger: `library_claim_validate`
- Iteración: `2026-04-11_20-27_01`
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
    "src-4fefc677"
  ],
  "primary_source_gap": true,
  "claim_ok": false,
  "validation_message": "claim 'Momentum intradia robusto' apoyado solo en fuentes ['tertiary'] — se requiere ≥1 primaria",
  "sources_total": 1,
  "primary_count": 0,
  "missing_source_ids": [],
  "backlog_item_id": "bl-31422711"
}
```
