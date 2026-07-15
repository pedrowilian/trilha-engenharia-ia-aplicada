"""Solucao de referencia - Exercicio 3 da Licao 057.

Pipeline RAG basico completo: recupera os top-k por cosseno, monta o prompt
aumentado com os trechos recuperados e gera a resposta (gerador-stub que devolve
o texto do trecho mais relevante). Imprime o prompt, as fontes e a resposta.
"""
import re

import numpy as np


corpus = {
    "d1": "o plano basico custa 10 reais por mes",
    "d2": "o plano pro custa 30 reais por mes",
    "d3": "o suporte responde em ate 24 horas",
}


def tokenizar(t):
    return re.findall(r"[a-z0-9]+", t.lower())


vocab = sorted({tok for txt in corpus.values() for tok in tokenizar(txt)})
idx = {t: i for i, t in enumerate(vocab)}


def vetorizar(texto):
    v = np.zeros(len(vocab))
    for tok in tokenizar(texto):
        if tok in idx:
            v[idx[tok]] += 1.0
    return v


def cosseno(a, b):
    na, nb = np.linalg.norm(a), np.linalg.norm(b)
    if na == 0 or nb == 0:
        return 0.0
    return float(a @ b / (na * nb))


def recuperar(pergunta, k=2):
    qv = vetorizar(pergunta)
    ranking = sorted(((d, cosseno(qv, vetorizar(corpus[d]))) for d in corpus),
                     key=lambda t: (-t[1], t[0]))
    return ranking[:k]


def montar_prompt(pergunta, recuperados):
    ctx = "\n".join(f"[{d}] {corpus[d]}" for d, _ in recuperados)
    return f"Contexto:\n{ctx}\n\nPergunta: {pergunta}\nResposta:"


def gerar(recuperados):
    return corpus[recuperados[0][0]]


pergunta = "quanto custa o plano basico"
rec = recuperar(pergunta, k=2)
print(montar_prompt(pergunta, rec))
print("---")
print("fontes:", [d for d, _ in rec])
print("resposta:", gerar(rec))
