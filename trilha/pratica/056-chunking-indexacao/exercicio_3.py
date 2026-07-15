"""Exercicio 3 - Indice invertido (postings) e busca por intersecao.

Setup (dado):
    chunks = {
        "c0": "instalacao do produto em windows",
        "c1": "instalacao do produto em linux",
        "c2": "remocao do produto em windows",
    }

Tarefa:
    Implemente construir_indice(chunks): para cada chunk (em ordem de id) e cada
    termo unico (em ordem), acrescenta o id do chunk a postings[termo]. Implemente
    buscar(indice, consulta): intersecao das postings de todos os termos da
    consulta (ordenada). Imprima as postings de 'windows', de 'instalacao' e o
    resultado de buscar "instalacao windows".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/056-chunking-indexacao/solucao_3.saida.txt
"""
import re

chunks = {
    "c0": "instalacao do produto em windows",
    "c1": "instalacao do produto em linux",
    "c2": "remocao do produto em windows",
}

# TODO: implemente construir_indice e buscar; imprima as postings e a busca.
