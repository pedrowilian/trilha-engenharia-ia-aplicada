"""Licao 023 — Exercicio 2: esparsidade da ReLU.

Tarefa:
- Use o vetor z = [-3, -1, -0.2, 0, 0.7, 1.5, 4].
- Aplique ReLU e conte quantos neuronios ficam ativos (saida > 0) e
  desligados (saida == 0); calcule a ativacao media.
- Imprima a entrada, a saida da ReLU, a contagem de ativos/desligados e a
  ativacao media (4 casas).

Criterio binario: saida IDENTICA a
trilha/solucoes/023-funcoes-de-ativacao/solucao_2.saida.txt
"""
import numpy as np


def relu(z):
    return np.maximum(0.0, z)


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
