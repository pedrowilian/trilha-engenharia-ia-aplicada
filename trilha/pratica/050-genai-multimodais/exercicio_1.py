"""Exercício 1 — Geração gulosa com um bigrama.

Setup: o `corpus` abaixo (lista de palavras) e a palavra inicial "a".

Tarefa:
    Treine um bigrama por contagem (palavra -> Counter de próximas palavras).
    Implemente `proximo(palavra)` que devolve a próxima palavra mais provável,
    com desempate alfabético (use `max(sorted(candidatos), key=...)`).
    A partir de "a", gere 5 palavras e imprima:
        corpus: a ia gera texto ...
        gerado: a ia ajuda pessoas a ia

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/050-genai-multimodais/solucao_1.saida.txt
"""
from collections import Counter, defaultdict

corpus = "a ia gera texto a ia ajuda pessoas a ia aprende".split()

# TODO: treinar o bigrama, implementar proximo() e gerar a sequencia.
