"""Solucao de referencia — Licao 013, Exercicio 1.

Gradient descent 1D do zero sobre L(theta) = (theta - 5)^2.
"""


def perda(theta):
    return (theta - 5.0) ** 2


def gradiente(theta):
    return 2.0 * (theta - 5.0)


def main():
    theta = 0.0
    eta = 0.1
    for _ in range(100):
        theta = theta - eta * gradiente(theta)
    print(f"theta final: {theta:.4f}")


if __name__ == "__main__":
    main()
