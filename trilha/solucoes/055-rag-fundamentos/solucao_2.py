"""Solucao de referencia - Exercicio 2 da Licao 055.

Pipeline minimo retrieve -> augment -> generate: recupera o documento mais
relevante, monta um prompt com o contexto e gera a resposta com um gerador-stub
deterministico (que extrai a sentenca do contexto). Sem servicos externos.
"""
import re


corpus = {
    "d1": "A politica de reembolso da empresa e de 30 dias corridos.",
    "d2": "O prazo de entrega padrao e de 5 dias uteis.",
    "d3": "O horario de atendimento e das 9h as 18h.",
}


def tokenizar(texto):
    return set(re.findall(r"[a-z0-9]+", texto.lower()))


def recuperar(pergunta, corpus):
    return max(sorted(corpus), key=lambda d: len(tokenizar(pergunta) & tokenizar(corpus[d])))


def aumentar(pergunta, doc_texto):
    return f"Contexto: {doc_texto}\nPergunta: {pergunta}\nResposta:"


def gerar(prompt):
    contexto = prompt.split("Contexto: ", 1)[1].split("\n", 1)[0]
    return contexto


pergunta = "quantos dias para reembolso"
doc = recuperar(pergunta, corpus)
prompt = aumentar(pergunta, corpus[doc])
resposta = gerar(prompt)
print("doc recuperado:", doc)
print("resposta:", resposta)
