"""Exercício 2 — Balanceamento por subamostragem.

Setup: a lista `exemplos` (abaixo) com pares (rotulo, texto) desbalanceados.

Tarefa:
    Conte os exemplos por classe, determine o tamanho da menor classe e reduza
    cada classe a esse tamanho. Use `random.Random(7)` para embaralhar e
    percorra as classes em ordem alfabética (`sorted`). Imprima `antes`,
    `minimo`, `depois` e `total`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/076-preparacao-datasets-fine-tuning/solucao_2.saida.txt
"""
import random
from collections import Counter

exemplos = [
    ("spam", "ganhe dinheiro agora"),
    ("spam", "clique neste link"),
    ("spam", "premio liberado"),
    ("spam", "oferta imperdivel"),
    ("spam", "voce foi sorteado"),
    ("ham", "reuniao as 15h"),
    ("ham", "segue o relatorio"),
]

# TODO: contar por classe, subamostrar ate o minimo e imprimir o relatório.
