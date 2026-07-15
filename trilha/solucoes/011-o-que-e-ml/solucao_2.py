"""Solucao de referencia — Licao 011, Exercicio 2.

k-means (k=2) do zero sobre pontos 1D, sem rotulos. Roda ate os centroides
estabilizarem e imprime o numero de iteracoes e o resultado final.
"""

dados = [2.0, 2.5, 3.0, 10.0, 10.5, 11.0, 11.5]
centroides = [0.0, 20.0]   # inicializacao deterministica


def atribuir(dados, centroides):
    grupos = {0: [], 1: []}
    for x in dados:
        c = 0 if abs(x - centroides[0]) <= abs(x - centroides[1]) else 1
        grupos[c].append(x)
    return grupos


def main():
    cents = list(centroides)
    iteracoes = 0
    while True:
        grupos = atribuir(dados, cents)
        novos = [sum(grupos[c]) / len(grupos[c]) for c in (0, 1)]
        iteracoes += 1
        if novos == cents:
            break
        cents = novos
    print(f"iteracoes ate convergir: {iteracoes}")
    print(f"centroides finais: [{cents[0]:.4f}, {cents[1]:.4f}]")
    print("grupo 0:", grupos[0])
    print("grupo 1:", grupos[1])


if __name__ == "__main__":
    main()
