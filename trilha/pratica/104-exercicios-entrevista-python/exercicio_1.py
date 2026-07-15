"""Exercicio 1 - Top-k palavras mais frequentes.

Setup (dado):
    texto = "embedding token embedding rag token embedding rag chunk rag"
    k = 3

Tarefa:
    Implemente top_k_palavras(texto, k): minusculas, split por espaco, conte com
    Counter e ordene por (-frequencia, palavra) para desempate deterministico;
    devolva os k primeiros. Imprima "<palavra>: <freq>" para cada um.

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/104-exercicios-entrevista-python/solucao_1.saida.txt
"""
from collections import Counter

texto = "embedding token embedding rag token embedding rag chunk rag"
k = 3

# TODO: implemente top_k_palavras(texto, k) e imprima as k palavras mais frequentes.
