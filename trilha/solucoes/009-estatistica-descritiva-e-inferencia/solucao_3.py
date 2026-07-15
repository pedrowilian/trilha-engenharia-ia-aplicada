"""Solução de referência — Lição 009, Exercício 3.

Teste de hipótese para teste A/B: teste z de duas proporções com proporção
combinada (pooled) e p-valor bicaudal via CDF da normal padrão.
"""
from math import sqrt, erf


def normal_cdf(z: float) -> float:
    # CDF da normal padrao usando a funcao erro.
    return 0.5 * (1 + erf(z / sqrt(2)))


def main() -> None:
    n_a, c_a = 500, 40   # controle: 40 conversoes em 500
    n_b, c_b = 500, 65   # variante: 65 conversoes em 500

    p_a = c_a / n_a
    p_b = c_b / n_b
    p_pool = (c_a + c_b) / (n_a + n_b)
    se = sqrt(p_pool * (1 - p_pool) * (1 / n_a + 1 / n_b))
    z = (p_b - p_a) / se
    p_valor = 2 * (1 - normal_cdf(abs(z)))

    print(f"taxa A  = {p_a:.4f}")
    print(f"taxa B  = {p_b:.4f}")
    print(f"z       = {z:.4f}")
    print(f"p-valor = {p_valor:.4f}")
    print("rejeita H0 (alpha=0.05)?", p_valor < 0.05)


if __name__ == "__main__":
    main()
