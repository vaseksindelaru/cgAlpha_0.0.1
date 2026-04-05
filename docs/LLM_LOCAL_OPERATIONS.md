# Local LLM Operations Guide (Lila v3)

> [!IMPORTANT]
> **Consolidación v3**: Toda la infraestructura de LLM local ha sido migrada al espacio `cgalpha_v3`. 
> Los comandos `cgalpha ask` ahora utilizan el nuevo **Lila Assistant v3** con arquitectura de doble capa.

## Objective

Este manual estandariza el uso de LLM locales bajo el motor de **Lila v3**. La arquitectura se divide en dos capas operativas:

- **Capa 3 (Sintetizador)**: `qwen2.5:3b`. Razonamiento profundo, validación académica y síntesis de contexto.
- **Capa 2 (Recuperador)**: `qwen2.5:1.5b`. Búsqueda semántica ultra-rápida y extracción de datos.

## Available CLI Commands

### Technical Mentor (Ask)

Consulta sobre arquitectura, flujos o dudas técnicas generales.
```bash
cgalpha ask "¿Cómo se comunica el RiskManager con Lila?"
```

### Requirements Architect

Genera especificaciones técnicas a partir de ideas vagas.
```bash
cgalpha ask-requirements "Implementar un nuevo gate de calidad para volumen"
```

### Assistant Status

Verifica la conexión con Ollama y el proveedor activo.
```bash
cgalpha ask-health
```

## Recommended Settings

La v3 autogestiona los parámetros del modelo, pero se puede configurar el proveedor en caliente desde la **GUI Control Room** (Lila settings).

### Hardware Roles:
- **Balanceado**: `qwen2.5:1.5b` (Layer 2) + `qwen2.5:3b` (Layer 3).
- **Pro**: `qwen2.5:7b` (si está disponible en Ollama para Layer 3).

## Why this matters

Lila v3 no es solo un chat; es el **cerebro híbrido** de CGAlpha. Utiliza el LLM local para:
- Proteger la privacidad de los datos estratégicos.
- Mantener latencia baja en la recuperación de hechos (0a-4 levels).
- Validar cada señal con fundamento académico antes de la ejecución.
