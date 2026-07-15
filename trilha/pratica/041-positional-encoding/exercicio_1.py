"""Exercício 1 — Construir e inspecionar a matriz de positional encoding.

Setup (dado):
    positional_encoding(n_pos, d, base=10000.0) seguindo a fórmula sinusoidal:
        PE[pos, 2i]   = sin(pos / base**(2i/d))
        PE[pos, 2i+1] = cos(pos / base**(2i/d))
    com n_pos = 6 e d = 8.

Tarefa:
    Construa a matriz PE e imprima:
        - pe.shape
        - o mínimo e o máximo (4 casas)
        - np.round(pe[1], 4)

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/041-positional-encoding/solucao_1.saida.txt
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)

# TODO: implementar positional_encoding(n_pos, d) e imprimir shape, min/max e pe[1].
