"""Exercício 2 — Somar o positional encoding aos embeddings.

Setup (dado):
    e  = np.array([1.0, 0.0, 0.0, 0.0])   # embedding fixo de um token
    pe = positional_encoding(4, 4)

Tarefa:
    Some `e` ao encoding das posições 0 e 2 e imprima:
        - rep0 = e + pe[0]  (np.round(..., 4))
        - rep2 = e + pe[2]  (np.round(..., 4))
        - not np.allclose(rep0, rep2)   # mesmo token, posições diferentes

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/041-positional-encoding/solucao_2.saida.txt
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)

e = np.array([1.0, 0.0, 0.0, 0.0])

# TODO: implementar positional_encoding(4, 4), somar a `e` nas posições 0 e 2.
