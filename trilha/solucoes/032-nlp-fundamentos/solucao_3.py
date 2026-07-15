"""Solução de referência — Exercício 3 da Lição 032.

Gera n-grams de palavras (unigrams, bigrams, trigrams) de uma frase e conta
os bigramas mais frequentes em um pequeno corpus.
"""
from collections import Counter


def tokenizar(texto):
    return texto.lower().split()


def n_grams(tokens, n):
    return [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]


frase = "o gato e o cachorro"
toks = tokenizar(frase)
for n in (1, 2, 3):
    grams = n_grams(toks, n)
    print(f"{n}-grams ({len(grams)}): {[' '.join(g) for g in grams]}")

corpus = ["o gato corre", "o gato dorme", "o cachorro corre"]
contador = Counter()
for doc in corpus:
    contador.update(n_grams(tokenizar(doc), 2))
print("bigrama mais comum:", " ".join(contador.most_common(1)[0][0]),
      "->", contador.most_common(1)[0][1])
