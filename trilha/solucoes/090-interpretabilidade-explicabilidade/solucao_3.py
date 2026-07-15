"""Solução de referência — Exercício 3 da Lição 090.

Explicação global vs local: a importância global é a média de |w_i * x_i| sobre
o conjunto; a explicação local é a atribuição de UMA instância. Semente fixa.
"""
import numpy as np

rng = np.random.default_rng(3)
w = np.array([1.0, -2.0, 0.5])
X = rng.uniform(0.0, 1.0, size=(400, 3))

attrib = X * w
global_imp = np.mean(np.abs(attrib), axis=0)
local = attrib[0]

nomes = ["f0", "f1", "f2"]
for i, nome in enumerate(nomes):
    print(f"{nome}: global={global_imp[i]:.3f} local[0]={local[i]:+.3f}")
mais_global = nomes[int(np.argmax(global_imp))]
print(f"feature mais importante (global): {mais_global}")
