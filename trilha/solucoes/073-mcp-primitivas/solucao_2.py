"""Solução de referência — Exercício 2 da Lição 073.

Despacho de tools por nome, expandindo os argumentos nomeados. Determinístico.
"""
def dobro(x):
    return x * 2

def concatenar(a, b):
    return a + b

tools = {
    "dobro": dobro,
    "concatenar": concatenar,
}

def chamar_tool(nome, argumentos):
    return tools[nome](**argumentos)

print("tools:", sorted(tools))
print("dobro(21) =", chamar_tool("dobro", {"x": 21}))
print("concatenar =", chamar_tool("concatenar", {"a": "mc", "b": "p"}))
