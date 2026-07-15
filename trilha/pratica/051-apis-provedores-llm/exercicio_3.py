"""Exercício 3 — Decomposição de custo de uma chamada.

Setup: 1200 tokens de entrada, 400 de saída, preço de entrada 0.50 e de saída
1.50 (USD por 1k tokens).

Tarefa:
    Implemente `custo(prompt_tokens, completion_tokens, preco_in_1k,
    preco_out_1k)` devolvendo (custo_in, custo_out), onde cada custo é
    `tokens / 1000 * preco_1k`. Imprima a quebra (tokens e custos, 4 casas) e
    o custo total, no formato alinhado:
        tokens entrada : 1200
        ...
        custo total    : $1.2000

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/051-apis-provedores-llm/solucao_3.saida.txt
"""

prompt_tokens = 1200
completion_tokens = 400
preco_in_1k = 0.50
preco_out_1k = 1.50

# TODO: implementar custo() e imprimir a decomposicao.
