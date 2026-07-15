"""Exercício 2 — Filtragem top-k.

Setup: os `logits` do próximo token e o `k`, abaixo.

Tarefa:
    Calcule a softmax, selecione os `k` índices de maior probabilidade, zere os
    demais e renormalize. Imprima `p original` (lista, 4 casas), `top-k indices`
    (ordenados) e `p top-k` (lista, 4 casas).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/049-sampling-decodificacao/solucao_2.saida.txt
"""
import numpy as np

logits = np.array([2.0, 1.0, 0.5, 0.0, -1.0])
k = 3

# TODO: calcular a softmax, aplicar top-k, renormalizar e imprimir.
