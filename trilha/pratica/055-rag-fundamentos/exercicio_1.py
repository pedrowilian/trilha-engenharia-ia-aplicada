"""Exercicio 1 - Recuperacao por sobreposicao de termos.

Setup (dado):
    corpus = {
        "d1": "A capital da Franca e Paris e fica na Europa.",
        "d2": "A politica de reembolso da empresa e de 30 dias corridos.",
        "d3": "O prazo de entrega padrao do pedido e de 5 dias uteis.",
        "d4": "Paris sediou os jogos olimpicos no verao.",
    }
    pergunta = "qual e a politica de reembolso em dias"

Tarefa:
    Implemente tokenizar(texto) (conjunto de tokens [a-z0-9]+ em minusculas) e
    recuperar(pergunta, corpus, k=2), que pontua cada documento pelo numero de
    termos da consulta presentes nele e devolve os k melhores (desempate por id).
    Imprima, para os 2 melhores, "<id> score=<n>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/055-rag-fundamentos/solucao_1.saida.txt
"""
import re

corpus = {
    "d1": "A capital da Franca e Paris e fica na Europa.",
    "d2": "A politica de reembolso da empresa e de 30 dias corridos.",
    "d3": "O prazo de entrega padrao do pedido e de 5 dias uteis.",
    "d4": "Paris sediou os jogos olimpicos no verao.",
}
pergunta = "qual e a politica de reembolso em dias"

# TODO: implemente tokenizar e recuperar e imprima os 2 documentos melhores.
