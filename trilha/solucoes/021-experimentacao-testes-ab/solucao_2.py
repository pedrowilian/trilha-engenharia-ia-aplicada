"""Solucao de referencia — Licao 021, Exercicio 2.

Teste z para duas proporcoes do zero, com decisao por p-valor. Mostra que uma
diferenca pequena com amostra pequena NAO e significativa.
"""
import math


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def z_test_proporcoes(x1, n1, x2, n2):
    p1, p2 = x1 / n1, x2 / n2
    p_pool = (x1 + x2) / (n1 + n2)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
    z = (p2 - p1) / se
    return z, 2 * (1 - phi(abs(z)))


def main():
    # amostra pequena: 11% vs 13% com 300 por grupo
    z1, p1 = z_test_proporcoes(33, 300, 39, 300)
    # amostra grande: mesma diferenca relativa com 6000 por grupo
    z2, p2 = z_test_proporcoes(660, 6000, 780, 6000)
    print(f"amostra pequena: z={z1:.4f} p={p1:.4f} significativo={p1 < 0.05}")
    print(f"amostra grande:  z={z2:.4f} p={p2:.4f} significativo={p2 < 0.05}")
    print("mais dados detectam o mesmo efeito:", (not p1 < 0.05) and (p2 < 0.05))


if __name__ == "__main__":
    main()
