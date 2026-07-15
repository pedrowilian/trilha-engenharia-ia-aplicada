"""Lição 008 — Exercício 3: Atualização bayesiana em um filtro de spam.

Dados:
    P(spam)            = 0.40
    P(palavra | spam)  = 0.70
    P(palavra | ham)   = 0.10   (ham = nao-spam)

Passos:
  1. Calcule P(palavra) pela lei da probabilidade total:
        P(palavra) = P(palavra|spam) P(spam) + P(palavra|ham) P(ham)
  2. Aplique o teorema de Bayes:
        P(spam|palavra) = P(palavra|spam) P(spam) / P(palavra)
  3. Imprima, com 4 casas decimais:
        P(palavra)        = <p_palavra>
        P(spam | palavra) = <posterior>

Critério de conclusão (binário): a saída deve ser EXATAMENTE
        P(palavra)        = 0.3400
        P(spam | palavra) = 0.8235
"""


def main() -> None:
    # TODO: implemente os passos acima.
    raise NotImplementedError


if __name__ == "__main__":
    main()
