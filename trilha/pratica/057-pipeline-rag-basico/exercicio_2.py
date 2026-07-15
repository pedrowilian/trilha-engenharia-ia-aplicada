"""Exercicio 2 - Recuperacao top-k por cosseno.

Setup (dado):
    corpus com d1..d4 (animais e linguagens de programacao).
    pergunta = "linguagem python"

Tarefa:
    Reaproveite vetorizar/cosseno e implemente recuperar(pergunta, k=2) que
    ordena os documentos por (-cosseno, id) e devolve os k melhores. Imprima
    "<id> <cosseno com 4 casas>" para os 2 melhores.

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/057-pipeline-rag-basico/solucao_2.saida.txt
"""
import re

import numpy as np

corpus = {
    "d1": "gato e cachorro sao animais domesticos",
    "d2": "python e uma linguagem de programacao",
    "d3": "cachorro late e o gato mia",
    "d4": "java e python sao linguagens populares",
}
pergunta = "linguagem python"

# TODO: implemente recuperar(pergunta, k=2) por cosseno e imprima os 2 melhores.
