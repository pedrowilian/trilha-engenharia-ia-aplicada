"""Exercício 2 — Por que dividir por raiz de d_k.

Setup:
    d_k = 64; Q (1 x 64) e K (5 x 64) gerados por np.random.default_rng(0).

Tarefa:
    Compute os scores brutos (Q @ K.T) e escalados (/sqrt(d_k)). Imprima o
    desvio-padrão de cada (4 casas) e o peso máximo da softmax em cada caso,
    evidenciando que sem escala a distribuição satura.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/040-self-attention-qkv/solucao_2.saida.txt
"""
import numpy as np


def softmax(x, axis=-1):
    x = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(x)
    return e / np.sum(e, axis=axis, keepdims=True)


rng = np.random.default_rng(0)
d_k = 64
Q = rng.normal(0, 1, size=(1, d_k))
K = rng.normal(0, 1, size=(5, d_k))

# TODO: scores brutos/escalados, desvios-padrão e pesos máximos.
