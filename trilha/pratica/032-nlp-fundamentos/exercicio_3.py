"""Exercício 3 — N-grams e bigrama mais frequente.

Setup:
    frase  = "o gato e o cachorro"
    corpus = ["o gato corre", "o gato dorme", "o cachorro corre"]

Tarefa:
    1. Implemente n_grams(tokens, n) -> lista de tuplas contíguas.
    2. Imprima 1-grams, 2-grams e 3-grams da frase.
    3. Conte os bigramas do corpus com collections.Counter e imprima o mais
       frequente e sua contagem (esperado: "o gato -> 2").

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/032-nlp-fundamentos/solucao_3.saida.txt
"""
from collections import Counter

frase = "o gato e o cachorro"
corpus = ["o gato corre", "o gato dorme", "o cachorro corre"]

# TODO: implementar n_grams, imprimir os n-grams e o bigrama mais frequente.
