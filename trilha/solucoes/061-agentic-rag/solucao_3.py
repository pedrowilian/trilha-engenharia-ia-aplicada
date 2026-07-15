"""Solucao de referencia - Exercicio 3 da Licao 061.

Laco agentico completo: recuperar -> avaliar suficiencia -> (reformular | responder),
com numero maximo de iteracoes. Junta a reformulacao (Exercicio 2) com a avaliacao
de suficiencia e a parada controlada, devolvendo a resposta com a fonte.
"""
import re


corpus = {
    "d1": "o plano pro custa 30 reais por mes",
    "d2": "o plano pro inclui dez projetos",
}
sinonimos = {"preco": "custa", "valor": "custa"}


def tok(t):
    return set(re.findall(r"[a-z0-9]+", t.lower()))


def recuperar(consulta):
    pont = sorted(((d, len(tok(consulta) & tok(corpus[d]))) for d in corpus),
                  key=lambda t: (-t[1], t[0]))
    return pont[0]


def reformular(consulta):
    return " ".join(sinonimos.get(w, w) for w in consulta.lower().split())


def suficiente(score, limiar=3):
    return score >= limiar


def agente(pergunta, max_iter=3):
    consulta = pergunta
    for it in range(1, max_iter + 1):
        d, s = recuperar(consulta)
        if suficiente(s):
            return {"iters": it, "fonte": d, "resposta": corpus[d]}
        consulta = reformular(consulta)
    return {"iters": max_iter, "fonte": None, "resposta": "sem resposta suficiente"}


pergunta = "preco do plano pro"
res = agente(pergunta)
print("iteracoes:", res["iters"])
print("fonte:", res["fonte"])
print("resposta:", res["resposta"])
