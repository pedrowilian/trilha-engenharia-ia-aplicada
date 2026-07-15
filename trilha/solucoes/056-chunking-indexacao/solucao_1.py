"""Solucao de referencia - Exercicio 1 da Licao 056.

Chunking de tamanho fixo: parte a lista de tokens em blocos contiguos de
tamanho fixo, sem sobreposicao. E a estrategia de chunking mais simples.
"""
import re


texto = ("o gato dorme no sofa o cachorro corre no parque "
         "o passaro voa alto no ceu azul")


def tokenizar(t):
    return re.findall(r"[a-z0-9]+", t.lower())


def chunk_fixo(tokens, tamanho):
    return [tokens[i:i + tamanho] for i in range(0, len(tokens), tamanho)]


tokens = tokenizar(texto)
chunks = chunk_fixo(tokens, 5)
for i, c in enumerate(chunks):
    print(f"c{i}: {' '.join(c)}")
print("n_chunks:", len(chunks))
