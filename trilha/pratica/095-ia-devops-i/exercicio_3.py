"""Exercício 3 — Troubleshooting estilo ReAct sobre uma base de conhecimento.

Setup:
    base = {
        "fila_cheia": ("escalar_workers", "cpu_alta"),
        "cpu_alta": ("otimizar_query", "ok"),
    }
    sintoma inicial = "fila_cheia".

Tarefa:
    Implemente `diagnosticar(sintoma_inicial, max_passos=5)` que, a cada passo,
    se o estado não for "ok", consulta a base `(acao, proximo)`, registra
    "estado -> acao" e avança para `proximo`. Imprima cada passo e o estado
    final ("estado final: ...").

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/095-ia-devops-i/solucao_3.saida.txt.
"""

base = {
    "fila_cheia": ("escalar_workers", "cpu_alta"),
    "cpu_alta": ("otimizar_query", "ok"),
}

# TODO: implemente diagnosticar; imprima os passos e o estado final.
