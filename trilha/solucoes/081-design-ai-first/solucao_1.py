"""Solução de referência — Exercício 1 da Lição 081.

Triagem AI-First: decide entre "regras", "ia" e "ia+humano". Determinístico.
"""


def decidir_abordagem(regras_cobrem, entrada_ambigua, custo_erro_alto):
    if regras_cobrem:
        return "regras"
    if not entrada_ambigua:
        return "regras"
    return "ia+humano" if custo_erro_alto else "ia"


problemas = [
    ("checar CEP", True, False, False),
    ("resumir contrato", False, True, True),
    ("traduzir frase", False, True, False),
    ("somar valores", True, False, False),
]

for nome, cobrem, ambigua, custo in problemas:
    print(f"{nome:>18}: {decidir_abordagem(cobrem, ambigua, custo)}")
