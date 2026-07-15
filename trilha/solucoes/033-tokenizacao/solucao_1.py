"""Solução de referência — Exercício 1 da Lição 033.

Treina um Byte-Pair Encoding (BPE) didático: parte de palavras como sequências
de caracteres (com marcador de fim de palavra '</w>') e funde, repetidamente, o
par de símbolos adjacentes mais frequente do corpus.
"""
from collections import Counter

# Corpus clássico de BPE: palavra -> frequência.
corpus = {"low": 5, "lower": 2, "newest": 6, "widest": 3}


def palavra_em_simbolos(palavra):
    return tuple(list(palavra) + ["</w>"])


def contar_pares(vocab):
    pares = Counter()
    for simbolos, freq in vocab.items():
        for i in range(len(simbolos) - 1):
            pares[(simbolos[i], simbolos[i + 1])] += freq
    return pares


def fundir_par(vocab, par):
    novo = {}
    for simbolos, freq in vocab.items():
        fundido = []
        i = 0
        while i < len(simbolos):
            if i < len(simbolos) - 1 and (simbolos[i], simbolos[i + 1]) == par:
                fundido.append(simbolos[i] + simbolos[i + 1])
                i += 2
            else:
                fundido.append(simbolos[i])
                i += 1
        novo[tuple(fundido)] = freq
    return novo


vocab = {palavra_em_simbolos(p): f for p, f in corpus.items()}
merges = []
for passo in range(4):
    pares = contar_pares(vocab)
    melhor = max(pares.items(), key=lambda kv: (kv[1], kv[0]))[0]
    merges.append(melhor)
    vocab = fundir_par(vocab, melhor)
    print(f"merge {passo + 1}: {melhor[0]!r}+{melhor[1]!r} (freq {pares[melhor]})")

print("merges:", [a + b for a, b in merges])
