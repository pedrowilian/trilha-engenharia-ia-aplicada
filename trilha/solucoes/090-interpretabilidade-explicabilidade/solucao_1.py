"""Solução de referência — Exercício 1 da Lição 090.

Atribuição de features de uma única predição de um modelo linear: a contribuição
de cada feature é w_i * x_i; ordenamos por importância (|contribuição|).
Determinístico (sem aleatoriedade).
"""
import numpy as np

nomes = ["valor", "prazo", "historico", "garantia"]
w = np.array([2.0, -1.2, 1.5, -0.8])
b = 0.5
x = np.array([0.9, 0.4, 0.6, 0.7])

contrib = w * x
logito = b + float(contrib.sum())

ordem = np.argsort(-np.abs(contrib))
for i in ordem:
    print(f"{nomes[i]:>9}: {contrib[i]:+.3f}")
print(f"logito total: {logito:+.3f}")
