"""Exercício 2 — Coeficientes de uma combinação linear.

Setup:
    u1 = [1.0, 2.0]
    u2 = [3.0, 1.0]
    alvo = [5.0, 5.0]

Tarefa:
    1. Monte a matriz A cujas colunas são u1 e u2.
    2. Resolva A @ coef = alvo para encontrar os coeficientes da combinação.
    3. Reconstrua o alvo como coef[0]*u1 + coef[1]*u2.
    4. Imprima (valores arredondados a 4 casas, via .tolist()):
        coeficientes: [2.0, 1.0]
        reconstrucao: [5.0, 5.0]

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/001-vetores-e-espacos-vetoriais/solucao_2.saida.txt
"""
import numpy as np

u1 = np.array([1.0, 2.0])
u2 = np.array([3.0, 1.0])
alvo = np.array([5.0, 5.0])

# TODO: montar A com np.column_stack, resolver com np.linalg.solve e imprimir.
