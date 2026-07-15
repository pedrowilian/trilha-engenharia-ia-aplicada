"""Solução de referência — Lição 008, Exercício 2.

Esperança e variância de uma variável aleatória discreta a partir da sua
função de massa de probabilidade (PMF) de um dado "viciado".
"""


def main() -> None:
    valores = [1, 2, 3, 4, 5, 6]
    probs = [0.10, 0.10, 0.20, 0.20, 0.15, 0.25]

    # A PMF precisa somar 1 (axioma da normalização).
    assert abs(sum(probs) - 1.0) < 1e-9

    esperanca = sum(v * p for v, p in zip(valores, probs))
    e_x2 = sum(v * v * p for v, p in zip(valores, probs))
    variancia = e_x2 - esperanca ** 2

    print(f"E[X]   = {esperanca:.4f}")
    print(f"Var[X] = {variancia:.4f}")
    print(f"DP[X]  = {variancia ** 0.5:.4f}")


if __name__ == "__main__":
    main()
