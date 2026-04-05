"""
aiphalab/commands/librarian.py - Librarian command (Proxy to v3).

Redirige las consultas locales al nuevo Lila Assistant v3.
Resuelve P3: Consolidación de LLM Local en v3.
"""

from __future__ import annotations
import click
import sys
import logging
from pathlib import Path

# Asegurar que podemos importar cgalpha_v3
ROOT = Path(__file__).resolve().parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cgalpha_v3.lila.llm.assistant import LLMAssistant

@click.command(name="ask")
@click.argument("question", required=False)
@click.option("--role", type=click.Choice(["mentor", "requirements"]), default="mentor")
def ask_command(question: str | None, role: str):
    """
    📚 Librarian v3: Consulta técnica pro-activa.
    """
    if not question:
        click.echo("Uso: cgalpha ask \"¿Cómo funciona la v3?\"")
        return

    try:
        assistant = LLMAssistant()
        click.echo(f"[*] Consultando a Lila (v3) como {role}...")
        
        response = assistant.ask_technical(question, role=role)
        click.echo(f"\n[Lila v3]:\n{response}")
    except Exception as e:
        click.echo(f"Error al conectar con Lila v3: {e}")
        click.echo("Asegúrate de que Ollama esté corriendo y configurado en cgalpha_v3/.env")

@click.command(name="ask-requirements")
@click.argument("question", required=False)
def ask_requirements_command(question: str | None):
    """
    📐 Requirements Architect v3: Especificaciones técnicas pro.
    """
    ctx = click.get_current_context()
    ctx.invoke(ask_command, question=question, role="requirements")

@click.command(name="ask-health")
def ask_health_command():
    """🩺 Salud del sistema de inteligencia local."""
    try:
        assistant = LLMAssistant()
        status = assistant.get_status()
        click.echo(f"Provider: {status['provider_name']}")
        click.echo(f"Status: {status['circuit_breaker']['status']}")
    except Exception as e:
        click.echo(f"Error de salud: {e}")

@click.command(name="ask-setup")
def ask_setup_command():
    """⚙️ Configuración (v3 utiliza .env)."""
    click.echo("Lila v3 utiliza la configuración centralizada en cgalpha_v3/.env")
    click.echo("Usa el panel de ajustes en la GUI para cambiar de proveedor en caliente.")
    click.echo("Modelo por defecto: Qwen 2.5 (1.5b/3b)")
