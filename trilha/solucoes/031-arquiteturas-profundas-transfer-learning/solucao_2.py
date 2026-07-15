"""Solucao de referencia — Licao 031, Exercicio 2.

Fracao de parametros treinaveis em tres estrategias de transfer learning:
fine-tuning completo, feature extraction (so a cabeca) e fine-tuning parcial
(ultimo bloco + cabeca).
"""


def main():
    base = 23_000_000
    ultimo_bloco = 2_000_000
    cabeca = 20_490
    base_congelada = base - ultimo_bloco

    estrategias = [
        ("fine-tuning completo", base + cabeca),
        ("feature extraction", cabeca),
        ("fine-tuning parcial", ultimo_bloco + cabeca),
    ]
    total = base + cabeca
    for nome, treinaveis in estrategias:
        print(f"{nome:22s}: treinaveis={treinaveis:9d} fracao={treinaveis / total:.4%}")


if __name__ == "__main__":
    main()
