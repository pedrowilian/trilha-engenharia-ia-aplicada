"""Exercicio 3 - Laco agentico completo (recuperar -> avaliar -> iterar).

Setup (dado):
    corpus = {
        "d1": "o plano pro custa 30 reais por mes",
        "d2": "o plano pro inclui dez projetos",
    }
    sinonimos = {"preco": "custa", "valor": "custa"}
    pergunta = "preco do plano pro", limiar = 3, max_iter = 3.

Tarefa:
    Junte recuperar(consulta), reformular(consulta) e suficiente(score, limiar=3)
    num agente(pergunta, max_iter=3) que, a cada iteracao, recupera, decide se o
    score e suficiente (responde) ou reformula e tenta de novo. Imprima
    "iteracoes: <n>", "fonte: <id>" e "resposta: <texto>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/061-agentic-rag/solucao_3.saida.txt
"""
import re

corpus = {
    "d1": "o plano pro custa 30 reais por mes",
    "d2": "o plano pro inclui dez projetos",
}
sinonimos = {"preco": "custa", "valor": "custa"}
pergunta = "preco do plano pro"

# TODO: implemente o laco agentico (recuperar/avaliar/reformular) com parada controlada.
