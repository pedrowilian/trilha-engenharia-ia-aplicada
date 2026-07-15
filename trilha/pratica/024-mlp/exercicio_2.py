"""Licao 024 — Exercicio 2: o MLP resolve o XOR.

Tarefa:
- Use a rede com camada oculta ReLU e pesos a mao:
    W1 = [[1,1],[1,1]], b1 = [0,-1], W2 = [1,-2], b2 = 0.
- Para as 4 entradas do XOR (alvo [0,1,1,0]), calcule
  classe = int(W2 @ relu(W1 @ x + b1) + b2 >= 0.5) e conte os acertos.
- Imprima, por linha, `x=... classe=... alvo=...` e ao final
  `acertos=.../4 resolveu o XOR: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/024-mlp/solucao_2.saida.txt
"""
import numpy as np


def relu(z):
    return np.maximum(0.0, z)


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
