"""Licao 022 — Exercicio 3: o perceptron nao resolve o XOR.

Tarefa:
- Use X = [[0,0],[0,1],[1,0],[1,1]] e y = [0,1,1,0] (XOR).
- Treine por 100 epocas (w=zeros(2), b=0.0, eta=1.0) e, a cada epoca, calcule
  a acuracia (numero de acertos em 4); guarde a MELHOR acuracia vista.
- Imprima a melhor acuracia e se o perceptron resolveu o XOR (melhor == 4).

Criterio binario: saida IDENTICA a
trilha/solucoes/022-perceptron/solucao_3.saida.txt
"""
import numpy as np


def degrau(z):
    return 1 if z >= 0.0 else 0


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
