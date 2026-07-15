"""Exercício 2 — Propriedades da transposta.

Setup:
    A = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]   # 2x3
    B = [[1.0, 0.0], [0.0, 1.0], [2.0, 1.0]] # 3x2

Tarefa:
    1. Verifique (A.T).T == A com np.array_equal.
    2. Verifique (A@B).T == B.T@A.T com np.array_equal.
    3. Imprima A@B (via .tolist()).
    4. Saída esperada:
        (A.T).T == A? True
        (A@B).T == B.T@A.T? True
        A@B: [[7.0, 5.0], [16.0, 11.0]]

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/002-matrizes-e-operacoes/solucao_2.saida.txt
"""
import numpy as np

A = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
B = np.array([[1.0, 0.0],
              [0.0, 1.0],
              [2.0, 1.0]])

# TODO: imprimir as duas verificações e A@B.
