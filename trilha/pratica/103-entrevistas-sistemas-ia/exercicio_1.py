"""Exercicio 1 - Metricas de recuperacao (precision@k, recall@k, MRR).

Setup (dado):
    recuperados = ["d5", "d2", "d8", "d1", "d4", "d7"]   # ranking do retriever
    relevantes  = {"d1", "d2", "d4"}

Tarefa:
    Implemente metricas(recuperados, relevantes, k) retornando
        precision = acertos_no_topk / k
        recall    = acertos_no_topk / len(relevantes)
        rr        = 1 / rank_do_primeiro_relevante (0 se nenhum).
    Para k em [1, 3, 6] imprima "@<k>: precision=<2c> recall=<2c> mrr=<2c>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/103-entrevistas-sistemas-ia/solucao_1.saida.txt
"""

recuperados = ["d5", "d2", "d8", "d1", "d4", "d7"]
relevantes = {"d1", "d2", "d4"}

# TODO: implemente metricas() e imprima precision/recall/mrr para k em [1, 3, 6].
