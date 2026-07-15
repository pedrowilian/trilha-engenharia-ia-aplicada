"""Exercício 2 — Executor sequencial.

Setup:
    passos = [("incrementar", lambda x: x + 1),
              ("triplicar", lambda x: x * 3),
              ("subtrair2", lambda x: x - 2)]
    valor inicial = 3

Tarefa:
    Aplique os passos em ordem, encadeando o resultado. Após cada passo,
    imprima `{nome}: {valor}`. Ao final, imprima `resultado: {valor}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/064-plan-execute/solucao_2.saida.txt (resultado: 10).
"""

passos = [
    ("incrementar", lambda x: x + 1),
    ("triplicar", lambda x: x * 3),
    ("subtrair2", lambda x: x - 2),
]
valor = 3

# TODO: execute os passos em sequência.
