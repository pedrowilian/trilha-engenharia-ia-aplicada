"""Solução de referência — Lição 010, Exercício 3.

Divergência KL e a identidade que liga entropia cruzada, entropia e KL:
    H(p, q) = H(p) + KL(p || q).
"""
from math import log2


def entropia(d: list[float]) -> float:
    return -sum(p * log2(p) for p in d if p > 0)


def cross_entropy(p: list[float], q: list[float]) -> float:
    return -sum(pi * log2(qi) for pi, qi in zip(p, q) if pi > 0)


def kl(p: list[float], q: list[float]) -> float:
    return sum(pi * log2(pi / qi) for pi, qi in zip(p, q) if pi > 0)


def main() -> None:
    p = [0.7, 0.2, 0.1]
    q = [0.5, 0.3, 0.2]

    print(f"KL(p||q)      = {kl(p, q):.4f}")
    print(f"H(p,q)        = {cross_entropy(p, q):.4f}")
    print(f"H(p)+KL(p||q) = {entropia(p) + kl(p, q):.4f}")
    print("identidade ok?", round(cross_entropy(p, q), 9) == round(entropia(p) + kl(p, q), 9))


if __name__ == "__main__":
    main()
