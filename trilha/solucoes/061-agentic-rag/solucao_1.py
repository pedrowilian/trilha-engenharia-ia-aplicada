"""Solucao de referencia - Exercicio 1 da Licao 061.

Decisao de recuperar: o agente decide SE deve buscar antes de buscar. Perguntas
com termo interrogativo disparam a recuperacao; mensagens puramente sociais
(saudacoes/agradecimentos) sao respondidas sem tocar no indice.
"""
import re


interrogativos = {"qual", "quais", "quanto", "quantos", "como", "onde", "quando"}
chitchat = {"oi", "ola", "bom", "dia", "boa", "tarde", "noite", "obrigado", "tchau"}


def tok(t):
    return set(re.findall(r"[a-z0-9]+", t.lower()))


def precisa_buscar(pergunta):
    toks = tok(pergunta)
    if toks & interrogativos:
        return True
    if toks and toks <= chitchat:
        return False
    return True


for p in ["bom dia", "qual o preco do plano", "obrigado"]:
    print(f"{p!r} -> buscar={precisa_buscar(p)}")
