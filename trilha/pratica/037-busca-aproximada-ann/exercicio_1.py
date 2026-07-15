"""Exercício 1 — Medir recall@k.

Setup:
    casos = [
        (["d3", "d1", "d7"], ["d3", "d1", "d7"]),   # idêntico
        (["d3", "d1", "d9"], ["d3", "d1", "d7"]),   # erra 1 de 3
        (["d9", "d8", "d5"], ["d3", "d1", "d7"]),   # erra todos
    ]

Tarefa:
    Implemente recall_at_k(aprox, exato) = |interseção| / len(exato) e imprima,
    para cada caso, aprox, exato e o recall@3 com 4 casas.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/037-busca-aproximada-ann/solucao_1.saida.txt
"""

casos = [
    (["d3", "d1", "d7"], ["d3", "d1", "d7"]),
    (["d3", "d1", "d9"], ["d3", "d1", "d7"]),
    (["d9", "d8", "d5"], ["d3", "d1", "d7"]),
]

# TODO: implementar recall_at_k e imprimir o recall@3 de cada caso.
