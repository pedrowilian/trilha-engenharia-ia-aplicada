"""Lição 009 — Exercício 2: Erro padrão e intervalo de confiança.

Dados:
    media_amostral = 2.5
    desvio_padrao  = 1.2
    n              = 64
    z              = 1.96

Passos:
  1. erro_padrao = desvio_padrao / sqrt(n)
  2. ic_inf = media_amostral - z * erro_padrao
  3. ic_sup = media_amostral + z * erro_padrao
  4. Imprima, com 4 casas decimais:
        erro padrao = <erro_padrao>
        IC 95% = [<ic_inf>, <ic_sup>]

Critério de conclusão (binário): a saída deve ser EXATAMENTE
        erro padrao = 0.1500
        IC 95% = [2.2060, 2.7940]
"""


def main() -> None:
    # TODO: implemente os passos acima.
    raise NotImplementedError


if __name__ == "__main__":
    main()
