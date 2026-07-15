"""Exercício 2 — Topologias multi-agente (contagem de canais).

Setup: para `n` agentes, calcule o número de canais de comunicação em três
topologias: supervisor (estrela), hierárquica (árvore) e group-chat (completa).
Valores de n a imprimir: [3, 5].

Tarefa:
    Implemente `arestas_supervisor(n) = n`, `arestas_hierarquica(nos) = nos - 1`
    e `arestas_grupo(n) = n * (n - 1) // 2`. Para cada n, imprima
    `n={n}: supervisor={...} hierarquica={...} grupo={...}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/071-multi-agente/solucao_2.saida.txt
"""

# TODO: implemente as três fórmulas e imprima os resultados.
