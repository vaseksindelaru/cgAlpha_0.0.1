"""
cgAlpha_0.0.1 — LLM Switcher v4
================================
Selección de proveedor LLM por tipo de tarea.

Reglas de §4 del Prompt Fundacional:
- Cat.1 (parámetros): Qwen local via Ollama (rápido, sin costo)
- Cat.2 (semi-auto): GPT / Gemini (calidad media, costo moderado)
- Cat.3 (supervisado): Claude / GPT-4 (máxima calidad)
- Fallback: si el proveedor seleccionado no responde, degradar al siguiente

El Switcher NO reemplaza a LLMAssistant — lo envuelve.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, Optional

logger = logging.getLogger("llm_switcher")


@dataclass
class ProviderConfig:
    """Configuración de un proveedor para un tipo de tarea."""
    name: str
    priority: int  # menor = mayor prioridad
    model: str = ""
    temperature: float = 0.7
    max_tokens: int = 600
    available: bool = True


@dataclass
class LLMSwitcher:
    """
    Selección inteligente de proveedor LLM por tipo de tarea.

    Uso:
        switcher = LLMSwitcher(assistant=llm_assistant)
        provider = switcher.select("cat_1")
        result = switcher.generate("cat_1", prompt="Analiza este diff...")
    """
    assistant: Any = None  # LLMAssistant instance
    _task_routing: dict[str, list[ProviderConfig]] = field(default_factory=dict)
    _fallback_order: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not self._task_routing:
            self._task_routing = self._default_routing()
        if not self._fallback_order:
            self._fallback_order = ["ollama", "openai", "zhipu"]

    @staticmethod
    def _default_routing() -> dict[str, list[ProviderConfig]]:
        """Routing por defecto basado en las reglas del Prompt Fundacional §4."""
        return {
            "cat_1": [
                ProviderConfig(name="gemini", priority=1, temperature=0.3, max_tokens=400),
                ProviderConfig(name="ollama", priority=2, temperature=0.3, max_tokens=400),
                ProviderConfig(name="openai", priority=3, temperature=0.3, max_tokens=400),
            ],
            "cat_2": [
                ProviderConfig(name="gemini", priority=1, temperature=0.5, max_tokens=1000),
                ProviderConfig(name="openai", priority=2, temperature=0.5, max_tokens=1000),
                ProviderConfig(name="zhipu", priority=3, temperature=0.5, max_tokens=1000),
                ProviderConfig(name="ollama", priority=4, temperature=0.5, max_tokens=1000),
            ],
            "cat_3": [
                ProviderConfig(name="gemini", priority=1, temperature=0.7, max_tokens=4000),
                ProviderConfig(name="openai", priority=2, temperature=0.7, max_tokens=4000),
                ProviderConfig(name="zhipu", priority=3, temperature=0.7, max_tokens=4000),
            ],
            "reflection": [
                ProviderConfig(name="gemini", priority=1, temperature=0.4, max_tokens=1000),
                ProviderConfig(name="openai", priority=2, temperature=0.4, max_tokens=1000),
                ProviderConfig(name="ollama", priority=3, temperature=0.4, max_tokens=1000),
            ],
            "whitepaper": [
                ProviderConfig(name="gemini", priority=1, temperature=0.6, max_tokens=4000),
                ProviderConfig(name="openai", priority=2, temperature=0.6, max_tokens=4000),
                ProviderConfig(name="zhipu", priority=3, temperature=0.6, max_tokens=4000),
            ],
        }

    def select(self, task_type: str) -> ProviderConfig:
        """
        Selecciona la mejor configuración de proveedor para un tipo de tarea.

        Args:
            task_type: "cat_1", "cat_2", "cat_3", "reflection", "whitepaper"

        Returns:
            ProviderConfig con el proveedor a usar.

        Raises:
            ValueError: si task_type no está registrado.
        """
        if task_type not in self._task_routing:
            raise ValueError(
                f"Tipo de tarea '{task_type}' no registrado. "
                f"Disponibles: {list(self._task_routing.keys())}"
            )

        candidates = sorted(
            self._task_routing[task_type],
            key=lambda c: c.priority
        )

        for config in candidates:
            if config.available:
                return config

        # Si ninguno está disponible, devolver el de mayor prioridad
        logger.warning(
            f"Ningún proveedor disponible para '{task_type}'. "
            f"Usando {candidates[0].name} de todas formas."
        )
        return candidates[0]

    def generate(self, task_type: str, prompt: str, **kwargs) -> str:
        """
        Genera respuesta usando el proveedor adecuado para el tipo de tarea.

        Intenta el proveedor primario, si falla => fallback al siguiente.
        """
        if not self.assistant:
            raise RuntimeError("LLMSwitcher requiere un LLMAssistant configurado")

        config = self.select(task_type)
        candidates = sorted(
            self._task_routing.get(task_type, []),
            key=lambda c: c.priority
        )

        for cfg in candidates:
            if not cfg.available:
                continue
            try:
                # Switch provider if needed
                if self.assistant.provider.name != cfg.name:
                    switched = self.assistant.switch_provider(cfg.name)
                    if not switched:
                        logger.warning(f"No se pudo cambiar a {cfg.name}")
                        continue

                result = self.assistant.generate(
                    prompt,
                    temperature=kwargs.get("temperature", cfg.temperature),
                    max_tokens=kwargs.get("max_tokens", cfg.max_tokens),
                )
                logger.info(
                    f"✅ LLM_SWITCHER: {task_type} → {cfg.name} "
                    f"(tokens={cfg.max_tokens}, temp={cfg.temperature})"
                )
                return result

            except Exception as e:
                logger.warning(
                    f"⚠️ LLM_SWITCHER: {cfg.name} falló para {task_type}: "
                    f"{type(e).__name__}: {e}"
                )
                cfg.available = False
                continue

        raise RuntimeError(
            f"Todos los proveedores fallaron para '{task_type}'"
        )

    def mark_available(self, provider_name: str) -> None:
        """Marca un proveedor como disponible de nuevo."""
        for configs in self._task_routing.values():
            for cfg in configs:
                if cfg.name == provider_name:
                    cfg.available = True

    def mark_unavailable(self, provider_name: str) -> None:
        """Marca un proveedor como no disponible."""
        for configs in self._task_routing.values():
            for cfg in configs:
                if cfg.name == provider_name:
                    cfg.available = False

    def add_task_type(self, task_type: str, configs: list[ProviderConfig]) -> None:
        """Registra un nuevo tipo de tarea con sus proveedores."""
        self._task_routing[task_type] = sorted(configs, key=lambda c: c.priority)
        logger.info(f"Nuevo task_type registrado: {task_type}")

    def get_routing_table(self) -> dict[str, list[dict]]:
        """Devuelve la tabla de routing para el snapshot/GUI."""
        result = {}
        for task_type, configs in self._task_routing.items():
            result[task_type] = [
                {
                    "name": c.name,
                    "priority": c.priority,
                    "temperature": c.temperature,
                    "max_tokens": c.max_tokens,
                    "available": c.available,
                }
                for c in sorted(configs, key=lambda c: c.priority)
            ]
        return result
