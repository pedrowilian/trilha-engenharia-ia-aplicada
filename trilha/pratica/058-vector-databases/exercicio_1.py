"""Exercicio 1 - Indice flat (busca exata).

Setup (dado):
    base = {"v1": [1,1], "v2": [4,2], "v3": [2,5], "v4": [5,5]}
    consulta = [4, 4]

Tarefa:
    Implemente l2(a, b) (distancia euclidiana) e devolva os 2 vetores mais
    proximos da consulta, ordenados por (distancia, id). Imprima
    "<id> dist=<4 casas>" para os 2 melhores e "comparacoes: <n>" (= tamanho da
    base, pois o flat varre tudo).

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/058-vector-databases/solucao_1.saida.txt
"""
import numpy as np

base = {
    "v1": [1.0, 1.0],
    "v2": [4.0, 2.0],
    "v3": [2.0, 5.0],
    "v4": [5.0, 5.0],
}
consulta = [4.0, 4.0]

# TODO: implemente l2 e a busca flat; imprima os 2 melhores e as comparacoes.
