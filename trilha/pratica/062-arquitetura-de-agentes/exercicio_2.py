"""Exercício 2 — Toolbox e executor que despacha um plano.

Setup:
    toolbox = {"incrementar": lambda x: x + 1, "dobrar": lambda x: x * 2}
    plano = ["incrementar", "dobrar", "incrementar"]
    estado inicial = 2

Tarefa:
    Implemente `executor(acao, estado)` que aplica a ferramenta nomeada. Percorra
    o plano aplicando cada ação ao estado, registre `(acao, estado)` em `memory`
    e imprima `acao={acao} -> estado={estado}` a cada passo. Ao final, imprima
    `memoria: {memory}` e `estado final: {estado}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/062-arquitetura-de-agentes/solucao_2.saida.txt
"""

toolbox = {
    "incrementar": lambda x: x + 1,
    "dobrar": lambda x: x * 2,
}
plano = ["incrementar", "dobrar", "incrementar"]
estado = 2
memory = []

# TODO: implemente o executor e o despacho do plano.
