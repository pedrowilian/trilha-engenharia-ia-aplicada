"""Exercício 1 — Scan de segurança/compliance sobre uma configuração.

Setup: config = {"public": False, "encryption": False, "user": "admin"}.

Tarefa:
    Implemente `scan(config)` com as regras: HIGH se `public` é verdadeiro;
    MEDIUM se não há `encryption`; HIGH se `user == "root"`. Devolva a lista de
    achados `(severidade, mensagem)` e imprima cada um como `[SEV] mensagem`,
    seguido de `total:`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/096-ia-devops-ii/solucao_1.saida.txt.
"""

config = {"public": False, "encryption": False, "user": "admin"}

# TODO: implemente scan e imprima os achados e o total.
