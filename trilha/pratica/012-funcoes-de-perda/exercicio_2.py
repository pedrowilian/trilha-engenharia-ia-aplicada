"""Licao 012 — Exercicio 2: entropia cruzada binaria media (BCE).

Tarefa:
- Implemente `bce_media(ys, ps)` com clamp em [eps, 1-eps] para evitar log(0).
- Compare `ps_bom` e `ps_ruim` (ultimo caso: y=0 mas previu 0.99) sobre `ys`.
- Imprima `BCE lote bom: ...`, `BCE lote ruim: ...` (4 casas) e
  `erro confiante domina: <bool>` (BCE_ruim > 2 * BCE_bom).

Criterio binario: saida IDENTICA a
trilha/solucoes/012-funcoes-de-perda/solucao_2.saida.txt
"""
import math

ys = [1, 0, 1, 0]
ps_bom = [0.9, 0.1, 0.8, 0.2]
ps_ruim = [0.9, 0.1, 0.8, 0.99]


def bce_media(ys, ps, eps=1e-12):
    raise NotImplementedError


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
