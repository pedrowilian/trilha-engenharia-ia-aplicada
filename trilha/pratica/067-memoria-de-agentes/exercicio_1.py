"""Exercício 1 — Memória de curto prazo (buffer de tamanho fixo).

Setup: eventos = ["p1", "p2", "p3", "p4"]; capacidade do buffer = 2.

Tarefa:
    Use um `deque(maxlen=2)`. A cada evento adicionado, imprima
    `buffer: {lista atual}`. Ao final, imprima `janela final: {lista}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/067-memoria-de-agentes/solucao_1.saida.txt
"""
from collections import deque

eventos = ["p1", "p2", "p3", "p4"]

# TODO: implemente o buffer de curto prazo.
