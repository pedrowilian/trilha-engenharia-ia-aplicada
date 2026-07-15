"""Solucao de referencia — Licao 027, Exercicio 1.

Classifica o destino do gradiente apos 30 camadas para tres fatores tipicos:
fator < 1 some (vanishing), fator = 1 estabiliza, fator > 1 explode.
"""


def classificar(grad):
    if grad < 1e-3:
        return "vanishing"
    if grad > 1e3:
        return "exploding"
    return "estavel"


def main():
    L = 30
    for fator in [0.5, 1.0, 1.5]:
        grad = fator ** L
        print(f"fator={fator}: grad={grad:.3e} -> {classificar(grad)}")


if __name__ == "__main__":
    main()
