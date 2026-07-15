"""Exercicio 3 - Re-ranking com cross-encoder (inverte o top-1).

Setup (dado):
    candidatos com emb (bi-encoder) e texto (cross-encoder);
    pergunta_emb = [1.0, 0.0], pergunta_texto = "como redefinir a senha".

Tarefa:
    1a etapa: ordene por cosseno entre pergunta_emb e cada emb. Rerank: ordene por
    cross_encoder = sobreposicao de termos entre pergunta_texto e o texto. Use
    desempate (-score, id). Imprima "bi-encoder (1a etapa): <lista (id, score 4
    casas)>", "cross-encoder (rerank): <lista (id, score)>" e
    "top-1 antes: <id> | depois: <id>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/060-rag-multi-index-reranking/solucao_3.saida.txt
"""
import re

import numpy as np

candidatos = {
    "c1": {"emb": [1.0, 0.0], "texto": "introducao geral ao tema"},
    "c2": {"emb": [0.7, 0.7], "texto": "como redefinir a senha no painel"},
}
pergunta_emb = [1.0, 0.0]
pergunta_texto = "como redefinir a senha"

# TODO: implemente a 1a etapa (cosseno) e o rerank (cross-encoder) e mostre a inversao.
