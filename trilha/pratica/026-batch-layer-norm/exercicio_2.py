"""Licao 026 — Exercicio 2: Batch Norm com gamma e beta.

Tarefa:
- Use X = [[1,100],[3,300],[5,500],[7,700]], gamma = [3.0, 0.5], beta = [5.0, -2.0].
- Implemente batch_norm(X, gamma, beta) = gamma * normaliza(X) + beta, onde
  normaliza usa media/var por coluna (eps=1e-5).
- Imprima a media e o std da saida por feature (4 casas) e confirme com
  np.allclose que media ~= beta e std ~= |gamma| (atol=1e-3).

Criterio binario: saida IDENTICA a
trilha/solucoes/026-batch-layer-norm/solucao_2.saida.txt
"""
import numpy as np


def batch_norm(X, gamma, beta, eps=1e-5):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
