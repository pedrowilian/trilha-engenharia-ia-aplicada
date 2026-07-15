"""Exercício 1 — Model router por orçamento de tokens.

Setup:
    reqs = [(10, False), (80, False), (300, False), (50, True)]
    custo = {"leve": 1, "medio": 3, "forte": 10}
    limiar de tokens do tier leve = 64

Tarefa:
    Implemente `rotear(tokens, precisa_raciocinio)` (raciocínio -> "forte";
    senão tokens <= 64 -> "leve", senão "medio"), acumule o custo e imprima
    `tokens={tk:>3} raciocinio={raciocinio!s:>5} -> {tier} (custo {c})` e, por
    fim, `custo total: {total}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/083-padroes-design-ia/solucao_1.saida.txt
"""

reqs = [(10, False), (80, False), (300, False), (50, True)]
custo = {"leve": 1, "medio": 3, "forte": 10}

# TODO: implemente rotear(...) e acumule o custo total das requisições.
