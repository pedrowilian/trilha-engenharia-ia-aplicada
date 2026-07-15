"""Licao 018 — Exercicio 2: Expected Calibration Error (ECE).

Tarefa:
- Implemente `ece(p_pred, y, N, n_bins=10)` = soma ponderada por faixa de
  |prob_media - freq_positivos|.
- Use np.random.default_rng(11), N=6000, p_verdadeira ~ U(0.02,0.98), y ~ Bernoulli.
- Compare p_calibrado = p_verdadeira e p_super = sigmoid(2.5*log(p/(1-p))).
- Imprima `ECE calibrado: ...`, `ECE superconfiante: ...` (4 casas) e
  `calibrado tem ECE menor: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/018-calibracao/solucao_2.saida.txt
"""
import numpy as np


def ece(p_pred, y, N, n_bins=10):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
