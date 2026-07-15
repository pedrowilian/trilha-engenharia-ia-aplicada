"""Exercício 3 — Inversa e resolução de sistema linear.

Setup:
    A = [[4.0, 3.0], [6.0, 3.0]]
    b = [10.0, 12.0]

Tarefa:
    1. Calcule A_inv com np.linalg.inv.
    2. Confirme A @ A_inv == identidade (some + 0.0 após np.round para evitar -0.0).
    3. Resolva x = A_inv @ b.
    4. Saída esperada (valores arredondados a 4 casas):
        inversa: [[-0.5, 0.5], [1.0, -0.6667]]
        A@A_inv: [[1.0, 0.0], [0.0, 1.0]]
        x: [1.0, 2.0]

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/002-matrizes-e-operacoes/solucao_3.saida.txt
"""
import numpy as np

A = np.array([[4.0, 3.0],
              [6.0, 3.0]])
b = np.array([10.0, 12.0])

# TODO: calcular a inversa, verificar a identidade e resolver o sistema.
