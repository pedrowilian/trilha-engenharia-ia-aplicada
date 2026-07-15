"""Solução de referência — Exercício 3 da Lição 034.

Ilustra a diferença entre embedding ESTÁTICO (um vetor fixo por palavra) e
embedding CONTEXTUAL (o vetor depende das palavras vizinhas). Aqui o vetor
contextual é a média do vetor estático da palavra com os de seu contexto.
"""

estatico = {
    "manga": [0.5, 0.5],     # ambígua: fruta ou parte da camisa
    "fruta": [1.0, 0.0],
    "comer": [0.9, 0.1],
    "camisa": [0.0, 1.0],
    "costura": [0.1, 0.9],
}


def contextual(palavra, contexto):
    vecs = [estatico[palavra]] + [estatico[c] for c in contexto]
    n = len(vecs)
    return [round(sum(v[i] for v in vecs) / n, 4) for i in range(2)]


sentido_fruta = contextual("manga", ["comer", "fruta"])
sentido_roupa = contextual("manga", ["camisa", "costura"])
print("estatico de 'manga':", estatico["manga"])
print("contextual (comer, fruta):  ", sentido_fruta)
print("contextual (camisa, costura):", sentido_roupa)
print("o contexto muda a representacao:", sentido_fruta != sentido_roupa)
