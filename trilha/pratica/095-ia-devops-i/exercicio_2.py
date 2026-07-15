"""Exercício 2 — AIOps: detecção de anomalias por z-score robusto.

Setup: serie = [50, 52, 51, 49, 50, 51, 120, 50, 49, 51], limiar k = 3.5.

Tarefa:
    Implemente `mediana(xs)` e `detectar(serie, k=3.5)`. O escore robusto usa a
    mediana e o MAD escalado (mediana dos desvios absolutos × 1.4826). Sinalize
    como anomalia todo índice cujo |x - mediana| / MAD > k. Imprima
    `mediana:` e `anomalias:` (lista de índices).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/095-ia-devops-i/solucao_2.saida.txt.
"""

serie = [50, 52, 51, 49, 50, 51, 120, 50, 49, 51]

# TODO: implemente mediana e detectar; imprima mediana e anomalias.
