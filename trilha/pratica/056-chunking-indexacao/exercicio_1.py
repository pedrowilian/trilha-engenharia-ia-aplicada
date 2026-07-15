"""Exercicio 1 - Chunking de tamanho fixo.

Setup (dado):
    texto = ("o gato dorme no sofa o cachorro corre no parque "
             "o passaro voa alto no ceu azul")

Tarefa:
    Implemente tokenizar(t) ([a-z0-9]+ em minusculas) e
    chunk_fixo(tokens, tamanho) que parte os tokens em blocos contiguos de
    tamanho fixo (sem sobreposicao). Com tamanho=5, imprima "c<i>: <tokens>"
    para cada chunk e "n_chunks: <n>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/056-chunking-indexacao/solucao_1.saida.txt
"""
import re

texto = ("o gato dorme no sofa o cachorro corre no parque "
         "o passaro voa alto no ceu azul")

# TODO: implemente tokenizar e chunk_fixo; imprima os chunks de tamanho 5.
