"""Solução de referência — Exercício 3 da Lição 071.

Agregação: combina os resultados dos trabalhadores num resultado final ordenado.
Determinístico.
"""

resultados = {
    "dados": "ok",
    "modelo": "treinado",
    "relatorio": "enviado",
}
ordem = ["dados", "modelo", "relatorio"]
final = " | ".join(f"{k}={resultados[k]}" for k in ordem)

print("partes:", len(resultados))
print("final:", final)
