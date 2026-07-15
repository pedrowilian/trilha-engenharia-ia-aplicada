"""Solucao de referencia — Licao 022, Exercicio 1.

Treina um perceptron com a regra de aprendizado para a porta OR.
OR e linearmente separavel, entao o perceptron converge.
"""
import numpy as np


def degrau(z):
    return 1 if z >= 0.0 else 0


def main():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
    y = np.array([0, 1, 1, 1])      # porta OR
    w = np.zeros(2)
    b = 0.0
    eta = 1.0
    epoca_convergencia = None
    for epoca in range(20):
        erros = 0
        for xi, alvo in zip(X, y):
            pred = degrau(np.dot(w, xi) + b)
            erro = alvo - pred
            if erro != 0:
                w = w + eta * erro * xi
                b = b + eta * erro
                erros += 1
        if erros == 0:
            epoca_convergencia = epoca
            break
    preds = [degrau(np.dot(w, xi) + b) for xi in X]
    print(f"convergiu na epoca: {epoca_convergencia}")
    print(f"w={w} b={b}")
    print(f"predicoes={preds} alvo={[int(v) for v in y]}")
    print(f"todos corretos: {preds == [int(v) for v in y]}")


if __name__ == "__main__":
    main()
