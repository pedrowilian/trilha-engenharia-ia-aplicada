"""Exercício 1 — Atribuição de features de uma predição.

Setup: um modelo linear de decisão de crédito com viés `b = 0.5` e os vetores
    nomes = ["valor", "prazo", "historico", "garantia"]
    w = np.array([2.0, -1.2, 1.5, -0.8])
    x = np.array([0.9, 0.4, 0.6, 0.7])

Tarefa:
    Calcule a contribuição de cada feature (`w_i * x_i`) e o logito total
    (`b + soma das contribuições`). Imprima cada feature em ordem decrescente de
    |contribuição|, no formato `"{nome:>9}: {contrib:+.3f}"`, e ao final
    `"logito total: {logito:+.3f}"`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/090-interpretabilidade-explicabilidade/solucao_1.saida.txt
"""
import numpy as np

# TODO: calcule as contribuições e o logito, ordene por |contribuição| e imprima.
