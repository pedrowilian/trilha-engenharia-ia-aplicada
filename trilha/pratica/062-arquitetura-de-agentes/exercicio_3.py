"""Exercício 3 — Condição de parada com limite de iterações.

Setup: a ação fixa soma 2 ao estado (que começa em 0). Objetivos a testar:
[8, 7]. Limite de iterações: max_passos = 6.

Tarefa:
    Implemente `agente(objetivo, max_passos)` que itera enquanto o estado for
    diferente do objetivo E o número de passos for menor que `max_passos`.
    Retorne (estado, passos, atingiu) onde `atingiu = estado == objetivo`.
    Para cada objetivo, imprima
    `objetivo={objetivo}: estado={estado} passos={passos} -> {status}`,
    com status `sucesso` (atingiu) ou `parou no limite`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/062-arquitetura-de-agentes/solucao_3.saida.txt
"""

# TODO: implemente a função agente com a condição de parada dupla.
