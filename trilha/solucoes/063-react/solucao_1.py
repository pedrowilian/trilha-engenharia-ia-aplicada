"""Solução de referência — Exercício 1 da Lição 063.

Formata um traço ReAct (Thought / Action / Observation) e reporta o total de
passos. Determinístico.
"""

traco = [
    {"thought": "Localizar a capital", "action": "kb[capital_franca]", "observation": "Paris"},
    {"thought": "Contar as letras", "action": "tamanho[Paris]", "observation": "5"},
    {"thought": "Tenho a resposta", "action": "final[5]", "observation": "-"},
]

for i, p in enumerate(traco, 1):
    print(f"{i}. Thought: {p['thought']} | Action: {p['action']} | Observation: {p['observation']}")

print(f"total de passos: {len(traco)}")
