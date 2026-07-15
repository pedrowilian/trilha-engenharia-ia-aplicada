"""Exercício 1 — LayerNorm do zero.

Setup (dado):
    X = np.array([[2.0, 4.0, 6.0, 8.0],
                  [1.0, 1.0, 1.0, 5.0],
                  [-3.0, 0.0, 3.0, 6.0]])

Tarefa:
    Implemente layer_norm(x, eps=1e-5) normalizando ao longo da ÚLTIMA dimensão
    (média 0, variância 1 por linha; sem gamma/beta). Imprima:
        - a matriz normalizada (np.round(..., 4))
        - "media por linha:", np.round(Y.mean(axis=-1), 4)
        - "desvio por linha:", np.round(Y.std(axis=-1), 4)

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/043-arquitetura-transformer/solucao_1.saida.txt
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)

X = np.array([[2.0, 4.0, 6.0, 8.0],
              [1.0, 1.0, 1.0, 5.0],
              [-3.0, 0.0, 3.0, 6.0]])

# TODO: implementar layer_norm e imprimir matriz normalizada, média e desvio por linha.
