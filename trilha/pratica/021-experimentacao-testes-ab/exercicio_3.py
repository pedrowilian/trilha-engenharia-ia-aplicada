"""Licao 021 — Exercicio 3: peeking infla o falso-positivo.

Tarefa:
- Use np.random.default_rng(4). Simule 1000 testes A/A (p_real=0.15 nos DOIS
  grupos), n_max=2400, checkpoints range(300, n_max+1, 300).
- Para cada experimento: conte como falso-positivo "peeking" se algum checkpoint
  der p<0.05; e como falso-positivo "final" se o teste no n_max der p<0.05.
- Imprima `falso-positivo so no fim: ...`, `falso-positivo com peeking: ...`
  (3 casas) e `peeking infla o falso-positivo: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/021-experimentacao-testes-ab/solucao_3.saida.txt
"""
import math
import numpy as np


def phi(z):
    raise NotImplementedError


def z_test(x1, n1, x2, n2):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
