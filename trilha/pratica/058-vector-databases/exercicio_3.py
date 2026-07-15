"""Exercicio 3 - Filtragem por metadados + busca vetorial (modelo pgvector).

Setup (dado):
    registros com id, vec e meta (idioma, ano); consulta = [1, 0].

Tarefa:
    Implemente cosseno(a, b) e buscar(consulta, filtro, k=3): primeiro filtra os
    registros cujos metadados casam com TODOS os pares de 'filtro', depois ordena
    os candidatos por (-cosseno, id) e devolve os k ids. Imprima o resultado para
    {} (sem filtro), {idioma: pt} e {idioma: pt, ano: 2023}.

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/058-vector-databases/solucao_3.saida.txt
"""
import numpy as np

registros = [
    {"id": "r1", "vec": [1.0, 0.0], "meta": {"idioma": "pt", "ano": 2023}},
    {"id": "r2", "vec": [0.9, 0.1], "meta": {"idioma": "en", "ano": 2023}},
    {"id": "r3", "vec": [0.8, 0.2], "meta": {"idioma": "pt", "ano": 2021}},
    {"id": "r4", "vec": [0.0, 1.0], "meta": {"idioma": "pt", "ano": 2023}},
]
consulta = [1.0, 0.0]

# TODO: implemente cosseno e buscar (filtro de metadados + ordenacao por cosseno).
