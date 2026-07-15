"""Exercicio 2 - Percentis de latencia (p50/p95/p99).

Setup (dado):
    latencias = [200, 210, 190, 205, 195, 800, 215, 198, 202, 207, 199, 700]

Tarefa:
    Implemente percentil(amostras, p) pelo metodo nearest-rank: ordene, calcule
    rank = teto(p/100 * n) (limitado a [1, n]) e retorne o elemento na posicao
    rank-1. Imprima "p50: <n> ms", "p95: <n> ms", "p99: <n> ms",
    depois "media: <1 casa> ms" e "max: <n> ms".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/088-latencia-inferencia/solucao_2.saida.txt
"""
import math

latencias = [200, 210, 190, 205, 195, 800, 215, 198, 202, 207, 199, 700]

# TODO: implemente percentil() por nearest-rank e imprima p50/p95/p99, media e max.
