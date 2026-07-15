"""Solução de referência — Exercício 2 da Lição 090.

Importância por permutação: mede o aumento do erro (MSE) ao embaralhar cada
feature, quebrando sua relação com o alvo. Semente fixa => resultado reprodutível.
"""
import numpy as np

rng = np.random.default_rng(42)
n = 300
X = rng.normal(size=(n, 3))
y = 2.0 * X[:, 0] - 1.0 * X[:, 2] + rng.normal(scale=0.1, size=n)
w = np.array([2.0, 0.0, -1.0])


def mse(Xm):
    pred = Xm @ w
    return float(np.mean((pred - y) ** 2))


base = mse(X)
print(f"mse base: {base:.3f}")
for j in range(3):
    Xp = X.copy()
    Xp[:, j] = rng.permutation(X[:, j])
    print(f"feature x{j}: importancia={mse(Xp) - base:.3f}")
