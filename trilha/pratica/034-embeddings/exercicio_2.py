"""Exercício 2 — Analogia vetorial país/capital.

Setup:
    emb = {
        "franca": [1.0, 0.0],
        "paris":  [1.0, 1.0],
        "italia": [0.0, 1.0],
        "roma":   [0.0, 2.0],
        "carro":  [-1.0, -1.0],
    }

Tarefa:
    Implemente analogia(a, b, c, emb): alvo = b - a + c e devolve o vizinho
    mais próximo por cosseno (excluindo a, b, c). Resolva
    "paris esta para franca assim como ? esta para italia".

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/034-embeddings/solucao_2.saida.txt
"""
import math

emb = {
    "franca": [1.0, 0.0],
    "paris":  [1.0, 1.0],
    "italia": [0.0, 1.0],
    "roma":   [0.0, 2.0],
    "carro":  [-1.0, -1.0],
}

# TODO: implementar cos_sim e analogia(a, b, c, emb) e imprimir a resposta.
