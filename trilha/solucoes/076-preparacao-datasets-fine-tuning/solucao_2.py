"""Solução de referência — Exercício 2 da Lição 076.

Balanceamento por subamostragem (undersampling): reduz cada classe ao tamanho
da menor classe, de forma reprodutível (semente fixa).
"""
import random
from collections import Counter

exemplos = [
    ("spam", "ganhe dinheiro agora"),
    ("spam", "clique neste link"),
    ("spam", "premio liberado"),
    ("spam", "oferta imperdivel"),
    ("spam", "voce foi sorteado"),
    ("ham", "reuniao as 15h"),
    ("ham", "segue o relatorio"),
]

contagem = Counter(rotulo for rotulo, _ in exemplos)
minimo = min(contagem.values())

rng = random.Random(7)
por_classe = {}
for rotulo, texto in exemplos:
    por_classe.setdefault(rotulo, []).append((rotulo, texto))

balanceado = []
for rotulo in sorted(por_classe):
    grupo = list(por_classe[rotulo])
    rng.shuffle(grupo)
    balanceado.extend(grupo[:minimo])

print("antes :", dict(contagem))
print("minimo:", minimo)
print("depois:", dict(Counter(rotulo for rotulo, _ in balanceado)))
print("total :", len(balanceado))
