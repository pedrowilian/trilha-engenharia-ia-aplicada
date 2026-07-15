"""Exercício 1 — Lição 004: Verificar a equação de autovalores.

Tarefa:
  1. Dada a matriz simétrica B = [[4, 1], [1, 4]], calcule seus autovalores e
     autovetores (dica: use numpy.linalg.eigh, próprio para matrizes simétricas).
  2. Imprima os autovalores arredondados a 4 casas: f"Autovalores: {...}".
  3. Confirme as identidades:
       traço(B) == soma dos autovalores
       det(B)   == produto dos autovalores
     imprimindo: f"Traco={...:.4f} soma={...:.4f}"
                 f"Det={...:.4f} produto={...:.4f}"
  4. Calcule o resíduo máximo ||B·v - λ·v|| sobre todos os autopares e imprima
     f"residuo maximo: {...:.6f}".
  5. Imprima "OK" se traço≈soma e resíduo≈0; senão "FALHOU".

Critério de conclusão (binário): a saída deve ser EXATAMENTE igual a
  trilha/solucoes/004-autovalores-autovetores-svd-pca/solucao_1.saida.txt
"""
import numpy as np

B = np.array([[4.0, 1.0],
              [1.0, 4.0]])

# TODO: implemente os passos 1 a 5.
