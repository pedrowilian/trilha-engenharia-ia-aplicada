"""Exercício 3 — Lição 004: PCA e número de componentes.

Tarefa:
  1. Dado o conjunto de dados X (4 pontos em 3D) abaixo, centralize os dados
     subtraindo a média de cada coluna.
  2. Calcule a matriz de covariância: cov = (Xc.T @ Xc) / (n - 1).
  3. Obtenha as variâncias por componente principal (autovalores de cov),
     ordene-as em ordem decrescente e remova ruído numérico negativo
     (numpy.clip(valores, 0.0, None)).
  4. Imprima a razão de variância explicada (cada autovalor / soma) a 4 casas:
       f"Razao de variancia explicada: {...}"
     e a variância acumulada (numpy.cumsum) a 4 casas:
       f"Variancia acumulada: {...}"
  5. Determine o menor número k de componentes cuja variância acumulada é
     >= 90% e imprima f"Componentes para >=90% da variancia: {k}".

Critério de conclusão (binário): a saída deve ser EXATAMENTE igual a
  trilha/solucoes/004-autovalores-autovetores-svd-pca/solucao_3.saida.txt
"""
import numpy as np

X = np.array([
    [2.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [-2.0, 0.0, 0.0],
    [0.0, -1.0, 0.0],
])

# TODO: implemente os passos 1 a 5.
