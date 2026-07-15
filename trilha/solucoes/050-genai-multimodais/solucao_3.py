"""Solução de referência — Exercício 3 da Lição 050.

Recuperação tipo CLIP: dada a embedding de uma legenda já projetada no espaço
compartilhado, ordena as imagens candidatas por similaridade do cosseno e
reporta o melhor casamento.
"""
import numpy as np


def cosseno(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


legenda = np.array([0.2, 0.8, 0.3])
imagens = {
    "cachorro": np.array([0.9, 0.1, 0.2]),
    "montanha": np.array([0.1, 0.85, 0.2]),
    "carro":    np.array([0.3, 0.2, 0.9]),
}

sims = {nome: cosseno(legenda, emb) for nome, emb in imagens.items()}
ordenado = sorted(sims, key=sims.get, reverse=True)
for nome in ordenado:
    print(f"{nome:>9}: {sims[nome]:.4f}")
print("melhor match:", ordenado[0])
