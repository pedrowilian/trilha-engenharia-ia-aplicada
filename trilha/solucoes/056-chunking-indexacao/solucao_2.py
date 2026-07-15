"""Solucao de referencia - Exercicio 2 da Licao 056.

Janela deslizante (sliding window): chunks de tamanho fixo com sobreposicao
controlada por um passo menor que o tamanho. A sobreposicao preserva contexto
que cairia exatamente sobre a borda de um chunk de tamanho fixo.
"""
import re


texto = "termo a termo b termo c termo d termo e termo f"


def tokenizar(t):
    return re.findall(r"[a-z0-9]+", t.lower())


def chunk_sobreposto(tokens, tamanho, passo):
    chunks = []
    i = 0
    while i < len(tokens):
        chunks.append(tokens[i:i + tamanho])
        if i + tamanho >= len(tokens):
            break
        i += passo
    return chunks


tokens = tokenizar(texto)
chunks = chunk_sobreposto(tokens, 4, 2)
for i, c in enumerate(chunks):
    print(f"j{i}: {' '.join(c)}")
print("n_chunks:", len(chunks))
