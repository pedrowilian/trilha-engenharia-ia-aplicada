"""Solução de referência — Exercício 2 da Lição 066.

Despacho de tool-call: mapeia o nome para a função registrada e a chama com os
argumentos nomeados. Determinístico.
"""

registro = {
    "concat": lambda a, b: a + b,
    "repetir": lambda s, n: s * n,
}


def despachar(tool_call):
    fn = registro[tool_call["name"]]
    return fn(**tool_call["arguments"])


chamadas = [
    {"name": "concat", "arguments": {"a": "ab", "b": "cd"}},
    {"name": "repetir", "arguments": {"s": "xy", "n": 3}},
]
for tc in chamadas:
    print(tc["name"], "->", despachar(tc))
