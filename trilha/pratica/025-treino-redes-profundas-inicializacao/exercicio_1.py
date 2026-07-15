"""Licao 025 — Exercicio 1: inicializacao aleatoria quebra a simetria.

Tarefa:
- Use rng = np.random.default_rng(7), x = [1,2,3], W1 = rng.standard_normal((4,3))*0.5,
  b1 = zeros(4), ativacao sigmoid.
- Calcule h = sigmoid(W1 @ x + b1), dh = h*(1-h) e dW1 = outer(dh, x).
- Verifique se as linhas de dW1 sao identicas (simetria) e imprima h (4 casas),
  `linhas de dW1 identicas: <bool>` e `simetria quebrada: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/025-treino-redes-profundas-inicializacao/solucao_1.saida.txt
"""
import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
