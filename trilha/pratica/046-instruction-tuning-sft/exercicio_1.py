"""Exercício 1 — Construir um exemplo de SFT e marcar a máscara.

Setup: a lista de tokens já segmentada (abaixo).

Tarefa:
    Construa a máscara m_t: 0 para tudo até "<|assistant|>" inclusive; 1 para
    os tokens após ele. Imprima `tokens`, `mascara` e `tokens de resposta`
    (soma da máscara).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/046-instruction-tuning-sft/solucao_1.saida.txt
"""
tokens = ["<|user|>", "Some", "2", "e", "3", "<|assistant|>", "5", "<|end|>"]

# TODO: construir a mascara e imprimir tokens, mascara e tokens de resposta.
