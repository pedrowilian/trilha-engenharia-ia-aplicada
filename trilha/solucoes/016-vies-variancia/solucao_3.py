"""Solucao de referencia — Licao 016, Exercicio 3.

Mostra que MAIS DADOS reduzem a variancia de um modelo flexivel (grau 4) sem
mudar o vies: a variancia no ponto de teste cai conforme n cresce.
"""
import numpy as np


def f(x):
    return 0.5 * x ** 2


def variancia_no_ponto(n, rng, x0, sigma, M, grau=4):
    x_treino = np.linspace(-3, 3, n)
    preds = []
    for _ in range(M):
        y = f(x_treino) + rng.normal(0, sigma, size=x_treino.shape)
        coef = np.polyfit(x_treino, y, grau)
        preds.append(np.polyval(coef, x0))
    return float(np.var(preds))


def main():
    rng = np.random.default_rng(5)
    x0, sigma, M = 1.5, 1.0, 1500
    variancias = []
    for n in [10, 40, 160]:
        v = variancia_no_ponto(n, rng, x0, sigma, M)
        variancias.append(v)
        print(f"n={n:>3}: variancia={v:.4f}")
    decresce = all(variancias[i] > variancias[i + 1] for i in range(len(variancias) - 1))
    print("variancia cai com mais dados:", decresce)


if __name__ == "__main__":
    main()
