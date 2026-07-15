"""Exercício 2 — TF-IDF com IDF suavizado.

Setup:
    corpus = ["o gato dorme", "o cachorro corre", "o gato corre"]
    doc alvo = "o gato dorme"

Definições:
    tf(t, d)  = contagem de t em d / total de tokens em d
    idf(t)    = ln((1 + N) / (1 + df(t))) + 1
    tfidf     = tf * idf

Tarefa:
    Implemente tf, doc_freq, idf e tfidf e imprima df, idf e tfidf
    dos termos "o", "gato" e "dorme" com 4 casas decimais.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/032-nlp-fundamentos/solucao_2.saida.txt
"""
import math

corpus = [
    "o gato dorme",
    "o cachorro corre",
    "o gato corre",
]

# TODO: implementar tf, doc_freq, idf, tfidf e imprimir as métricas dos termos.
