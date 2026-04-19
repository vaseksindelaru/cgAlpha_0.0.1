
import sys
import os

# Añadir el root del proyecto al path
sys.path.append(os.getcwd())

from cgalpha_v3.lila.llm.proposer import TechnicalSpec
from cgalpha_v3.lila.evolution_orchestrator import EvolutionOrchestratorV4
from cgalpha_v3.learning.memory_policy import MemoryPolicyEngine

def inject():
    memory = MemoryPolicyEngine()
    memory.load_from_disk()
    
    # No necesitamos switcher ni sage para este script de inyección física en el log
    # pero el Orchestrator real en server.py sí los tendrá.
    
    spec = TechnicalSpec(
        change_type="bugfix",
        target_file="cgalpha_v3/lila/evolution_orchestrator.py",
        target_attribute="retrain_trigger",
        old_value=0,
        new_value=1,
        reason="BUG-5: Pipeline no llama a train_model(). Agregar llamada a retrain_recursive() del Oracle tras detectar drift o periódicamente.",
        causal_score_est=0.85,
        confidence=0.9
    )
    
    # Como el orchestrator guarda en evolution_log.jsonl, 
    # podemos simular la recepción de la propuesta.
    
    orchestrator = EvolutionOrchestratorV4(memory=memory)
    # process_proposal clasificará esto como Cat.2 por ser 'bugfix'
    result = orchestrator.process_proposal(spec)
    
    print(f"Propuesta inyectada: {result.proposal_id}")
    print(f"Categoría: {result.category}")
    print(f"Status: {result.status}")

if __name__ == "__main__":
    inject()
