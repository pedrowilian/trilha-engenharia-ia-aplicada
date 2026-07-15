"""Lição 009 — Exercício 3: Decisão de um teste A/B.

Dados:
    controle: 40 conversoes em 500
    variante: 65 conversoes em 500
    alpha = 0.05

Passos:
  1. Implemente normal_cdf(z) = 0.5 * (1 + erf(z / sqrt(2))).
  2. p_a = 40/500 ; p_b = 65/500
  3. p_pool = (40 + 65) / (500 + 500)
  4. se = sqrt(p_pool * (1 - p_pool) * (1/500 + 1/500))
  5. z = (p_b - p_a) / se
  6. p_valor = 2 * (1 - normal_cdf(abs(z)))
  7. Imprima taxas (4 casas), z (4 casas), p-valor (4 casas) e a decisao
     "rejeita H0 (alpha=0.05)?" com o booleano (p_valor < 0.05).

Critério de conclusão (binário): a saída deve ser EXATAMENTE
    taxa A  = 0.0800
    taxa B  = 0.1300
    z       = 2.5789
    p-valor = 0.0099
    rejeita H0 (alpha=0.05)? True
"""


def main() -> None:
    # TODO: implemente os passos acima.
    raise NotImplementedError


if __name__ == "__main__":
    main()
