"""Solucao de referencia - Exercicio 3 da Licao 060.

Re-ranking com cross-encoder: a 1a etapa (bi-encoder) pontua consulta e documento
por embeddings separados e pode errar; o re-ranker (cross-encoder) olha o par
consulta-documento em conjunto (aqui, sobreposicao lexical do texto) e reordena os
candidatos, podendo inverter o top-1.
"""
import re

import numpy as np


candidatos = {
    "c1": {"emb": [1.0, 0.0], "texto": "introducao geral ao tema"},
    "c2": {"emb": [0.7, 0.7], "texto": "como redefinir a senha no painel"},
}
pergunta_emb = [1.0, 0.0]
pergunta_texto = "como redefinir a senha"


def cosseno(a, b):
    a, b = np.array(a, float), np.array(b, float)
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


def tok(t):
    return set(re.findall(r"[a-z0-9]+", t.lower()))


def cross_encoder(p, texto):
    return len(tok(p) & tok(texto))


prim = sorted(((c, cosseno(pergunta_emb, candidatos[c]["emb"])) for c in candidatos),
              key=lambda t: (-t[1], t[0]))
rer = sorted(((c, cross_encoder(pergunta_texto, candidatos[c]["texto"])) for c in candidatos),
             key=lambda t: (-t[1], t[0]))

print("bi-encoder (1a etapa):", [(c, round(s, 4)) for c, s in prim])
print("cross-encoder (rerank):", [(c, s) for c, s in rer])
print("top-1 antes:", prim[0][0], "| depois:", rer[0][0])
