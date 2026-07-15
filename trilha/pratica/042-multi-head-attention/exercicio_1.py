"""Exercício 1 — split_heads e merge_heads (ida e volta).

Setup (dado):
    X = np.arange(24.0).reshape(4, 6)
    h em {1, 2, 3}

Tarefa:
    Implemente:
        split_heads(M, h) -> tensor (h, n, d_k), com d_k = d_model // h
        merge_heads(ctx)  -> matriz (n, d_model)   (inverso de split_heads)
    Para cada h, imprima o shape das cabeças e
        np.array_equal(merge_heads(split_heads(X, h)), X)

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/042-multi-head-attention/solucao_1.saida.txt
"""
import numpy as np

X = np.arange(24.0).reshape(4, 6)

# TODO: implementar split_heads e merge_heads; checar o round-trip para h em {1,2,3}.
