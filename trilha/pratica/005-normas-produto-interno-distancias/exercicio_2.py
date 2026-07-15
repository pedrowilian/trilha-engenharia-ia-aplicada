"""Exercício 2 — Ranking por cosseno vs. por distância L2.

Setup:
    q = [1.0, 1.0]
    docs = {"A": [10.0, 10.0], "B": [1.0, 0.0], "C": [0.0, 2.0]}

Tarefa:
    1. Implemente cos_sim(u, v) e l2(u, v).
    2. Ordene os documentos por cosseno (decrescente) e por L2 (crescente).
    3. Imprima cada ranking e, na última linha, exatamente:
        top cosseno=A top L2=B

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/005-normas-produto-interno-distancias/solucao_2.saida.txt
"""
import math

q = [1.0, 1.0]
docs = {
    "A": [10.0, 10.0],
    "B": [1.0, 0.0],
    "C": [0.0, 2.0],
}


def cos_sim(u, v):
    # TODO: produto interno dividido pelo produto das normas L2
    raise NotImplementedError


def l2(u, v):
    # TODO: raiz da soma dos quadrados das diferenças
    raise NotImplementedError


# TODO: ordenar por cada critério, imprimir os rankings e o top de cada um.
