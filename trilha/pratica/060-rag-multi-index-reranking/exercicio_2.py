"""Exercicio 2 - Recuperacao em duas etapas (recall -> precisao).

Setup (dado):
    corpus de 6 documentos; pergunta = "erro de conexao".

Tarefa:
    estagio1(pergunta, N): varre todo o corpus e devolve N candidatos por
    sobreposicao de termos (ordem (-overlap, id)). estagio2(pergunta, candidatos,
    k): reordena SO os candidatos por rerank_score = overlap + 2*(bigramas exatos
    em comum), devolvendo os k melhores. Use N=4, k=2. Imprima
    "estagio1 (N=4): <ids>", "estagio2 (k=2): <lista>" e
    "docs avaliados no rerank: <n> de <total>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/060-rag-multi-index-reranking/solucao_2.saida.txt
"""
import re

corpus = {
    "d1": "erro de conexao com servidor",
    "d2": "conexao de rede com erro",
    "d3": "erro fatal no sistema",
    "d4": "conexao estavel",
    "d5": "de novo o erro",
    "d6": "manual do usuario",
}
pergunta = "erro de conexao"

# TODO: implemente estagio1, rerank_score (com bonus de bigrama) e estagio2.
