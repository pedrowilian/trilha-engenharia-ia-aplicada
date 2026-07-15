"""Exercício 1 — Montar um prompt a partir de suas partes.

Setup: as quatro partes anatômicas do prompt, abaixo.

Tarefa:
    Implemente `montar_prompt(sistema, instrucao, contexto, consulta)` que
    devolve uma string com uma linha por parte, cada uma rotulada como
    `[SISTEMA] ...`, `[INSTRUCAO] ...`, `[CONTEXTO] ...`, `[CONSULTA] ...`
    (juntas por '\n'). Imprima o prompt e o número de linhas.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/052-prompt-engineering-fundamentos/solucao_1.saida.txt
"""

sistema = "Voce e um assistente juridico."
instrucao = "Responda apenas com base no contexto."
contexto = "O contrato vence em 30 dias."
consulta = "Quando vence o contrato?"

# TODO: implementar montar_prompt() e imprimir o prompt + n de linhas.
