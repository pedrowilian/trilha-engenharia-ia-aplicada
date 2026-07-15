"""Exercício 1 — Treinar merges de BPE.

Setup:
    corpus = {"low": 5, "lower": 2, "newest": 6, "widest": 3}
    cada palavra inicia como tupla de caracteres + marcador "</w>".

Tarefa:
    1. Implemente contar_pares(vocab) -> Counter de pares adjacentes ponderados.
    2. Implemente fundir_par(vocab, par) que funde todas as ocorrências do par.
    3. Execute 4 merges (par mais frequente; desempate determinístico pelo par)
       e imprima cada merge e a lista final de subpalavras formadas.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/033-tokenizacao/solucao_1.saida.txt
"""
from collections import Counter

corpus = {"low": 5, "lower": 2, "newest": 6, "widest": 3}

# TODO: representar palavras em símbolos, contar pares, fundir e iterar 4 merges.
