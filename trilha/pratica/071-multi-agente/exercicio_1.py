"""Exercício 1 — Supervisor que roteia tarefas.

Setup:
    trabalhadores = {
        "codigo": lambda t: f"implementei {t}",
        "revisao": lambda t: f"revisei {t}",
    }

Tarefa:
    Implemente `supervisor(tipo, tarefa)` que escolhe o trabalhador pelo `tipo`
    e o executa sobre a `tarefa`. Imprima o resultado de
    `supervisor("codigo", "login")` e de `supervisor("revisao", "PR")`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/071-multi-agente/solucao_1.saida.txt
"""

trabalhadores = {
    "codigo": lambda t: f"implementei {t}",
    "revisao": lambda t: f"revisei {t}",
}

# TODO: implemente o supervisor e roteie as duas tarefas.
