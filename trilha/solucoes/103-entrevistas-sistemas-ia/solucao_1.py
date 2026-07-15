"""Solucao de referencia - Exercicio 1 da Licao 103.

Metricas de recuperacao (RAG): precision@k, recall@k e MRR. Avaliar o retriever
isoladamente e o primeiro passo de qualquer avaliacao seria de RAG - se o
documento certo nao entra no contexto, o gerador nao tem como acertar.
"""


def metricas(recuperados, relevantes, k):
    topk = recuperados[:k]
    acertos = [d for d in topk if d in relevantes]
    precision = len(acertos) / k
    recall = len(acertos) / len(relevantes)
    rr = 0.0
    for i, d in enumerate(recuperados, 1):
        if d in relevantes:
            rr = 1.0 / i
            break
    return precision, recall, rr


recuperados = ["d5", "d2", "d8", "d1", "d4", "d7"]
relevantes = {"d1", "d2", "d4"}
for k in [1, 3, 6]:
    p, r, rr = metricas(recuperados, relevantes, k)
    print(f"@{k}: precision={p:.2f} recall={r:.2f} mrr={rr:.2f}")
