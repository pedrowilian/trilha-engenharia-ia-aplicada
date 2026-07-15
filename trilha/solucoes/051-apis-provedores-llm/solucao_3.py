"""Solução de referência — Exercício 3 da Lição 051.

Decomposição de custo de uma chamada de API: preços distintos por 1k tokens de
entrada e de saída. Imprime a quebra (entrada, saída) e o custo total.
"""


def custo(prompt_tokens, completion_tokens, preco_in_1k, preco_out_1k):
    custo_in = prompt_tokens / 1000 * preco_in_1k
    custo_out = completion_tokens / 1000 * preco_out_1k
    return custo_in, custo_out


prompt_tokens = 1200
completion_tokens = 400
c_in, c_out = custo(prompt_tokens, completion_tokens, 0.50, 1.50)
print(f"tokens entrada : {prompt_tokens}")
print(f"tokens saida   : {completion_tokens}")
print(f"custo entrada  : ${c_in:.4f}")
print(f"custo saida    : ${c_out:.4f}")
print(f"custo total    : ${c_in + c_out:.4f}")
