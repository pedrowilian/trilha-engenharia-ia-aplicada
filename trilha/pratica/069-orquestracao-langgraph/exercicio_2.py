"""Exercício 2 — Grafo linear e motor de execução.

Setup:
    nós: A (valor += 5, registra "A"), B (valor -= 2, registra "B")
    arestas = {"START": "A", "A": "B", "B": "END"}
    estado inicial = {"valor": 10, "rota": []}

Tarefa:
    Implemente os nós e o motor que, partindo de `arestas["START"]`, executa o
    nó atual e segue para o próximo até chegar em "END". Imprima `valor: {valor}`
    e `rota: {rota}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/069-orquestracao-langgraph/solucao_2.saida.txt (valor: 13).
"""

arestas = {"START": "A", "A": "B", "B": "END"}
estado = {"valor": 10, "rota": []}

# TODO: implemente os nós e o motor de execução do grafo.
