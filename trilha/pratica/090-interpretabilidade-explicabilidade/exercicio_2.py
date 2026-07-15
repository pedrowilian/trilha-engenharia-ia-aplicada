"""Exercício 2 — Importância por permutação.

Setup (use exatamente estas sementes/parâmetros para reproduzir a saída):
    rng = np.random.default_rng(42)
    n = 300
    X = rng.normal(size=(n, 3))
    y = 2.0 * X[:, 0] - 1.0 * X[:, 2] + rng.normal(scale=0.1, size=n)
    w = np.array([2.0, 0.0, -1.0])

Tarefa:
    Defina `mse(Xm)` = média de `(Xm @ w - y) ** 2`. Imprima `"mse base: {base:.3f}"`.
    Para cada coluna j em 0..2, copie X, embaralhe a coluna j com
    `rng.permutation(X[:, j])` e imprima
    `"feature x{j}: importancia={mse(Xp) - base:.3f}"`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/090-interpretabilidade-explicabilidade/solucao_2.saida.txt
"""
import numpy as np

# TODO: gere os dados com a semente dada, calcule o MSE base e a importância
#       por permutação de cada feature.
