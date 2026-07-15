"""Exercício 3 — Arestas condicionais (laço agente ↔ ferramenta).

Setup:
    nós: agente (passos += 1, registra "agente"),
         ferramenta (coletado += 1, registra "ferramenta")
    rotear(estado) -> "ferramenta" se coletado < 3, senão "END"
    A ferramenta SEMPRE volta ao agente.
    estado inicial = {"passos": 0, "coletado": 0, "rota": []}

Tarefa:
    Implemente o motor: começando em "agente", execute o nó atual; se o nó atual
    for "agente", o próximo vem de `rotear`; se for "ferramenta", o próximo é
    "agente". Pare em "END". Imprima `rota: {rota}` e `passos do agente: {passos}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/069-orquestracao-langgraph/solucao_3.saida.txt
    (`passos do agente: 4`).
"""

estado = {"passos": 0, "coletado": 0, "rota": []}

# TODO: implemente os nós, o roteamento condicional e o motor.
