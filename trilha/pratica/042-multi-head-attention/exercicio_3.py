"""Exercício 3 — Cabeças se especializam.

Setup (dado):
    rng = np.random.default_rng(0)
    n, d_model, h = 6, 8, 4
    d_k = d_model // h
    X = rng.normal(0, 1, size=(n, d_model))
    Para cada cabeça (em ordem), gere Wq e Wk com forma (d_model, d_k).

Tarefa:
    Para cada cabeça, calcule a matriz de atenção
        P = softmax((X@Wq) @ (X@Wk).T / sqrt(d_k))
    e imprima "cabeca c: posicao mais atendida por linha = ..." (P.argmax(axis=1).tolist()).
    Ao final, imprima "todas as cabecas iguais:" com o booleano correspondente.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/042-multi-head-attention/solucao_3.saida.txt
"""
import numpy as np

rng = np.random.default_rng(0)
n, d_model, h = 6, 8, 4
d_k = d_model // h
X = rng.normal(0, 1, size=(n, d_model))

# TODO: para cada cabeça, gerar Wq, Wk e calcular o argmax por linha da atenção.
