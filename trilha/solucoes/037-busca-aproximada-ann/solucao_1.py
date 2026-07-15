"""Solução de referência — Exercício 1 da Lição 037.

Implementa a métrica de qualidade da busca aproximada: o recall@k, fração dos k
vizinhos verdadeiros (do k-NN exato) que a busca aproximada recuperou.
"""


def recall_at_k(aprox, exato):
    return len(set(aprox) & set(exato)) / len(exato)


casos = [
    (["d3", "d1", "d7"], ["d3", "d1", "d7"]),   # idêntico ao exato
    (["d3", "d1", "d9"], ["d3", "d1", "d7"]),   # erra 1 dos 3
    (["d9", "d8", "d5"], ["d3", "d1", "d7"]),   # erra todos
]
for aprox, exato in casos:
    print(f"aprox={aprox} exato={exato} recall@3={recall_at_k(aprox, exato):.4f}")
