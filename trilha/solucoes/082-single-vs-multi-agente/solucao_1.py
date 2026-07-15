"""Solução de referência — Exercício 1 da Lição 082.

Custo de coordenação: single (n*t) vs multi (n*t + n*h). Determinístico.
"""


def custo_single(n, t):
    return n * t


def custo_multi(n, t, h):
    return n * t + n * h


tokens_por_subtarefa = 80
overhead_handoff = 30

for n in [2, 4, 6]:
    s = custo_single(n, tokens_por_subtarefa)
    m = custo_multi(n, tokens_por_subtarefa, overhead_handoff)
    print(f"subtarefas={n}: single={s} multi={m} overhead={m - s}")
