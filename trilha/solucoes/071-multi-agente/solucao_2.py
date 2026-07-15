"""Solução de referência — Exercício 2 da Lição 071.

Topologias multi-agente: número de canais de comunicação em função do número de
agentes, para supervisor (estrela), hierárquica (árvore) e group-chat (completa).
Determinístico.
"""


def arestas_supervisor(n):
    return n


def arestas_hierarquica(nos):
    return nos - 1


def arestas_grupo(n):
    return n * (n - 1) // 2


for n in [3, 5]:
    print(f"n={n}: supervisor={arestas_supervisor(n)} "
          f"hierarquica={arestas_hierarquica(n)} grupo={arestas_grupo(n)}")
