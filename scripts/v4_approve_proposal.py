
import sys
import os
import json

# Añadir el root del proyecto al path
sys.path.append(os.getcwd())

from cgalpha_v3.lila.evolution_orchestrator import EvolutionOrchestratorV4
from cgalpha_v3.lila.llm.llm_switcher import LLMSwitcher
from cgalpha_v3.lila.llm.assistant import LLMAssistant
from cgalpha_v3.lila.codecraft_sage import CodeCraftSage
from cgalpha_v3.learning.memory_policy import MemoryPolicyEngine

def approve(proposal_id):
    memory = MemoryPolicyEngine()
    memory.load_from_disk()
    
    assistant = LLMAssistant()
    switcher = LLMSwitcher(assistant=assistant)
    
    sage = CodeCraftSage.create_default()
    sage.switcher = switcher
    
    orchestrator = EvolutionOrchestratorV4(
        memory=memory,
        switcher=switcher,
        sage=sage
    )
    
    print(f"Aprobando propuesta {proposal_id}...")
    result = orchestrator.approve_proposal(proposal_id, approved_by="human")
    
    print(f"Status final: {result.status}")
    if result.error:
        print(f"Error: {result.error}")
    print(f"Branch: {result.branch_name}")
    print(f"Tests Passed: {result.tests_passed}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python scripts/v4_approve_bug5.py <proposal_id>")
    else:
        approve(sys.argv[1])
