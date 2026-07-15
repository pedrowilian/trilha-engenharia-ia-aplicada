"""Solução de referência — Lição 008, Exercício 3.

Teorema de Bayes aplicado a um filtro de spam: dada a presença de uma
palavra-gatilho, atualiza a crença de que a mensagem é spam.
"""


def main() -> None:
    prior_spam = 0.40            # P(spam) antes de observar a palavra
    prior_ham = 1 - prior_spam   # P(ham) = P(nao-spam)

    p_palavra_dado_spam = 0.70   # P(palavra | spam)
    p_palavra_dado_ham = 0.10    # P(palavra | ham)

    # Lei da probabilidade total: P(palavra).
    p_palavra = p_palavra_dado_spam * prior_spam + p_palavra_dado_ham * prior_ham

    # Teorema de Bayes: P(spam | palavra).
    posterior_spam = p_palavra_dado_spam * prior_spam / p_palavra

    print(f"P(palavra)        = {p_palavra:.4f}")
    print(f"P(spam | palavra) = {posterior_spam:.4f}")


if __name__ == "__main__":
    main()
