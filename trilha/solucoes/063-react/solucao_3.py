"""Solução de referência — Exercício 3 da Lição 063.

Laço ReAct completo: alterna Thought / Action / Observation e termina ao emitir
"Final Answer". Resolve (10 - 4) + 1 com uma política determinística (scriptada).
"""

ferramentas = {"sub": lambda a, b: a - b, "soma": lambda a, b: a + b}


def politica(passo, memoria):
    if passo == 0:
        return ("Subtrair 4 de 10", "sub", (10, 4))
    if passo == 1:
        return ("Somar 1 ao resultado", "soma", (memoria[-1], 1))
    return ("Pronto", "final", (memoria[-1],))


memoria = []
passo = 0
while True:
    pensamento, acao, args = politica(passo, memoria)
    print(f"Thought: {pensamento}")
    if acao == "final":
        print(f"Final Answer: {args[0]}")
        break
    obs = ferramentas[acao](*args)
    memoria.append(obs)
    print(f"Action: {acao}{args}")
    print(f"Observation: {obs}")
    passo += 1
