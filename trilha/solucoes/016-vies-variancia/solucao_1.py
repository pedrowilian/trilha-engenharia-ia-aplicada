"""Solucao de referencia — Licao 016, Exercicio 1.

Estima vies^2 e variancia empiricos em um ponto de teste para um modelo
simples (alto vies) e um flexivel (alta variancia).
"""
import numpy as np


def f(x):
    return 0.5 * x ** 2


def bias_var(grau, rng, x_treino, x0, sigma, M):
    preds = []
    for _ in range(M):
        y = f(x_treino) + rng.normal(0, sigma, size=x_treino.shape)
        coef = np.polyfit(x_treino, y, grau)
        preds.append(np.polyval(coef, x0))
    preds = np.array(preds)
    return (preds.mean() - f(x0)) ** 2, preds.var()


def main():
    rng = np.random.default_rng(10)
    x_treino = np.linspace(-3, 3, 15)
    x0, sigma, M = 2.0, 1.0, 2000
    b0, v0 = bias_var(0, rng, x_treino, x0, sigma, M)
    b3, v3 = bias_var(3, rng, x_treino, x0, sigma, M)
    print(f"grau 0: vies^2={b0:.4f} variancia={v0:.4f}")
    print(f"grau 3: vies^2={b3:.4f} variancia={v3:.4f}")
    print("grau 0 tem mais vies:", b0 > b3)
    print("grau 3 tem mais variancia:", v3 > v0)


if __name__ == "__main__":
    main()
