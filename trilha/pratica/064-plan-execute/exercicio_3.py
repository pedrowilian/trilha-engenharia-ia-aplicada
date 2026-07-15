"""Exercício 3 — Replanejamento ao falhar.

Setup:
    plano = ["login", "pagamento", "recibo"]
    `executar(passo)` retorna False apenas para "pagamento" (falha simulada).
    alternativo = {"pagamento": ["pagamento_2fa"]}

Tarefa:
    Percorra o plano por índice. Execute cada passo e registre
    `(passo, "ok"/"falhou")` em `historico`. Se falhar, substitua o passo atual
    pelos passos do plano alternativo e retome (sem avançar o índice). Ao final,
    imprima cada `{passo}: {status}` e `plano final: {plano}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/064-plan-execute/solucao_3.saida.txt
"""


def executar(passo):
    return passo != "pagamento"


plano = ["login", "pagamento", "recibo"]
alternativo = {"pagamento": ["pagamento_2fa"]}

# TODO: implemente o laço com replanejamento.
