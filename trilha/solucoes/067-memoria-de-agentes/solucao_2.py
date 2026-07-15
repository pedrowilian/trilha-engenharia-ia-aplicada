"""Solução de referência — Exercício 2 da Lição 067.

Memória episódica de longo prazo: cada episódio guarda um texto e seu embedding.
Determinístico (embeddings fixos).
"""
import numpy as np

memoria = []


def gravar(texto, vetor):
    memoria.append({"texto": texto, "vetor": np.array(vetor, dtype=float)})


gravar("python e linguagem", [1.0, 0.0, 0.0])
gravar("cobra python", [0.8, 0.2, 0.0])
gravar("cafe quente", [0.0, 0.0, 1.0])

print("episodios:", len(memoria))
for e in memoria:
    print(e["texto"], "->", e["vetor"].tolist())
