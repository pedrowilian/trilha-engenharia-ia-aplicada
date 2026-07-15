"""Exercício 1 — Tracing de execução.

Setup: registre, nesta ordem, os eventos
    ("inicio", "tarefa"), ("tool_call", "calc"), ("fim", "ok").

Tarefa:
    Implemente `registrar(evento, detalhe)` acrescentando a `trace` um dict com
    `passo` (1-indexado), `evento` e `detalhe`. Depois imprima cada span como
    `[{passo}] {evento}: {detalhe}` e `total de eventos: {n}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/070-observabilidade-limites/solucao_1.saida.txt
"""

trace = []

# TODO: implemente registrar e produza o traço.
