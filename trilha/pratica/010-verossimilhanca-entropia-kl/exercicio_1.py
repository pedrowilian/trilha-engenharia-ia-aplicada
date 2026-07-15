"""Lição 010 — Exercício 1: Máxima verossimilhança (MLE) de uma Bernoulli.

Dados (lançamentos de uma moeda; 1 = sucesso, 0 = fracasso):
    dados = [1, 0, 0, 1, 0, 0, 1, 0]   # 3 sucessos, 5 fracassos

Passos:
  1. k = soma dos sucessos; n = número de lançamentos.
  2. Defina log_verossimilhanca(p) = k * log(p) + (n - k) * log(1 - p)  (use math.log).
  3. O estimador de máxima verossimilhança é p* = k / n.
  4. Imprima, nesta ordem:
        k={k} n={n}
        MLE p* = {p*:.4f}
        logL(p*)  = {logL(p*):.4f}
        logL(0.5) = {logL(0.5):.4f}

Critério de conclusão (binário): a saída deve ser EXATAMENTE igual a
`trilha/solucoes/010-verossimilhanca-entropia-kl/solucao_1.saida.txt`.
"""
from math import log


def main() -> None:
    # TODO: implemente os passos acima.
    raise NotImplementedError


if __name__ == "__main__":
    main()
