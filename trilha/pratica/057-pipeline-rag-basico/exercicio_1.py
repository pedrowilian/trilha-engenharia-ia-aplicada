"""Exercicio 1 - Similaridade do cosseno entre consulta e documentos.

Setup (dado):
    corpus = {
        "d1": "gato e cachorro sao animais domesticos",
        "d2": "python e uma linguagem de programacao",
        "d3": "cachorro late e o gato mia",
    }
    pergunta = "o gato e o cachorro"

Tarefa:
    Construa o vocabulario ordenado do corpus, implemente vetorizar(texto)
    (bag-of-words sobre o vocabulario) e cosseno(a, b). Imprima, para cada
    documento em ordem de id, "<id> <cosseno com 4 casas>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/057-pipeline-rag-basico/solucao_1.saida.txt
"""
import re

import numpy as np

corpus = {
    "d1": "gato e cachorro sao animais domesticos",
    "d2": "python e uma linguagem de programacao",
    "d3": "cachorro late e o gato mia",
}
pergunta = "o gato e o cachorro"

# TODO: monte o vocabulario, implemente vetorizar/cosseno e imprima as similaridades.
