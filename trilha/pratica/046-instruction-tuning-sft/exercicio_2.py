"""Exercício 2 — Perda mascarada do SFT.

Setup: os vetores `p_alvo` (probabilidade do token-alvo em cada posição) e
`mascara` (1 = token de resposta, 0 = token de prompt) abaixo.

Tarefa:
    Calcule a NLL por token (-log p_alvo) e a perda mascarada (média de -log p
    apenas sobre os tokens de resposta). Imprima `nll por token` (4 casas, como
    lista), `tokens de resposta` (soma da máscara) e `perda mascarada` (4 casas).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/046-instruction-tuning-sft/solucao_2.saida.txt
"""
import numpy as np

p_alvo = np.array([0.4, 0.7, 0.3, 0.95, 0.5, 0.6])
mascara = np.array([0, 0, 0, 1, 1, 1])

# TODO: calcular nll por token, a perda mascarada e imprimir os resultados.
