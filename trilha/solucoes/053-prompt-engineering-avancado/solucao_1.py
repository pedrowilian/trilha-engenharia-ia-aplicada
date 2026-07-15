"""Solução de referência — Exercício 1 da Lição 053.

Monta um prompt few-shot: cada exemplo é formatado como par Texto/Rotulo e a
consulta entra ao final com o rótulo em aberto, para o modelo completar.
"""


def montar_few_shot(exemplos, consulta):
    linhas = []
    for entrada, rotulo in exemplos:
        linhas.append(f"Texto: {entrada}\nRotulo: {rotulo}")
    linhas.append(f"Texto: {consulta}\nRotulo:")
    return "\n".join(linhas)


exemplos = [
    ("adorei o filme", "positivo"),
    ("que experiencia horrivel", "negativo"),
]
consulta = "o atendimento foi otimo"
print(montar_few_shot(exemplos, consulta))
