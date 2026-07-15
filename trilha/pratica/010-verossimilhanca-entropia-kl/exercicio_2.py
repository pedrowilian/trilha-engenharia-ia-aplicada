"""Lição 010 — Exercício 2: Entropia e entropia cruzada (em bits).

A entropia mede a incerteza de uma distribuição; a entropia cruzada mede o custo
de codificar a distribuição verdadeira p usando as probabilidades previstas q —
é exatamente a perda de classificação (cross-entropy loss).

Setup:
    p  = [1, 0]        # rótulo verdadeiro (one-hot): classe 0
    q1 = [0.9, 0.1]    # previsão boa
    q2 = [0.5, 0.5]    # previsão indecisa

Passos (use math.log2; some apenas sobre termos com probabilidade > 0):
  1. entropia(dist)        = -sum(p * log2(p))
  2. cross_entropy(p, q)   = -sum(p_i * log2(q_i))
  3. Imprima, nesta ordem:
        H([0.5, 0.5]) = {...:.4f}
        H(p, q1) = {...:.4f}
        H(p, q2) = {...:.4f}

Critério de conclusão (binário): a saída deve ser EXATAMENTE igual a
`trilha/solucoes/010-verossimilhanca-entropia-kl/solucao_2.saida.txt`.
"""
from math import log2


def main() -> None:
    # TODO: implemente entropia(dist) e cross_entropy(p, q) e imprima os 3 valores.
    raise NotImplementedError


if __name__ == "__main__":
    main()
