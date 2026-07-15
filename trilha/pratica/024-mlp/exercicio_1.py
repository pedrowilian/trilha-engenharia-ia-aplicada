"""Licao 024 — Exercicio 1: forward pass de um MLP 2-3-1.

Tarefa:
- Use os pesos fixos:
    W1 = [[0.5,-0.5],[1.0,1.0],[-1.0,0.5]], b1 = [0.0,-0.5,0.2]
    W2 = [1.0,-1.0,0.5], b2 = 0.1
  e a entrada x = [1.0, 2.0].
- Calcule a camada oculta h = sigmoid(W1 @ x + b1) e a saida
  y = sigmoid(W2 @ h + b2).
- Imprima as shapes de x e h, h (4 casas) e a saida (4 casas).

Criterio binario: saida IDENTICA a
trilha/solucoes/024-mlp/solucao_1.saida.txt
"""
import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
