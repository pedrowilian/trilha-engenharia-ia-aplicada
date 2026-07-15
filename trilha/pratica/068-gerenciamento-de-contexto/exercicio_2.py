"""Exercício 2 — Truncamento por recência.

Setup:
    sistema = "assistente util"
    historico = ["passo um inicial", "passo dois meio", "passo tres final"]
    limite = 8

Tarefa:
    Mantenha sempre o `sistema`. Percorra o histórico das mensagens mais
    recentes para as mais antigas, incluindo cada uma enquanto o total de tokens
    couber no `limite`; pare ao estourar. Restaure a ordem cronológica das
    incluídas. Imprima `sistema: {sistema}`, `incluidas: {lista}` e
    `tokens usados: {usado}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/068-gerenciamento-de-contexto/solucao_2.saida.txt
"""


def contar(t):
    return len(t.split())


sistema = "assistente util"
historico = ["passo um inicial", "passo dois meio", "passo tres final"]
limite = 8

# TODO: implemente o truncamento por recência respeitando o orçamento.
