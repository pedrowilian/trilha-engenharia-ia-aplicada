"""Solucao de referencia — Licao 029, Exercicio 2.

Average pooling 2x2: cada bloco vira a MEDIA dos seus valores (suaviza, ao
contrario do max pooling que pega o maior).
"""
import numpy as np


def avg_pool(x, k=2):
    h, w = x.shape
    out = np.zeros((h // k, w // k))
    for i in range(h // k):
        for j in range(w // k):
            out[i, j] = x[i * k:(i + 1) * k, j * k:(j + 1) * k].mean()
    return out


def main():
    x = np.array([[1, 3, 2, 4],
                  [5, 6, 1, 2],
                  [0, 1, 3, 8],
                  [2, 1, 0, 7]], dtype=float)
    saida = avg_pool(x, 2)
    print("avg pool 2x2:\n", saida)
    print("shape:", x.shape, "->", saida.shape)


if __name__ == "__main__":
    main()
