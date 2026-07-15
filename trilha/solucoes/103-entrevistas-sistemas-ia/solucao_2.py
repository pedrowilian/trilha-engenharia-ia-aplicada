"""Solucao de referencia - Exercicio 2 da Licao 103.

Orcamento de um loop de agente (estilo ReAct): cada iteracao gasta tokens; o
loop para ao concluir a tarefa ou ao esgotar o orcamento. Em entrevista de
agentes, controlar o numero de iteracoes e o gasto e o que separa um agente util
de um que entra em loop infinito e queima a fatura.
"""


def simular_agente(passos_necessarios, tokens_por_passo, orcamento_tokens):
    usados = 0
    iteracoes = 0
    for passo in range(1, passos_necessarios + 1):
        if usados + tokens_por_passo > orcamento_tokens:
            return iteracoes, usados, "estourou orcamento"
        usados += tokens_por_passo
        iteracoes += 1
    return iteracoes, usados, "concluiu"


for orc in [800, 1500]:
    it, usados, status = simular_agente(5, 300, orc)
    print(f"orcamento={orc}: iteracoes={it} tokens={usados} -> {status}")
