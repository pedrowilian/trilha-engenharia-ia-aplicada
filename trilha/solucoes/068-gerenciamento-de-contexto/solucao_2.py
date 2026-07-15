"""Solução de referência — Exercício 2 da Lição 068.

Truncamento: mantém a mensagem de sistema e inclui as mensagens mais recentes
que couberem no orçamento, descartando as mais antigas. Determinístico.
"""


def contar(t):
    return len(t.split())


sistema = "assistente util"
historico = ["passo um inicial", "passo dois meio", "passo tres final"]
limite = 8

incluidas = []
usado = contar(sistema)
for msg in reversed(historico):
    c = contar(msg)
    if usado + c <= limite:
        incluidas.append(msg)
        usado += c
    else:
        break
incluidas.reverse()

print("sistema:", sistema)
print("incluidas:", incluidas)
print("tokens usados:", usado)
