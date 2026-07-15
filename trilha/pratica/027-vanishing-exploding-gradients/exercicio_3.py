"""Licao 027 — Exercicio 3: gradient clipping por norma.

Tarefa:
- Implemente clip_por_norma(g, max_norma): se ||g|| > max_norma, reescale g por
  max_norma/||g||; retorne (g_clipado, norma_original, clipado_bool).
- Com teto = 5.0, aplique a g = [0.3, 0.4] (dentro) e g = [6.0, 8.0] (acima).
- Imprima por linha `g=... norma=... clipado=... norma_final=...` (4 casas).

Criterio binario: saida IDENTICA a
trilha/solucoes/027-vanishing-exploding-gradients/solucao_3.saida.txt
"""
import numpy as np


def clip_por_norma(g, max_norma):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
