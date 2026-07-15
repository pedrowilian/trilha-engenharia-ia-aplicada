"""Licao 024 — Exercicio 3: contar parametros de um MLP.

Tarefa:
- Para a arquitetura camadas = [3, 5, 5, 2], calcule o numero de parametros
  treinaveis de cada camada densa: n_in*n_out + n_out (pesos + vieses).
- Imprima, por camada, `camada n_in->n_out: n_in*n_out+n_out = P parametros`
  e ao final `total de parametros: T`.

Criterio binario: saida IDENTICA a
trilha/solucoes/024-mlp/solucao_3.saida.txt
"""


def parametros_por_camada(n_in, n_out):
    return n_in * n_out + n_out


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
