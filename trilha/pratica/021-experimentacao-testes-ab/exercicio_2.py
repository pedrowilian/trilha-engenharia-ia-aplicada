"""Licao 021 — Exercicio 2: teste z para duas proporcoes.

Tarefa:
- Implemente phi (CDF normal via math.erf) e z_test_proporcoes(x1,n1,x2,n2)
  usando a proporcao combinada (pooled) no erro-padrao; p-valor bicaudal.
- Compare amostra pequena (33/300 vs 39/300) e grande (660/6000 vs 780/6000).
- Imprima `amostra pequena: z=.. p=.. significativo=..` e a linha analoga para
  a grande (4 casas), e `mais dados detectam o mesmo efeito: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/021-experimentacao-testes-ab/solucao_2.saida.txt
"""
import math


def phi(z):
    raise NotImplementedError


def z_test_proporcoes(x1, n1, x2, n2):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
