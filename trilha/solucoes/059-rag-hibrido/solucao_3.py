"""Solucao de referencia - Exercicio 3 da Licao 059.

Fusao por Reciprocal Rank Fusion (RRF): combina varias listas ranqueadas somando
1/(k + posicao) de cada documento em cada lista. Independe da escala das
pontuacoes (so usa posicoes), o que a torna robusta para fundir denso e esparso.
"""
denso = ["d3", "d1", "d5", "d2"]
esparso = ["d1", "d4", "d3", "d6"]


def rrf(listas, k=60):
    score = {}
    for lista in listas:
        for posicao, did in enumerate(lista, start=1):
            score[did] = score.get(did, 0.0) + 1.0 / (k + posicao)
    return sorted(score.items(), key=lambda t: (-t[1], t[0]))


fusao = rrf([denso, esparso], k=60)
print("RRF (k=60):")
for did, s in fusao:
    print(f"{did} {s:.6f}")
print("fusao final:", [did for did, _ in fusao])
