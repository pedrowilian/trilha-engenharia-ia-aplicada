"""Solucao de referencia — Licao 017, Exercicio 3.

Curva de aprendizado: conforme o tamanho do treino cresce, a lacuna entre erro
de validacao e erro de treino encolhe.
"""
import numpy as np


def f(x):
    return 0.5 * x ** 2


def main():
    rng = np.random.default_rng(7)
    X_full = np.linspace(-4, 4, 100)
    y_full = f(X_full) + rng.normal(0, 1.0, size=X_full.shape)
    val_idx = np.arange(0, 100, 5)
    tr_pool = np.array([i for i in range(100) if i not in set(val_idx)])
    rng.shuffle(tr_pool)
    Xv, yv = X_full[val_idx], y_full[val_idx]

    def mse(a, b):
        return float(np.mean((a - b) ** 2))

    lacunas = []
    for n in [6, 20, 80]:
        sub = tr_pool[:n]
        coef = np.polyfit(X_full[sub], y_full[sub], 2)
        e_tr = mse(np.polyval(coef, X_full[sub]), y_full[sub])
        e_val = mse(np.polyval(coef, Xv), yv)
        lacunas.append(e_val - e_tr)
        print(f"n_treino={n:>2}: erro_treino={e_tr:.4f} erro_val={e_val:.4f} lacuna={e_val - e_tr:.4f}")
    print("lacuna encolhe com mais dados:", lacunas[0] > lacunas[-1])


if __name__ == "__main__":
    main()
