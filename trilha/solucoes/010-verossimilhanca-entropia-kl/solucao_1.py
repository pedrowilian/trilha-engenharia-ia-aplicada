"""Solução de referência — Lição 010, Exercício 1.

Estimação de máxima verossimilhança (MLE) para uma Bernoulli: dado um conjunto
de lançamentos, o p que maximiza a log-verossimilhança é a média amostral k/n.
"""
from math import log


def main() -> None:
    dados = [1, 0, 0, 1, 0, 0, 1, 0]   # 3 sucessos, 5 fracassos
    k = sum(dados)
    n = len(dados)

    def log_verossimilhanca(p: float) -> float:
        # log L(p) = k log p + (n - k) log(1 - p)
        return k * log(p) + (n - k) * log(1 - p)

    p_mle = k / n

    print(f"k={k} n={n}")
    print(f"MLE p* = {p_mle:.4f}")
    print(f"logL(p*)  = {log_verossimilhanca(p_mle):.4f}")
    print(f"logL(0.5) = {log_verossimilhanca(0.5):.4f}")


if __name__ == "__main__":
    main()
