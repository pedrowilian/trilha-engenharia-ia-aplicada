"""Exercicio 3 - Fusao por Reciprocal Rank Fusion (RRF).

Setup (dado):
    denso   = ["d3", "d1", "d5", "d2"]
    esparso = ["d1", "d4", "d3", "d6"]

Tarefa:
    Implemente rrf(listas, k=60): para cada lista e cada documento, soma
    1/(k + posicao) (posicao comeca em 1); ordena por (-score, id). Imprima
    "RRF (k=60):", uma linha "<id> <score 6 casas>" por documento na ordem
    fundida e, por fim, "fusao final: <ids>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/059-rag-hibrido/solucao_3.saida.txt
"""
denso = ["d3", "d1", "d5", "d2"]
esparso = ["d1", "d4", "d3", "d6"]

# TODO: implemente rrf(listas, k=60) e imprima a fusao das duas listas.
