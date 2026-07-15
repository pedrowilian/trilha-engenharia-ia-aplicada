"""Exercício 3 — Comparar perda mascarada e não-mascarada.

Setup: os mesmos vetores `p_alvo` e `mascara` do Exercício 2.

Tarefa:
    Calcule a perda sem máscara (média de -log p sobre TODOS os tokens, estilo
    pré-treino) e a perda com máscara (só os tokens de resposta, estilo SFT).
    Imprima ambas (4 casas) e se elas diferem.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/046-instruction-tuning-sft/solucao_3.saida.txt
"""
import numpy as np

p_alvo = np.array([0.4, 0.7, 0.3, 0.95, 0.5, 0.6])
mascara = np.array([0, 0, 0, 1, 1, 1])

# TODO: calcular as duas perdas, imprimir ambas (4 casas) e se diferem.
