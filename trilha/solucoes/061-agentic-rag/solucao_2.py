"""Solucao de referencia - Exercicio 2 da Licao 061.

Reformulacao e busca iterativa: quando a busca inicial nao alcanca o limiar de
relevancia, o agente reescreve a consulta (expandindo sinonimos) e tenta de novo,
ate resolver ou esgotar as iteracoes.
"""
import re


corpus = {
    "d1": "a devolucao do valor ocorre em cinco dias uteis",
    "d2": "contato do suporte por email",
}
sinonimos = {"reembolso": "devolucao"}


def tok(t):
    return set(re.findall(r"[a-z0-9]+", t.lower()))


def melhor(consulta):
    pont = sorted(((d, len(tok(consulta) & tok(corpus[d]))) for d in corpus),
                  key=lambda t: (-t[1], t[0]))
    return pont[0]


def reformular(consulta):
    return " ".join(sinonimos.get(w, w) for w in consulta.lower().split())


consulta = "reembolso"
limiar = 1
historico = []
for it in range(1, 4):
    d, s = melhor(consulta)
    historico.append((it, consulta, d, s))
    if s >= limiar:
        break
    consulta = reformular(consulta)

for it, c, d, s in historico:
    print(f"iter {it}: consulta={c!r} melhor={d} score={s}")
print("resolvido:", historico[-1][3] >= limiar)
