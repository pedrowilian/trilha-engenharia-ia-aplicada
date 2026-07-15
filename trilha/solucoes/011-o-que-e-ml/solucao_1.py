"""Solucao de referencia — Licao 011, Exercicio 1.

Classificador supervisionado 1-NN do zero sobre dados rotulados de frutas
(peso_g, indice_de_cor) -> rotulo. Determinístico (sem aleatoriedade).
"""

treino = [
    ((150.0, 0.9), "maca"),
    ((160.0, 0.8), "maca"),
    ((140.0, 0.85), "maca"),
    ((120.0, 0.2), "banana"),
    ((130.0, 0.15), "banana"),
    ((118.0, 0.25), "banana"),
]


def distancia(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def prever(x):
    melhor = min(treino, key=lambda par: distancia(par[0], x))
    return melhor[1]


def main():
    novos = [(155.0, 0.88), (125.0, 0.18), (145.0, 0.7)]
    acertos = 0
    esperado = ["maca", "banana", "maca"]
    for x, alvo in zip(novos, esperado):
        pred = prever(x)
        acertos += int(pred == alvo)
        print(f"x={x} -> {pred}")
    print(f"acertos: {acertos}/3")


if __name__ == "__main__":
    main()
