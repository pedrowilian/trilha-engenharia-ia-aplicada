"""Solucao de referencia — Licao 030, Exercicio 1.

Forward de uma RNN escalar sobre uma sequencia: h_t = tanh(Wx*x + Wh*h + b).
"""
import numpy as np


def rnn_step(x, h, Wx, Wh, b):
    return np.tanh(Wx * x + Wh * h + b)


def main():
    Wx, Wh, b = 0.6, 0.8, 0.1
    h = 0.0
    seq = [1.0, 0.0, -1.0, 0.5]
    for t, x in enumerate(seq):
        h = rnn_step(x, h, Wx, Wh, b)
        print(f"t={t} x={x:+.1f} h={h:+.4f}")


if __name__ == "__main__":
    main()
