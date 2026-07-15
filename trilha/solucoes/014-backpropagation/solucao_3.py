"""Solucao de referencia — Licao 014, Exercicio 3.

Gradient checking de AMBOS os parametros (w e b) de um neuronio sigmoide,
comparando o gradiente analitico com diferencas finitas centrais.
"""
import math


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def perda(w, b, x, y):
    p = sigmoid(w * x + b)
    return -(y * math.log(p) + (1 - y) * math.log(1 - p))


def main():
    x, y = -1.0, 0.0
    w, b = 0.8, -0.2
    p = sigmoid(w * x + b)

    dL_dw_a = (p - y) * x
    dL_db_a = (p - y)

    h = 1e-5
    dL_dw_n = (perda(w + h, b, x, y) - perda(w - h, b, x, y)) / (2 * h)
    dL_db_n = (perda(w, b + h, x, y) - perda(w, b - h, x, y)) / (2 * h)

    ok_w = abs(dL_dw_a - dL_dw_n) < 1e-6
    ok_b = abs(dL_db_a - dL_db_n) < 1e-6
    print(f"w: analitico={dL_dw_a:.6f} numerico={dL_dw_n:.6f}")
    print(f"b: analitico={dL_db_a:.6f} numerico={dL_db_n:.6f}")
    print("gradientes conferem:", ok_w and ok_b)


if __name__ == "__main__":
    main()
