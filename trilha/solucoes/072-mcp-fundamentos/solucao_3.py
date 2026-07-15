"""Solução de referência — Exercício 3 da Lição 072.

Negociação de capacidades por interseção dos conjuntos do cliente e do servidor.
Determinístico (saída ordenada).
"""
cap_cliente = {"resources", "tools", "roots"}
cap_servidor = {"tools", "prompts", "resources"}

negociadas = cap_cliente & cap_servidor

print("negociadas:", sorted(negociadas))
print("usa resources?", "resources" in negociadas)
print("usa roots?", "roots" in negociadas)
