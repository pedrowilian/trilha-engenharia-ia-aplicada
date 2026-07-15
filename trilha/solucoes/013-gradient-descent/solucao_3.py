"""Solucao de referencia — Licao 013, Exercicio 3.

Comparacao de batch, mini-batch e SGD sobre regressao linear y = w*x.
Todas convergem para o mesmo w; muda o numero de atualizacoes por epoca.
"""

X = [1.0, 2.0, 3.0, 4.0, 5.0]
Y = [2.0, 4.0, 6.0, 8.0, 10.0]


def grad_subconjunto(w, idxs):
    n = len(idxs)
    return (2.0 / n) * sum((w * X[i] - Y[i]) * X[i] for i in idxs)


def treinar(tamanho_lote, epocas=300, eta=0.01):
    w = 0.0
    atualizacoes = 0
    for _ in range(epocas):
        for inicio in range(0, len(X), tamanho_lote):
            idxs = list(range(inicio, min(inicio + tamanho_lote, len(X))))
            w = w - eta * grad_subconjunto(w, idxs)
            atualizacoes += 1
    return w, atualizacoes


def main():
    for nome, lote in [("batch", 5), ("mini-batch", 2), ("sgd", 1)]:
        w, n = treinar(lote)
        print(f"{nome:>10}: w={w:.2f} atualizacoes={n}")


if __name__ == "__main__":
    main()
