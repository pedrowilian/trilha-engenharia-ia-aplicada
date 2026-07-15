"""Exercício 2 — Multi-head attention completa.

Setup (dado):
    rng = np.random.default_rng(7)
    n, d_model, h = 5, 12, 3
    Gere, NESTA ordem: X, Wq, Wk, Wv, Wo = rng.normal(0, 1, ...) com as formas
    X (n, d_model) e cada W (d_model, d_model).

Tarefa:
    Monte a multi-head: split -> atenção escalada por cabeça -> merge -> @ Wo.
    Imprima:
        - "saida shape:", saida.shape
        - "soma de cada linha dos pesos (deve ser 1):" e np.round(pesos.sum(axis=-1), 4)
        - "saida[0] =", np.round(saida[0], 4)

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/042-multi-head-attention/solucao_2.saida.txt
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)

rng = np.random.default_rng(7)
n, d_model, h = 5, 12, 3

# TODO: gerar X, Wq, Wk, Wv, Wo (nesta ordem) e implementar a multi-head attention.
