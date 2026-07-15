"""Solucao de referencia — Licao 031, Exercicio 3.

O valor das features pre-treinadas: treinar a MESMA cabeca linear sobre features
uteis (que carregam sinal da classe) da alta acuracia; sobre features aleatorias
(sem sinal) fica perto do acaso.
"""
import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def treinar(feats, y, eta=0.1, passos=300):
    w = np.zeros(feats.shape[1])
    b = 0.0
    for _ in range(passos):
        p = sigmoid(feats @ w + b)
        g = p - y
        w -= eta * (feats.T @ g) / len(y)
        b -= eta * g.mean()
    return ((sigmoid(feats @ w + b) >= 0.5).astype(float) == y).mean()


def main():
    rng = np.random.default_rng(2)
    N = 200
    y = (rng.uniform(size=N) < 0.5).astype(float)
    uteis = rng.standard_normal((N, 8)) + y[:, None] * 1.5   # carregam sinal
    aleatorias = rng.standard_normal((N, 8))                 # sem sinal
    print(f"acuracia com features uteis (pre-treinadas): {treinar(uteis, y):.4f}")
    print(f"acuracia com features aleatorias:            {treinar(aleatorias, y):.4f}")


if __name__ == "__main__":
    main()
