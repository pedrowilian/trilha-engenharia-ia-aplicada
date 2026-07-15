"""Exercício 1 — Formatar um traço ReAct.

Setup: a lista `traco` (abaixo) com três passos, cada um com as chaves
`thought`, `action` e `observation`.

Tarefa:
    Para cada passo (numerado a partir de 1), imprima na forma
    `{i}. Thought: {thought} | Action: {action} | Observation: {observation}`.
    Ao final, imprima `total de passos: {n}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/063-react/solucao_1.saida.txt
"""

traco = [
    {"thought": "Localizar a capital", "action": "kb[capital_franca]", "observation": "Paris"},
    {"thought": "Contar as letras", "action": "tamanho[Paris]", "observation": "5"},
    {"thought": "Tenho a resposta", "action": "final[5]", "observation": "-"},
]

# TODO: formate e imprima o traço e o total de passos.
