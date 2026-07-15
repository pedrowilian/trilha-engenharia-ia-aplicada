"""Solução de referência — Exercício 2 da Lição 080.

Teste A/B entre o modelo base e o ajustado: acurácia de cada um, lift absoluto
e relativo, e o vencedor.
"""


def acuracia(gold, pred):
    return sum(1 for g, p in zip(gold, pred) if g == p) / len(gold)


gold = ["x", "y", "z", "x", "y", "z", "x", "y"]
base = ["x", "y", "x", "x", "z", "z", "x", "x"]
ajustado = ["x", "y", "z", "x", "y", "z", "x", "y"]

acc_base = acuracia(gold, base)
acc_aj = acuracia(gold, ajustado)
lift = acc_aj - acc_base

print(f"acuracia base    : {acc_base:.3f}")
print(f"acuracia ajustado: {acc_aj:.3f}")
print(f"lift absoluto    : {lift:+.3f}")
print(f"lift relativo    : {100 * lift / acc_base:+.1f}%")
print("vencedor:", "ajustado" if acc_aj > acc_base else "base" if acc_base > acc_aj else "empate")
