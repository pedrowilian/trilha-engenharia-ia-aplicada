"""Solucao de referencia - Exercicio 1 da Licao 104.

Top-k palavras mais frequentes (manipulacao de strings + contagem). Padrao
classico de live coding com sabor de NLP: contar, ordenar com desempate
deterministico e cortar o top-k. Complexidade O(n log n) pela ordenacao.
"""
from collections import Counter


def top_k_palavras(texto, k):
    palavras = texto.lower().split()
    contagem = Counter(palavras)
    return sorted(contagem.items(), key=lambda kv: (-kv[1], kv[0]))[:k]


texto = "embedding token embedding rag token embedding rag chunk rag"
for palavra, freq in top_k_palavras(texto, 3):
    print(f"{palavra}: {freq}")
