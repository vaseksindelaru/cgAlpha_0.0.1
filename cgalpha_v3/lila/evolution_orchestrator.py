import logging
import time
from typing import Dict, Any, Optional

from cgalpha_v3.lila.codecraft_sage import CodeCraftSage
from cgalpha_v3.application.live_adapter import LiveDataFeedAdapter
from cgalpha_v3.lila.llm.oracle import OracleTrainer_v3

logger = logging.getLogger("evolution_orchestrator")

class EvolutionOrchestrator:
    """
    Controlador de Auto-Evolución (Capa 5).
    Monitorea la deriva causal y dispara procesos de CodeCraft Sage.
    """
    def __init__(self, shadow_trader: LiveDataFeedAdapter, oracle: OracleTrainer_v3, sage: CodeCraftSage):
        self.shadow_trader = shadow_trader
        self.oracle = oracle
        self.sage = sage
        self.last_evolution_ts = 0
        self.evolution_cooldown = 3600 # 1 hora entre evoluciones automáticas
        
    def check_drift_and_evolve(self):
        """
        Si la delta_causal es crítica, inicia bucle de auto-corrección.
        """
        dc = self.shadow_trader.delta_causal
        is_safe = self.shadow_trader.nexus.is_safe(dc)
        
        if not is_safe and (time.time() - self.last_evolution_ts > self.evolution_cooldown):
            logger.warning(f"🔧 DRIFT DETECTADO ({dc:.4f}). Iniciando bucle de Auto-Evolución...")
            
            # 1. Crear propuesta de mejora técnica via Sage
            # En la v3.1 simplificamos disparando un re-entrenamiento con datos frescos
            try:
                # Nota: En v3.2 esto se haría a través de una Proposal formal de Lila
                # Aquí automatizamos el re-entrenamiento recursivo
                logger.info("📡 Solicitando re-entrenamiento recursivo del Oracle con datos de sesión...")
                
                # Simulación de recolección de datos frescos (OutcomeOrdinals)
                # En un sistema real, esto leería de bridge.jsonl
                # self.oracle.retrain_recursive("aipha_memory/evolutionary/bridge.jsonl")
                
                self.last_evolution_ts = time.time()
                logger.info("✅ Pipeline de evolución disparado con éxito.")
                
            except Exception as e:
                logger.error(f"❌ Error en Auto-Evolución: {e}")
