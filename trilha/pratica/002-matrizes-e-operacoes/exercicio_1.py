"""Exercício 1 — Multiplicação de matrizes implementada do zero.

Setup:
    A = [[1.0, 2.0], [3.0, 4.0]]
    B = [[5.0, 6.0], [7.0, 8.0]]

Tarefa:
    1. Implemente matmul(A, B) com laços: (A@B)[i][j] = soma_k A[i][k]*B[k][j].
    2. Imprima o resultado e confirme com np.allclose contra np.array(A) @ np.array(B).
    3. Saída esperada:
        A@B (do zero): [[19.0, 22.0], [43.0, 50.0]]
        confere numpy? True

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/002-matrizes-e-operacoes/solucao_1.saida.txt
"""
import numpy as np


def matmul(A, B):
    # TODO: implementar a multiplicação com laços (sem usar @ nem np.dot).
    raise NotImplementedError


A = [[1.0, 2.0], [3.0, 4.0]]
B = [[5.0, 6.0], [7.0, 8.0]]

# TODO: imprimir matmul(A, B) e a verificação com np.allclose.
