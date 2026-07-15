"""Solução de referência — Exercício 1 da Lição 065.

Crítico determinístico: pontua um rascunho por regras simples e lista problemas.
"""


def criticar(texto):
    problemas = []
    if "titulo" not in texto:
        problemas.append("sem titulo")
    if len(texto.split()) < 3:
        problemas.append("poucas palavras")
    nota = 10 - 4 * len(problemas)
    return nota, problemas


for d in ["titulo e mais texto", "curto"]:
    nota, problemas = criticar(d)
    print(f"{d!r}: nota={nota} problemas={problemas}")
