"""Exercício 1 — RAG por similaridade de cosseno.

Setup:
    corpus = {
        "doc-senha": "para redefinir a senha acesse configuracoes e redefinir senha",
        "doc-fatura": "a fatura e gerada todo dia primeiro baixe a fatura em pdf",
        "doc-reembolso": "reembolsos sao processados em ate cinco dias uteis",
    }
    consulta = "como redefinir minha senha"

Tarefa:
    Tokenize por `[a-z0-9]+` (minúsculas), monte vetores de frequência e calcule
    a similaridade de cosseno entre a consulta e cada documento. Imprima
    `doc: {score:.4f}` em ordem decrescente de score (desempate por doc_id) e,
    ao final, `top-1: {doc_id}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/100-capstone-implementacao-fluxo/solucao_1.saida.txt.
"""
import math
import re

corpus = {
    "doc-senha": "para redefinir a senha acesse configuracoes e redefinir senha",
    "doc-fatura": "a fatura e gerada todo dia primeiro baixe a fatura em pdf",
    "doc-reembolso": "reembolsos sao processados em ate cinco dias uteis",
}
consulta = "como redefinir minha senha"

# TODO: tokenize, calcule o cosseno por documento e imprima o ranque + top-1.
