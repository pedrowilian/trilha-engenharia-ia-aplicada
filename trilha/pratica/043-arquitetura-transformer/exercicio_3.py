"""Exercício 3 — Bloco de encoder preserva a forma.

Setup (dado):
    rng = np.random.default_rng(55)
    n, d_model, d_ff = 4, 6, 12
    Gere, NESTA ordem: X (n, d_model), Wq, Wk, Wv (d_model, d_model),
    W1 (d_model, d_ff), W2 (d_ff, d_model).
    Use LayerNorm sem parâmetros e self-attention de cabeça única.

Tarefa:
    Monte o bloco: atenção -> residual+norm -> FFN(ReLU) -> residual+norm.
    Imprima:
        - "entrada shape:", X.shape, "-> saida shape:", Y.shape
        - "shape preservado:", X.shape == Y.shape
        - "media por linha (apos norm):", np.round(Y.mean(axis=-1), 4)
        - "Y[0] =", np.round(Y[0], 4)

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/043-arquitetura-transformer/solucao_3.saida.txt
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)

rng = np.random.default_rng(55)
n, d_model, d_ff = 4, 6, 12

# TODO: gerar X, Wq, Wk, Wv, W1, W2 (nesta ordem) e montar o bloco de encoder.
