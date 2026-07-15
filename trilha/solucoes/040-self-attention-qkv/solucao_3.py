"""Solução de referência — Exercício 3 da Lição 040.

A saída da atenção é uma combinação convexa das linhas de V: como os pesos são
não negativos e somam 1, o resultado fica dentro do envoltório convexo de V.
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)

V = np.array([[0.0, 10.0], [2.0, 8.0], [5.0, 5.0], [9.0, 1.0]])
pesos = np.array([0.1, 0.2, 0.3, 0.4])

saida = pesos @ V
print("soma dos pesos:", round(float(pesos.sum()), 4))
print("saida (media ponderada):", np.round(saida, 4))

dentro = (np.all(saida >= V.min(axis=0) - 1e-9)
          and np.all(saida <= V.max(axis=0) + 1e-9))
print("dentro do envoltorio convexo de V:", bool(dentro))
