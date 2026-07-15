"""Exercício 2 — Escolher solução por utilidade ponderada.

Setup:
    nomes = ["regra", "leve", "forte"]
    M = [[0.70, 8, 0.2],
         [0.90, 200, 1.5],
         [0.97, 900, 7.0]]   # colunas: precisao, latencia_ms, custo_relativo
    pesos: w_p=0.6, w_l=0.25, w_c=0.15

Tarefa:
    Normalize latência e custo pelos seus máximos, calcule
    `utilidade = 0.6*prec - 0.25*lat_norm - 0.15*custo_norm`, imprima
    `{nome:>6}: utilidade={u:.3f}` para cada candidato e, na última linha,
    `escolhido: {melhor}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/081-design-ai-first/solucao_2.saida.txt
"""
import numpy as np

nomes = ["regra", "leve", "forte"]
M = np.array([
    [0.70, 8.0, 0.2],
    [0.90, 200.0, 1.5],
    [0.97, 900.0, 7.0],
])

# TODO: normalize, calcule a utilidade ponderada e imprima o vencedor.
