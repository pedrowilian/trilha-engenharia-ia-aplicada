"""Solução de referência — Exercício 2 da Lição 064.

Executor sequencial: aplica os passos do plano em ordem, encadeando o resultado.
Determinístico.
"""

passos = [
    ("incrementar", lambda x: x + 1),
    ("triplicar", lambda x: x * 3),
    ("subtrair2", lambda x: x - 2),
]

valor = 3
for nome, fn in passos:
    valor = fn(valor)
    print(f"{nome}: {valor}")
print("resultado:", valor)
