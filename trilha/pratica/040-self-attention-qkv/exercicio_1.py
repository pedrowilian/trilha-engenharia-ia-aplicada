"""Exercício 1 — Atenção do zero (função reutilizável).

Setup (dado):
    X  = embeddings de 4 tokens, d_model = 4
    Wq, Wk, Wv = projeções 4 x 2 (d_k = 2)

Tarefa:
    Implemente softmax(x, axis=-1) estável e
    self_attention(X, Wq, Wk, Wv) -> (saida, pesos), onde
        Q,K,V = X@Wq, X@Wk, X@Wv
        pesos = softmax(Q @ K.T / sqrt(d_k))
        saida = pesos @ V
    Imprima np.round(pesos, 4) e pesos.argmax(axis=1).tolist().

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/040-self-attention-qkv/solucao_1.saida.txt
"""
import numpy as np

X = np.array([
    [2.0, 0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0, 2.0],
    [1.0, 1.0, 1.0, 0.0],
    [0.0, 2.0, 1.0, 1.0],
])
Wq = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 0.0], [0.0, 1.0]])
Wk = np.array([[0.0, 1.0], [1.0, 0.0], [0.0, 1.0], [1.0, 0.0]])
Wv = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.0, 1.0]])

# TODO: implementar softmax e self_attention; imprimir pesos e argmax por linha.
