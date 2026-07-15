"""Exercicio 3 - Pipeline RAG basico completo.

Setup (dado):
    corpus = {
        "d1": "o plano basico custa 10 reais por mes",
        "d2": "o plano pro custa 30 reais por mes",
        "d3": "o suporte responde em ate 24 horas",
    }
    pergunta = "quanto custa o plano basico"

Tarefa:
    Junte tudo: recuperar(pergunta, k=2) por cosseno; montar_prompt(pergunta,
    recuperados) com um bloco "Contexto:" listando "[id] texto" por linha,
    seguido de "Pergunta: ..." e "Resposta:"; gerar(recuperados) devolvendo o
    texto do documento mais relevante. Imprima o prompt, depois "---", depois
    "fontes: <lista>" e "resposta: <texto>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/057-pipeline-rag-basico/solucao_3.saida.txt
"""
import re

import numpy as np

corpus = {
    "d1": "o plano basico custa 10 reais por mes",
    "d2": "o plano pro custa 30 reais por mes",
    "d3": "o suporte responde em ate 24 horas",
}
pergunta = "quanto custa o plano basico"

# TODO: implemente recuperar, montar_prompt e gerar; imprima o pipeline completo.
