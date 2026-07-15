"""Solucao de referencia — Licao 029, Exercicio 1.

Convolucao 2D com um detector de borda HORIZONTAL sobre uma imagem dividida em
metade superior (1) e inferior (0). A borda aparece como ativacao forte.
"""
import numpy as np


def conv2d(img, kernel):
    kh, kw = kernel.shape
    h, w = img.shape
    out = np.zeros((h - kh + 1, w - kw + 1))
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            out[i, j] = np.sum(img[i:i + kh, j:j + kw] * kernel)
    return out


def main():
    img = np.array([[1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]], dtype=float)
    kernel = np.array([[1, 1, 1],
                       [0, 0, 0],
                       [-1, -1, -1]], dtype=float)
    saida = conv2d(img, kernel)
    print("shape:", img.shape, "->", saida.shape)
    print("mapa de ativacao:\n", saida)


if __name__ == "__main__":
    main()
