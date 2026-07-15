"""Exercício 1 — Laço de controle de um agente.

Setup: objetivo = 10, estado inicial = 0, ações possíveis "+3" e "+1".

Tarefa:
    Implemente o laço percepção -> raciocínio -> ação -> feedback. A cada
    iteração, calcule o restante (objetivo - estado); se o restante for >= 3,
    a ação é "+3", senão "+1". Aplique a ação, conte os passos e imprima
    `passo {n}: acao={acao} estado={estado}`. Ao final, imprima
    `objetivo atingido em {passos} passos`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/062-arquitetura-de-agentes/solucao_1.saida.txt
"""

objetivo = 10
estado = 0
passos = 0

# TODO: implemente o laço de controle do agente.
