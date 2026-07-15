"""Exercicio 2 - Janela deslizante com sobreposicao.

Setup (dado):
    texto = "termo a termo b termo c termo d termo e termo f"

Tarefa:
    Implemente chunk_sobreposto(tokens, tamanho, passo): gera chunks de tamanho
    fixo avancando 'passo' tokens por vez (passo < tamanho => sobreposicao),
    parando assim que um chunk alcanca o fim. Com tamanho=4 e passo=2, imprima
    "j<i>: <tokens>" para cada chunk e "n_chunks: <n>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/056-chunking-indexacao/solucao_2.saida.txt
"""
import re

texto = "termo a termo b termo c termo d termo e termo f"

# TODO: implemente chunk_sobreposto (tamanho=4, passo=2) e imprima os chunks.
