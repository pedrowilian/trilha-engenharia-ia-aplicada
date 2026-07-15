"""Solucao de referencia — Licao 012, Exercicio 2.

Entropia cruzada binaria media (BCE) sobre um lote de predicoes, e demonstracao
de que uma unica predicao confiante e errada domina a perda.
"""
import math


def bce_media(ys, ps, eps=1e-12):
    total = 0.0
    for y, p in zip(ys, ps):
        p = min(max(p, eps), 1 - eps)
        total += -(y * math.log(p) + (1 - y) * math.log(1 - p))
    return total / len(ys)


def main():
    ys = [1, 0, 1, 0]
    ps_bom = [0.9, 0.1, 0.8, 0.2]
    ps_ruim = [0.9, 0.1, 0.8, 0.99]   # ultimo: y=0 mas previu 0.99
    print(f"BCE lote bom:  {bce_media(ys, ps_bom):.4f}")
    print(f"BCE lote ruim: {bce_media(ys, ps_ruim):.4f}")
    print("erro confiante domina:", bce_media(ys, ps_ruim) > 2 * bce_media(ys, ps_bom))


if __name__ == "__main__":
    main()
