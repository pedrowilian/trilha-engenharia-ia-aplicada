"""Solução de referência — Exercício 1 da Lição 076.

Limpeza de um dataset cru: normaliza espaços, descarta exemplos com algum
campo vazio e remove duplicatas exatas (pergunta, resposta).
"""
brutos = [
    {"pergunta": "Defina overfitting.", "resposta": "Decorar o treino."},
    {"pergunta": "  Defina overfitting. ", "resposta": "Decorar o treino."},
    {"pergunta": "O que e um token?", "resposta": "Unidade de texto."},
    {"pergunta": "Pergunta sem resposta", "resposta": "   "},
    {"pergunta": "", "resposta": "orfa"},
    {"pergunta": "O que e um token?", "resposta": "Unidade de texto."},
]


def normalizar(texto):
    return " ".join(texto.split())


vistos = set()
limpos = []
for ex in brutos:
    p, r = normalizar(ex["pergunta"]), normalizar(ex["resposta"])
    if not p or not r:            # descarta campos vazios
        continue
    if (p, r) in vistos:          # descarta duplicata exata
        continue
    vistos.add((p, r))
    limpos.append({"pergunta": p, "resposta": r})

print("brutos:", len(brutos))
print("limpos:", len(limpos))
print("removidos:", len(brutos) - len(limpos))
for ex in limpos:
    print(f"- {ex['pergunta']} | {ex['resposta']}")
