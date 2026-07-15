"""Solucao de referencia — Licao 015, Exercicio 1.

Regressao ridge (L2) por solucao fechada; mostra que a norma dos pesos cai
monotonamente conforme lambda aumenta.
"""
import numpy as np


def ridge(X, y, lam):
    A = X.T @ X + lam * np.eye(X.shape[1])
    return np.linalg.solve(A, X.T @ y)


def main():
    X = np.array([[1.0, 4.0],
                  [1.0, 2.0],
                  [1.0, 6.0],
                  [1.0, 8.0],
                  [1.0, 10.0]])
    y = np.array([9.0, 5.0, 13.0, 17.0, 21.0])
    normas = []
    for lam in [0.0, 5.0, 50.0]:
        w = ridge(X, y, lam)
        normas.append(np.linalg.norm(w))
        print(f"lambda={lam:>5}: w=[{w[0]:.4f}, {w[1]:.4f}] norma_L2={np.linalg.norm(w):.4f}")
    decrescente = all(normas[i] > normas[i + 1] for i in range(len(normas) - 1))
    print("norma decresce com lambda:", decrescente)


if __name__ == "__main__":
    main()
