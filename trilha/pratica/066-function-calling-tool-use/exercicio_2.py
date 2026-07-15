"""Exercício 2 — Despacho de tool-call.

Setup:
    registro = {"concat": lambda a, b: a + b, "repetir": lambda s, n: s * n}
    chamadas = [
        {"name": "concat", "arguments": {"a": "ab", "b": "cd"}},
        {"name": "repetir", "arguments": {"s": "xy", "n": 3}},
    ]

Tarefa:
    Implemente `despachar(tool_call)` que busca a função pelo `name` e a chama
    com `**arguments`. Para cada chamada, imprima `{name} -> {resultado}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/066-function-calling-tool-use/solucao_2.saida.txt
"""

registro = {
    "concat": lambda a, b: a + b,
    "repetir": lambda s, n: s * n,
}
chamadas = [
    {"name": "concat", "arguments": {"a": "ab", "b": "cd"}},
    {"name": "repetir", "arguments": {"s": "xy", "n": 3}},
]

# TODO: implemente o despacho e imprima os resultados.
