"""Exercício 2 — IVF com nprobe=1 vs k-NN exato.

Setup:
    base com a0..a2 e b0..b2 (vetores 2D do esqueleto)
    centroides = {"A": [0.5, 0.5], "B": [3.5, 3.5]}
    q = [2.0, 2.0]

Tarefa:
    Construa o inverted file (listas de pontos por cluster), implemente
    busca_exata(q, k) e busca_ivf(q, k, nprobe) e compare o top-3 exato com o
    aproximado de nprobe=1, imprimindo o recall@3.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/037-busca-aproximada-ann/solucao_2.saida.txt
"""
import math

base = {
    "a0": [0.0, 0.0], "a1": [0.5, 0.5], "a2": [1.0, 1.0],
    "b0": [4.0, 4.0], "b1": [3.5, 3.5], "b2": [3.0, 3.0],
}
centroides = {"A": [0.5, 0.5], "B": [3.5, 3.5]}
q = [2.0, 2.0]

# TODO: montar listas (IVF), implementar busca_exata e busca_ivf e medir recall.
