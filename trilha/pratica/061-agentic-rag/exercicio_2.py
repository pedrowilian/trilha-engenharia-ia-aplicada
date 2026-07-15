"""Exercicio 2 - Reformulacao e busca iterativa.

Setup (dado):
    corpus = {
        "d1": "a devolucao do valor ocorre em cinco dias uteis",
        "d2": "contato do suporte por email",
    }
    sinonimos = {"reembolso": "devolucao"}
    consulta inicial = "reembolso", limiar = 1, max 3 iteracoes.

Tarefa:
    Implemente melhor(consulta) (melhor doc por sobreposicao, desempate por id) e
    reformular(consulta) (troca cada palavra pelo sinonimo, se houver). Itere ate
    o score alcancar o limiar ou esgotar 3 iteracoes; registre o historico.
    Imprima "iter <i>: consulta=<repr> melhor=<id> score=<n>" e "resolvido: <bool>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/061-agentic-rag/solucao_2.saida.txt
"""
import re

corpus = {
    "d1": "a devolucao do valor ocorre em cinco dias uteis",
    "d2": "contato do suporte por email",
}
sinonimos = {"reembolso": "devolucao"}

# TODO: implemente melhor e reformular; itere ate resolver (limiar=1, max 3 iter).
