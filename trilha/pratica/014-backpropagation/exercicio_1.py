"""Licao 014 — Exercicio 1: backprop em grafo computacional.

Tarefa:
- Para f = (a + b) * (b + c) com a=1, b=2, c=3, faca o forward guardando os
  intermediarios u=a+b e v=b+c, e f=u*v.
- Faca o backward pela regra da cadeia. ATENCAO: b alimenta DOIS caminhos (u e v),
  entao df/db e a SOMA das duas contribuicoes.
- Imprima `forward: u=... v=... f=...` e `df/da=... df/db=... df/dc=...`.

Criterio binario: saida IDENTICA a
trilha/solucoes/014-backpropagation/solucao_1.saida.txt
"""


def main():
    a, b, c = 1.0, 2.0, 3.0
    raise NotImplementedError


if __name__ == "__main__":
    main()
