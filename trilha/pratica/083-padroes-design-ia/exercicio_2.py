"""Exercício 2 — Semantic cache por cosseno.

Setup:
    cache_emb = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    cache_resp = ["A", "B", "C"]
    limiar = 0.9
    consultas = [[0.95, 0.05, 0], [0.0, 0.30, 0.95], [0.6, 0.6, 0.0]]

Tarefa:
    Implemente `cosseno(a, b)` e `consultar(q, limiar)` que devolve
    ("hit", resposta, sim_arredondada_em_3) se a maior similaridade >= limiar,
    senão ("miss", None, sim). Imprima `sim={sim} -> {estado} | {resp}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/083-padroes-design-ia/solucao_2.saida.txt
"""
import numpy as np

cache_emb = np.array([
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
])
cache_resp = ["A", "B", "C"]
consultas = [
    np.array([0.95, 0.05, 0.0]),
    np.array([0.0, 0.30, 0.95]),
    np.array([0.6, 0.6, 0.0]),
]
limiar = 0.9

# TODO: implemente cosseno(...) e consultar(...) e classifique cada consulta.
