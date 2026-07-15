"""Exercicio 1 - Multi-index (uniao de candidatos).

Setup (dado):
    indice_faq = {"f1": "como redefinir a senha", "f2": "como cancelar a assinatura"}
    indice_docs = {"g1": "a senha deve ter 8 caracteres",
                   "g2": "politica de cancelamento e reembolso"}
    pergunta = "como redefinir a senha"

Tarefa:
    Implemente buscar(indice, pergunta, k=1) (melhores por sobreposicao de termos,
    so score > 0). Busque o top-1 de cada indice e una os candidatos num conjunto
    ordenado. Imprima "faq: <lista>", "docs: <lista>" e "candidatos unidos: <ids>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/060-rag-multi-index-reranking/solucao_1.saida.txt
"""
import re

indice_faq = {
    "f1": "como redefinir a senha",
    "f2": "como cancelar a assinatura",
}
indice_docs = {
    "g1": "a senha deve ter 8 caracteres",
    "g2": "politica de cancelamento e reembolso",
}
pergunta = "como redefinir a senha"

# TODO: implemente buscar e una os candidatos dos dois indices.
