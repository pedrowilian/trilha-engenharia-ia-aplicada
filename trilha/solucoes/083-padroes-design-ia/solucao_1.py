"""Solução de referência — Exercício 1 da Lição 083.

Model router por orçamento de tokens; acumula o custo por tier. Determinístico.
"""


def rotear(tokens, precisa_raciocinio):
    if precisa_raciocinio:
        return "forte"
    if tokens <= 64:
        return "leve"
    return "medio"


reqs = [(10, False), (80, False), (300, False), (50, True)]
custo = {"leve": 1, "medio": 3, "forte": 10}

total = 0
for tk, raciocinio in reqs:
    tier = rotear(tk, raciocinio)
    total += custo[tier]
    print(f"tokens={tk:>3} raciocinio={raciocinio!s:>5} -> {tier} (custo {custo[tier]})")

print("custo total:", total)
