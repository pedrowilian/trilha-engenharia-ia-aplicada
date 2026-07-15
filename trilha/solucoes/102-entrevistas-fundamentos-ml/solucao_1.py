"""Solucao de referencia - Exercicio 1 da Licao 102.

Trade-off vies-variancia: o erro esperado decompoe-se em vies^2 (cai com a
capacidade), variancia (sobe com a capacidade) e ruido irredutivel. O erro total
e uma curva em U cujo minimo e a complexidade otima.
"""


def erros(complexidade):
    vies2 = 16.0 / complexidade
    variancia = 0.05 * complexidade
    ruido = 0.5
    return vies2, variancia, ruido, vies2 + variancia + ruido


for k in [1, 5, 10, 15, 20]:
    b, v, r, t = erros(k)
    print(f"k={k:2d}: vies2={b:.2f} var={v:.2f} ruido={r:.2f} total={t:.2f}")

melhor = min(range(1, 21), key=lambda k: erros(k)[3])
print(f"complexidade otima (1..20): {melhor}")
