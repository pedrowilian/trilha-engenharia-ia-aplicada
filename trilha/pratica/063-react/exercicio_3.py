"""Exercício 3 — Laço ReAct até a resposta final.

Setup:
    ferramentas = {"sub": lambda a, b: a - b, "soma": lambda a, b: a + b}
    Política determinística que resolve (10 - 4) + 1:
      passo 0 -> ("Subtrair 4 de 10", "sub", (10, 4))
      passo 1 -> ("Somar 1 ao resultado", "soma", (memoria[-1], 1))
      senão   -> ("Pronto", "final", (memoria[-1],))

Tarefa:
    Implemente o laço que, a cada passo, imprime `Thought: ...`; se a ação for
    "final", imprime `Final Answer: {valor}` e encerra; senão, executa a
    ferramenta, guarda a observação em `memoria` e imprime `Action: {acao}{args}`
    e `Observation: {obs}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/063-react/solucao_3.saida.txt (termina em `Final Answer: 7`).
"""

ferramentas = {"sub": lambda a, b: a - b, "soma": lambda a, b: a + b}


def politica(passo, memoria):
    if passo == 0:
        return ("Subtrair 4 de 10", "sub", (10, 4))
    if passo == 1:
        return ("Somar 1 ao resultado", "soma", (memoria[-1], 1))
    return ("Pronto", "final", (memoria[-1],))


# TODO: implemente o laço ReAct usando a política acima.
