"""Exercício 3 — Monitorar treino e usar o modelo ajustado.

Setup: 4 passos de treino, perda inicial 2.0, decaimento 0.8.

Tarefa:
    Implemente `monitorar(passos, perda_inicial=2.0, decaimento=0.8)` que
    devolve a lista de (passo, round(perda, 4)), o status "succeeded" e o nome
    "ft:base-mini:org::abc123". Imprima `passo {p}: train_loss={perda}` por
    passo, o status e o modelo; depois implemente `responder(modelo, pergunta)`
    devolvendo `f"[{modelo}] -> {pergunta.upper()}"` e imprima a resposta para
    "ola mundo".

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/079-fine-tuning-openai-api/solucao_3.saida.txt
"""

# TODO: implementar monitorar(...) e responder(...) e imprimir o relatório.
