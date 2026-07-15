"""Licao 018 — Exercicio 3: temperature scaling.

Tarefa:
- Use np.random.default_rng(20), N=8000, p_verdadeira ~ U(0.02,0.98), y ~ Bernoulli.
- logits = 3 * log(p/(1-p)) (superconfiante). Busque T em linspace(1.0, 5.0, 41)
  que minimiza o ECE de sigmoid(logits / T).
- Imprima `ECE com T=1.0: ...`, `melhor T: <T 1 casa>`, `ECE com melhor T: ...`
  (4 casas) e `temperature scaling melhorou: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/018-calibracao/solucao_3.saida.txt
"""
import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def ece(p_pred, y, N, n_bins=10):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
