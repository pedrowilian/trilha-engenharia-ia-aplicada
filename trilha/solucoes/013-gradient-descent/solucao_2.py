"""Solucao de referencia — Licao 013, Exercicio 2.

Diagnostico da taxa de aprendizado pelo fator de contracao |1 - 2*eta| para
L(theta) = (theta - 5)^2.
  |1 - 2*eta| < 1  -> converge
  |1 - 2*eta| == 0 -> passo unico
  |1 - 2*eta| >= 1 -> nao converge
"""


def classificar(eta):
    fator = abs(1.0 - 2.0 * eta)
    if fator == 0.0:
        return "passo unico"
    if fator < 1.0:
        return "converge"
    return "nao converge"


def main():
    for eta in [0.05, 0.5, 1.0]:
        print(f"{eta} -> {classificar(eta)}")


if __name__ == "__main__":
    main()
