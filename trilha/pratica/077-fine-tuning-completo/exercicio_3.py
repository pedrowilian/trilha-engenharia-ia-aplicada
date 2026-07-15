"""Exercício 3 — Matriz de decisão ponderada RAG vs fine-tuning.

Setup: a lista `criterios` (abaixo), cada um (nome, peso, nota_rag, nota_ft).

Tarefa:
    Calcule o total ponderado de RAG e de fine-tuning (soma de peso * nota),
    imprima o cabeçalho, uma linha por critério, um separador de 43 traços, a
    linha TOTAL e o vencedor (maior total; "empate" se iguais). Use os mesmos
    formatos de coluna do enunciado.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/077-fine-tuning-completo/solucao_3.saida.txt
"""
criterios = [
    ("conhecimento muda rapido", 3, 5, 1),
    ("comportamento/estilo fixo", 3, 2, 5),
    ("controle total do modelo", 1, 1, 5),
    ("setup rapido", 2, 5, 1),
]

# TODO: somar os totais ponderados, imprimir a tabela e decidir o vencedor.
