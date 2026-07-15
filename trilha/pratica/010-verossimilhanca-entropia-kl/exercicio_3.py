"""Lição 010 — Exercício 3: Divergência KL e a identidade fundamental.

Mostre numericamente a identidade que liga entropia cruzada, entropia e KL:
    H(p, q) = H(p) + KL(p || q)

Setup:
    p = [0.7, 0.2, 0.1]
    q = [0.5, 0.3, 0.2]

Passos (use math.log2; some apenas sobre termos com p_i > 0):
  1. entropia(d)         = -sum(p * log2(p))
  2. cross_entropy(p, q) = -sum(p_i * log2(q_i))
  3. kl(p, q)            =  sum(p_i * log2(p_i / q_i))
  4. Imprima, nesta ordem:
        KL(p||q)      = {kl:.4f}
        H(p,q)        = {cross_entropy:.4f}
        H(p)+KL(p||q) = {entropia(p)+kl:.4f}
        identidade ok? {True/False}   # compare arredondando a 9 casas

Critério de conclusão (binário): a saída deve ser EXATAMENTE igual a
`trilha/solucoes/010-verossimilhanca-entropia-kl/solucao_3.saida.txt`
(em particular, `identidade ok? True`).
"""
from math import log2


def main() -> None:
    # TODO: implemente entropia, cross_entropy e kl; imprima os 4 valores.
    raise NotImplementedError


if __name__ == "__main__":
    main()
