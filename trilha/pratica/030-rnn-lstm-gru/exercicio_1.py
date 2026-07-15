"""Licao 030 — Exercicio 1: forward de uma RNN escalar.

Tarefa:
- Use Wx=0.6, Wh=0.8, b=0.1, h inicial = 0.0 e a sequencia [1.0, 0.0, -1.0, 0.5].
- A cada passo calcule h = tanh(Wx*x + Wh*h + b).
- Imprima por linha `t=... x=... h=...` (h com 4 casas).

Criterio binario: saida IDENTICA a
trilha/solucoes/030-rnn-lstm-gru/solucao_1.saida.txt
"""
import numpy as np


def rnn_step(x, h, Wx, Wh, b):
    return np.tanh(Wx * x + Wh * h + b)


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
