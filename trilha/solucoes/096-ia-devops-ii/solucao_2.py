"""Solução de referência — Exercício 2 da Lição 096.

FinOps: previsão de custo por ajuste linear (mínimos quadrados) sobre o
histórico mensal. Determinístico.
"""


def ajuste_linear(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    a = sxy / sxx
    b = my - a * mx
    return a, b


meses = [1, 2, 3, 4, 5]
custo = [200, 230, 260, 290, 320]
a, b = ajuste_linear(meses, custo)
previsao = a * 6 + b

print(f"inclinacao: {a:.2f} USD/mes")
print(f"previsao mes 6: {previsao:.2f} USD")
