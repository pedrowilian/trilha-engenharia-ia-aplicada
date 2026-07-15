"""Solução de referência — Exercício 1 da Lição 062.

Laço de controle de um agente: percepção -> raciocínio -> ação -> feedback.
O agente parte de 0 e deve atingir o objetivo somando passos de +3 (quando
possível) ou +1. Determinístico.
"""

objetivo = 10
estado = 0
passos = 0

while estado < objetivo:                       # condição de continuação
    restante = objetivo - estado               # PERCEPÇÃO
    acao = "+3" if restante >= 3 else "+1"      # RACIOCÍNIO (planner)
    estado += 3 if acao == "+3" else 1          # AÇÃO (executor)
    passos += 1                                 # FEEDBACK
    print(f"passo {passos}: acao={acao} estado={estado}")

print(f"objetivo atingido em {passos} passos")
