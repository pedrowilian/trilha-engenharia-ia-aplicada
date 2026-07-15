"""Licao 018 — Exercicio 1: tabela de confiabilidade (reliability).

Tarefa:
- Use np.random.default_rng(3), N=6000, p_verdadeira ~ U(0.02, 0.98),
  y ~ Bernoulli(p_verdadeira).
- Modelo superconfiante: p_pred = sigmoid(2 * log(p/(1-p))).
- Agrupe p_pred em 5 faixas (linspace(0,1,6), digitize-1, clip 0..4) e imprima
  `faixa | prob_media | freq_positivos` (3 casas) por faixa.

Criterio binario: saida IDENTICA a
trilha/solucoes/018-calibracao/solucao_1.saida.txt
"""
import numpy as np


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
