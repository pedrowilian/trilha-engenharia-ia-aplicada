"""Licao 020 — Exercicio 1: target leakage.

Tarefa:
- Use np.random.default_rng(10), N=500, y ~ Bernoulli(0.5).
- x_legit = 0.4*(2y-1) + N(0,1); x_leaky = (2y-1) + N(0,0.03).
- Classificador trivial: prediz 1 se x>=0. Calcule a acuracia de cada feature.
- Imprima `acuracia feature legitima: ...`, `acuracia feature vazada: ...` (3 casas)
  e `suspeita de leakage: <bool>` (acc_leaky>0.95 e diferenca>0.2).

Criterio binario: saida IDENTICA a
trilha/solucoes/020-data-leakage/solucao_1.saida.txt
"""
import numpy as np


def acuracia_threshold(x, y):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
