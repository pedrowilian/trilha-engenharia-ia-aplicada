"""Solução de referência — Lição 010, Exercício 2.

Entropia e entropia cruzada (em bits): a entropia mede a incerteza de uma
distribuição; a entropia cruzada mede o custo de codificar p usando q — é
exatamente a função de perda de classificação.
"""
from math import log2


def entropia(dist: list[float]) -> float:
    return -sum(p * log2(p) for p in dist if p > 0)


def cross_entropy(p: list[float], q: list[float]) -> float:
    return -sum(pi * log2(qi) for pi, qi in zip(p, q) if pi > 0)


def main() -> None:
    p = [1, 0]          # rotulo verdadeiro (one-hot): classe 0
    q1 = [0.9, 0.1]     # previsao boa
    q2 = [0.5, 0.5]     # previsao indecisa

    print(f"H([0.5, 0.5]) = {entropia([0.5, 0.5]):.4f}")
    print(f"H(p, q1) = {cross_entropy(p, q1):.4f}")
    print(f"H(p, q2) = {cross_entropy(p, q2):.4f}")


if __name__ == "__main__":
    main()
