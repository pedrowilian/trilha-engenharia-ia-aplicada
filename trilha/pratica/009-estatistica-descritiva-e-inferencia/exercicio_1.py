"""Lição 009 — Exercício 1: Medidas descritivas e o divisor n-1.

Amostra:
    dados = [2, 4, 4, 4, 5, 5, 7, 9]

Passos (use o modulo `statistics`):
  1. media   = soma / n
  2. mediana = statistics.median(dados)
  3. var_populacional = statistics.pvariance(dados)   # divisor n
  4. var_amostral     = statistics.variance(dados)    # divisor n-1
  5. desvio_amostral  = statistics.stdev(dados)
  6. Imprima cada valor com 4 casas decimais.

Critério de conclusão (binário): a saída deve ser EXATAMENTE
    media               = 5.0000
    mediana             = 4.5000
    var (populacional)  = 4.0000
    var (amostral)      = 4.5714
    desvio (amostral)   = 2.1381
"""


def main() -> None:
    # TODO: implemente os passos acima.
    raise NotImplementedError


if __name__ == "__main__":
    main()
