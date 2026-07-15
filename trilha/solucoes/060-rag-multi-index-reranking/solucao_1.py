"""Solucao de referencia - Exercicio 1 da Licao 060.

Multi-index: a consulta vai a varios indices especializados (FAQ, documentacao),
cada um devolve seus melhores candidatos e o sistema une os candidatos num pool
unico, deduplicado, para a etapa seguinte.
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


def tok(t):
    return set(re.findall(r"[a-z0-9]+", t.lower()))


def buscar(indice, pergunta, k=1):
    pont = sorted(((d, len(tok(pergunta) & tok(indice[d]))) for d in indice),
                  key=lambda t: (-t[1], t[0]))
    return [(d, s) for d, s in pont[:k] if s > 0]


pergunta = "como redefinir a senha"
faq = buscar(indice_faq, pergunta, k=1)
docs = buscar(indice_docs, pergunta, k=1)
print("faq:", faq)
print("docs:", docs)
print("candidatos unidos:", sorted({d for d, _ in faq + docs}))
