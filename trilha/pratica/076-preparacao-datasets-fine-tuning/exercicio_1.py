"""Exercício 1 — Limpeza de um dataset cru.

Setup: a lista `brutos` (abaixo) com perguntas/respostas cruas.

Tarefa:
    Normalize os espaços de cada campo (colapsando espaços repetidos e
    aparando as bordas), descarte exemplos com qualquer campo vazio e remova
    duplicatas exatas (pergunta, resposta). Imprima `brutos`, `limpos`,
    `removidos` e a lista final no formato "- pergunta | resposta".

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/076-preparacao-datasets-fine-tuning/solucao_1.saida.txt
"""
brutos = [
    {"pergunta": "Defina overfitting.", "resposta": "Decorar o treino."},
    {"pergunta": "  Defina overfitting. ", "resposta": "Decorar o treino."},
    {"pergunta": "O que e um token?", "resposta": "Unidade de texto."},
    {"pergunta": "Pergunta sem resposta", "resposta": "   "},
    {"pergunta": "", "resposta": "orfa"},
    {"pergunta": "O que e um token?", "resposta": "Unidade de texto."},
]

# TODO: normalizar, filtrar vazios, deduplicar e imprimir o relatório.
