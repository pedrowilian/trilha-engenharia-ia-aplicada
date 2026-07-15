"""Exercício 2 — Lição 004: Aproximação de baixo posto via SVD.

Tarefa:
  1. Para a matriz C = diag(3, 2, 1) (3x3), calcule a SVD
     (numpy.linalg.svd com full_matrices=False).
  2. Imprima os valores singulares arredondados a 4 casas:
     f"Valores singulares: {...}".
  3. Para k = 1, 2, 3, reconstrua a aproximação de posto k usando apenas os
     k maiores valores/vetores singulares e imprima:
       f"rank-{k}: erro={erro_frobenius:.4f} energia={energia_percentual:.1f}%"
     onde energia = soma dos k maiores sigma^2 / soma de todos os sigma^2.

Critério de conclusão (binário): a saída deve ser EXATAMENTE igual a
  trilha/solucoes/004-autovalores-autovetores-svd-pca/solucao_2.saida.txt
"""
import numpy as np

C = np.array([[3.0, 0.0, 0.0],
              [0.0, 2.0, 0.0],
              [0.0, 0.0, 1.0]])

# TODO: implemente os passos 1 a 3.
