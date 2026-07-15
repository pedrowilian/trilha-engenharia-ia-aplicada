"""Exercicio 2 - Complementaridade denso x esparso.

Setup (dado):
    corpus com texto (para BM25) e emb (para denso); consulta_texto = "reembolso",
    consulta_emb = [1.0, 0.0].

Tarefa:
    Calcule o ranking denso (cosseno entre consulta_emb e cada emb) e o ranking
    esparso (BM25 sobre os textos), cada um ordenado por (-score, id). Imprima
    "ranking denso: <ids>", "ranking esparso: <ids>" e
    "top-1 denso: <id> | top-1 esparso: <id>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/059-rag-hibrido/solucao_2.saida.txt
"""
import collections
import math
import re

import numpy as np

corpus = {
    "d1": {"texto": "politica de reembolso", "emb": [0.8, 0.6]},
    "d2": {"texto": "devolucao do valor", "emb": [1.0, 0.0]},
    "d3": {"texto": "horario de atendimento", "emb": [0.0, 1.0]},
}
consulta_texto = "reembolso"
consulta_emb = [1.0, 0.0]

# TODO: produza os rankings denso (cosseno) e esparso (BM25) e mostre o top-1 de cada.
