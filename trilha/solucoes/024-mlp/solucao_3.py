"""Solucao de referencia — Licao 024, Exercicio 3.

Conta os parametros treinaveis de um MLP a partir dos tamanhos das camadas.
Cada camada densa (n_in -> n_out) tem n_in*n_out pesos + n_out vieses.
"""


def parametros_por_camada(n_in, n_out):
    return n_in * n_out + n_out


def main():
    camadas = [3, 5, 5, 2]   # entrada, oculta, oculta, saida
    total = 0
    for i in range(len(camadas) - 1):
        n_in, n_out = camadas[i], camadas[i + 1]
        p = parametros_por_camada(n_in, n_out)
        total += p
        print(f"camada {n_in}->{n_out}: {n_in}*{n_out}+{n_out} = {p} parametros")
    print(f"total de parametros: {total}")


if __name__ == "__main__":
    main()
