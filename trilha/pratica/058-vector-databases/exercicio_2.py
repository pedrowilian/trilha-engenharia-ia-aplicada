"""Exercicio 2 - Indice particionado (IVF, nprobe=1).

Setup (dado):
    base de 9 vetores (v1..v9) e 3 centroides (c0, c1, c2); consulta = [4, 6].

Tarefa:
    Atribua cada vetor ao centroide mais proximo (clusters). Na busca, encontre
    o centroide mais proximo da consulta e varra SO os pontos daquele cluster.
    Imprima o centroide probado, o top-1 IVF e o top-1 flat (com distancias de 4
    casas), "comparacoes ivf: <n> | flat: <n>" e "resultados coincidem: <bool>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/058-vector-databases/solucao_2.saida.txt
"""
import numpy as np

base = {
    "v1": [1.0, 1.0], "v2": [2.0, 1.0], "v3": [1.0, 2.0],
    "v4": [5.0, 1.0], "v5": [6.0, 1.0], "v6": [5.0, 2.0],
    "v7": [3.0, 6.0], "v8": [4.0, 6.0], "v9": [3.0, 7.0],
}
centroides = {"c0": [1.0, 1.0], "c1": [5.0, 1.0], "c2": [3.0, 6.0]}
consulta = [4.0, 6.0]

# TODO: construa os clusters, faca a busca IVF (nprobe=1) e compare com o flat.
