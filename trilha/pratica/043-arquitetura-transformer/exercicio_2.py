"""Exercício 2 — Feed-forward com ReLU.

Setup (dado):
    rng = np.random.default_rng(101)
    d_model, d_ff = 4, 16
    Gere, NESTA ordem: X (3, d_model), W1 (d_model, d_ff), W2 (d_ff, d_model).

Tarefa:
    Calcule H = relu(X @ W1) e Y = H @ W2. Imprima:
        - "fracao de ativacoes ocultas zeradas (ReLU):" round((H == 0).mean(), 4)
        - "saida shape:", Y.shape
        - "Y[0] =", np.round(Y[0], 4)

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/043-arquitetura-transformer/solucao_2.saida.txt
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)

rng = np.random.default_rng(101)
d_model, d_ff = 4, 16

# TODO: gerar X, W1, W2 (nesta ordem); calcular H = relu(X@W1), Y = H@W2 e os prints.
