"""Solução de referência — Exercício 2 da Lição 053.

Chain-of-thought: resolve um problema em passos explícitos, registrando cada
resultado intermediário antes de chegar à resposta final.
"""

caixas, por_caixa = 3, 4
passos = []

total = caixas * por_caixa
passos.append(f"total = {caixas} * {por_caixa} = {total}")

comidas = 5
sobram = total - comidas
passos.append(f"sobram = {total} - {comidas} = {sobram}")

for p in passos:
    print("passo:", p)
print("resposta:", sobram)
