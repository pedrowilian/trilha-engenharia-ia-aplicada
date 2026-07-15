"""Solucao de referencia — Licao 017, Exercicio 2.

Validacao cruzada k-fold (k=5) do zero para selecionar o grau do polinomio
com menor erro medio de validacao.
"""
import numpy as np


def f(x):
    return np.sin(1.2 * x)


def main():
    rng = np.random.default_rng(42)
    X = np.linspace(-3, 3, 40)
    y = f(X) + rng.normal(0, 0.3, size=X.shape)

    def cv_erro(grau, k=5):
        folds = np.array_split(np.arange(len(X)), k)
        erros = []
        for i in range(k):
            val_idx = folds[i]
            tr_idx = np.concatenate([folds[j] for j in range(k) if j != i])
            coef = np.polyfit(X[tr_idx], y[tr_idx], grau)
            pred = np.polyval(coef, X[val_idx])
            erros.append(np.mean((pred - y[val_idx]) ** 2))
        return float(np.mean(erros))

    melhor_grau, melhor_erro = None, float("inf")
    for grau in [1, 2, 3, 4, 5]:
        e = cv_erro(grau)
        if e < melhor_erro:
            melhor_erro, melhor_grau = e, grau
        print(f"grau={grau}: erro_cv={e:.4f}")
    print(f"melhor grau (k-fold): {melhor_grau}")


if __name__ == "__main__":
    main()
