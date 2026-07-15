"""Exercício 2 — Chain-of-thought em passos explícitos.

Setup: o problema "3 caixas com 4 maçãs cada; 5 são comidas. Quantas sobram?",
com os valores abaixo.

Tarefa:
    Resolva em dois passos, guardando cada passo numa lista `passos`:
        passo 1: total = caixas * por_caixa
        passo 2: sobram = total - comidas
    Imprima cada passo prefixado por `passo:` e, por fim, `resposta:` com o
    valor de `sobram`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/053-prompt-engineering-avancado/solucao_2.saida.txt
"""

caixas, por_caixa = 3, 4
comidas = 5

# TODO: calcular os passos, registra-los e imprimir os passos + resposta.
