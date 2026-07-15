"""Solução de referência — Exercício 2 da Lição 065.

Ciclo gerar -> criticar -> revisar: a cada iteração o crítico aponta a parte
faltante e o revisor a adiciona, até o rascunho ser aceito. Determinístico.
"""


def criticar(texto):
    return [p for p in ["abertura", "dados", "conclusao"] if p not in texto]


def revisar(texto, falta):
    return texto + " " + falta[0]


rascunho = "abertura"
for it in range(1, 6):
    falta = criticar(rascunho)
    print(f"iter {it}: falta={falta}")
    if not falta:
        print("aceito")
        break
    rascunho = revisar(rascunho, falta)

print("final:", rascunho)
