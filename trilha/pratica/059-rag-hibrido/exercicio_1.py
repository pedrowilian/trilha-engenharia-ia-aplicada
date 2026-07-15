"""Exercicio 1 - Recuperacao esparsa com BM25.

Setup (dado):
    corpus = {
        "d1": "o gato preto dorme",
        "d2": "o cachorro corre no parque",
        "d3": "o gato e o cachorro brincam",
    }
    query = "gato cachorro"

Tarefa:
    Implemente o BM25 (k1=1.5, b=0.75): IDF(t) = ln(1 + (N - n_t + 0.5)/(n_t + 0.5)),
    e score(D) = soma_t IDF(t) * (f*(k1+1)) / (f + k1*(1 - b + b*dl/avgdl)).
    Imprima "<id> <score 4 casas>" para cada documento em ordem de id.

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/059-rag-hibrido/solucao_1.saida.txt
"""
import collections
import math
import re

corpus = {
    "d1": "o gato preto dorme",
    "d2": "o cachorro corre no parque",
    "d3": "o gato e o cachorro brincam",
}
query = "gato cachorro"

# TODO: implemente idf e bm25 (k1=1.5, b=0.75) e imprima o score de cada doc.
