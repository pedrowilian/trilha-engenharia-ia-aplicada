"""Solucao de referencia — Licao 016, Exercicio 2.

Varre o grau do polinomio e identifica a complexidade que minimiza o erro de
TESTE (o vale da curva em U), demonstrando o trade-off vies-variancia.
"""
import numpy as np


def f(x):
    return np.sin(1.5 * x)


def main():
    rng = np.random.default_rng(3)
    x_treino = np.linspace(-3, 3, 11)
    x_teste = np.linspace(-3, 3, 200)
    y_treino = f(x_treino) + rng.normal(0, 0.25, size=x_treino.shape)
    y_teste = f(x_teste)

    def mse(a, b):
        return float(np.mean((a - b) ** 2))

    melhor_grau, melhor_te = None, float("inf")
    for grau in range(1, 10):
        coef = np.polyfit(x_treino, y_treino, grau)
        te = mse(np.polyval(coef, x_teste), y_teste)
        if te < melhor_te:
            melhor_te, melhor_grau = te, grau
        print(f"grau={grau}: erro_teste={te:.4f}")
    print(f"melhor grau (menor erro_teste): {melhor_grau}")


if __name__ == "__main__":
    main()
