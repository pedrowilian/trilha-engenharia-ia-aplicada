"""Exercicio 2 - Orcamento de um loop de agente.

Setup (dado):
    passos_necessarios = 5 ; tokens_por_passo = 300 ; orcamentos = [800, 1500].

Tarefa:
    Implemente simular_agente(passos_necessarios, tokens_por_passo, orcamento_tokens)
    que executa passos enquanto couber no orcamento; retorna
        (iteracoes, tokens_usados, status) com status "concluiu" se todos os
        passos coubrem, ou "estourou orcamento" caso contrario.
    Para cada orcamento imprima
        "orcamento=<orc>: iteracoes=<it> tokens=<usados> -> <status>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/103-entrevistas-sistemas-ia/solucao_2.saida.txt
"""

passos_necessarios = 5
tokens_por_passo = 300
orcamentos = [800, 1500]

# TODO: implemente simular_agente() e imprima o resultado para cada orcamento.
