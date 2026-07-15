"""Solucao de referencia - Exercicio 2 da Licao 060.

Recuperacao em duas etapas: o estagio 1 (barato) varre todo o corpus e devolve N
candidatos por sobreposicao de termos; o estagio 2 (caro) reordena APENAS esses N
com um score mais preciso (sobreposicao + bonus por bigrama exato). Assim o custo
do reranker incide so sobre poucos candidatos.
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


def tok(t):
    return re.findall(r"[a-z0-9]+", t.lower())


def overlap(pergunta, texto):
    return len(set(tok(pergunta)) & set(tok(texto)))


def estagio1(pergunta, N):
    pont = sorted(((d, overlap(pergunta, corpus[d])) for d in corpus),
                  key=lambda t: (-t[1], t[0]))
    return [d for d, _ in pont[:N]]


def rerank_score(pergunta, texto):
    pt, tt = tok(pergunta), tok(texto)
    bigr_p = set(zip(pt, pt[1:]))
    bigr_t = set(zip(tt, tt[1:]))
    return overlap(pergunta, texto) + 2 * len(bigr_p & bigr_t)


def estagio2(pergunta, candidatos, k):
    pont = sorted(((d, rerank_score(pergunta, corpus[d])) for d in candidatos),
                  key=lambda t: (-t[1], t[0]))
    return pont[:k]


pergunta = "erro de conexao"
cand = estagio1(pergunta, N=4)
final = estagio2(pergunta, cand, k=2)
print("estagio1 (N=4):", cand)
print("estagio2 (k=2):", final)
print("docs avaliados no rerank:", len(cand), "de", len(corpus))
