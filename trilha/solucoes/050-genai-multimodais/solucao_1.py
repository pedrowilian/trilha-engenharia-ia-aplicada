"""Solução de referência — Exercício 1 da Lição 050.

Modelo generativo mínimo (bigrama por contagem) com decodificação gulosa
determinística: a partir de uma palavra inicial, gera a sequência escolhendo
sempre a próxima palavra mais provável (desempate alfabético).
"""
from collections import Counter, defaultdict

corpus = "a ia gera texto a ia ajuda pessoas a ia aprende".split()

trans = defaultdict(Counter)
for a, b in zip(corpus, corpus[1:]):
    trans[a][b] += 1


def proximo(palavra):
    candidatos = trans[palavra]
    return max(sorted(candidatos), key=lambda w: candidatos[w])


seq = ["a"]
for _ in range(5):
    seq.append(proximo(seq[-1]))

print("corpus:", " ".join(corpus))
print("gerado:", " ".join(seq))
