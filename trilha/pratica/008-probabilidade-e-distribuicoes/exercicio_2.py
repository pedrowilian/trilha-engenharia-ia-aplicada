"""Lição 008 — Exercício 2: Esperança e variância de uma VA discreta.

Dado um dado viciado:
    valores = [1, 2, 3, 4, 5, 6]
    probs   = [0.10, 0.10, 0.20, 0.20, 0.15, 0.25]

Passos:
  1. Verifique com assert que a PMF soma 1 (tolerância 1e-9).
  2. Calcule E[X]  = soma de v * P(v).
  3. Calcule E[X2] = soma de v^2 * P(v).
  4. Calcule Var[X] = E[X2] - (E[X])^2 e o desvio padrão sqrt(Var[X]).
  5. Imprima, com 4 casas decimais:
       E[X]   = <esperanca>
       Var[X] = <variancia>
       DP[X]  = <desvio_padrao>

Critério de conclusão (binário): a saída deve ser EXATAMENTE
       E[X]   = 3.9500
       Var[X] = 2.6475
       DP[X]  = 1.6271
"""


def main() -> None:
    # TODO: implemente os passos acima.
    raise NotImplementedError


if __name__ == "__main__":
    main()
