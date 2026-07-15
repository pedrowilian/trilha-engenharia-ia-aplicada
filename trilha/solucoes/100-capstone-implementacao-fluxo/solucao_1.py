"""Solução de referência — Exercício 1 da Lição 100.

RAG mínimo: recuperação por similaridade de cosseno sobre um corpus de três
documentos. Determinístico e offline. Imprime o score de cada documento (4 casas)
em ordem decrescente (desempate por doc_id) e o top-1.
"""
import math
import re


def tokenizar(t):
    return re.findall(r"[a-z0-9]+", t.lower())


def freq(tokens):
    f = {}
    for tok in tokens:
        f[tok] = f.get(tok, 0) + 1
    return f


def cosseno(a, b):
    comuns = set(a) & set(b)
    num = sum(a[t] * b[t] for t in comuns)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return num / (na * nb) if na and nb else 0.0


corpus = {
    "doc-senha": "para redefinir a senha acesse configuracoes e redefinir senha",
    "doc-fatura": "a fatura e gerada todo dia primeiro baixe a fatura em pdf",
    "doc-reembolso": "reembolsos sao processados em ate cinco dias uteis",
}
consulta = freq(tokenizar("como redefinir minha senha"))
ranque = sorted(
    ((round(cosseno(consulta, freq(tokenizar(txt))), 4), doc) for doc, txt in corpus.items()),
    key=lambda par: (-par[0], par[1]),
)
for score, doc in ranque:
    print(f"{doc}: {score:.4f}")
print(f"top-1: {ranque[0][1]}")
