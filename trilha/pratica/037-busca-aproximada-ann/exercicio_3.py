"""Exercício 3 — Varrer o trade-off recall × latência.

Setup:
    base com a*, b*, c* (9 vetores 2D do esqueleto)
    centroides = {"A": [0.5, 0.5], "B": [3.5, 3.5], "C": [0.5, 8.0]}
    q = [2.0, 2.0]

Tarefa:
    Implemente busca_ivf(q, k, nprobe) contando comparações (proxy de latência)
    e varra nprobe em {1, 2, 3}, imprimindo comparações e recall@3 de cada.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/037-busca-aproximada-ann/solucao_3.saida.txt
    (recall sobe de 0.6667 para 1.0000; comparações de 3 a 9).
"""
import math

base = {
    "a0": [0.0, 0.0], "a1": [0.5, 0.5], "a2": [1.0, 1.0],
    "b0": [4.0, 4.0], "b1": [3.5, 3.5], "b2": [3.0, 3.0],
    "c0": [0.0, 8.0], "c1": [0.5, 8.0], "c2": [1.0, 8.0],
}
centroides = {"A": [0.5, 0.5], "B": [3.5, 3.5], "C": [0.5, 8.0]}
q = [2.0, 2.0]

# TODO: montar IVF, implementar busca_ivf com contagem e varrer nprobe.
