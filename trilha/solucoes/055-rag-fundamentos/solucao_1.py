"""Solucao de referencia - Exercicio 1 da Licao 055.

Recuperacao por sobreposicao de termos: pontua cada documento pelo numero de
termos da consulta que ele contem e devolve os k melhores (desempate por id).
E o mecanismo mais simples de recuperacao nao-parametrica de um sistema RAG.
"""
import re


corpus = {
    "d1": "A capital da Franca e Paris e fica na Europa.",
    "d2": "A politica de reembolso da empresa e de 30 dias corridos.",
    "d3": "O prazo de entrega padrao do pedido e de 5 dias uteis.",
    "d4": "Paris sediou os jogos olimpicos no verao.",
}


def tokenizar(texto):
    return set(re.findall(r"[a-z0-9]+", texto.lower()))


def recuperar(pergunta, corpus, k=2):
    q = tokenizar(pergunta)
    pontuados = [(did, len(q & tokenizar(corpus[did]))) for did in sorted(corpus)]
    pontuados.sort(key=lambda t: (-t[1], t[0]))
    return pontuados[:k]


pergunta = "qual e a politica de reembolso em dias"
for did, score in recuperar(pergunta, corpus):
    print(f"{did} score={score}")
