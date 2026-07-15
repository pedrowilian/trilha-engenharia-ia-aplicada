"""Solucao de referencia — Licao 029, Exercicio 3.

Tamanho espacial da saida de uma convolucao:
    out = (n + 2*p - k) // s + 1
para entrada n, kernel k, stride s e padding p.
"""


def dim_saida(n, k, s, p):
    return (n + 2 * p - k) // s + 1


def main():
    configs = [
        (32, 3, 1, 0),   # sem padding
        (32, 3, 1, 1),   # "same" padding
        (28, 5, 2, 0),   # stride 2
    ]
    for n, k, s, p in configs:
        out = dim_saida(n, k, s, p)
        print(f"n={n} k={k} s={s} p={p} -> out={out}")


if __name__ == "__main__":
    main()
