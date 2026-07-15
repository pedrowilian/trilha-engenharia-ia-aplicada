"""Exercício 3 — Recuperação multimodal por similaridade do cosseno.

Setup: a embedding `legenda` (já no espaço compartilhado) e três embeddings de
imagens candidatas, abaixo.

Tarefa:
    Implemente `cosseno(a, b)` (produto interno normalizado). Calcule a
    similaridade da legenda com cada imagem, ordene em ordem decrescente e
    imprima cada `nome: similaridade` (campo de 9 à direita, 4 casas) e o
    melhor casamento, no formato:
        montanha: 0.9854
        ...
        melhor match: montanha

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/050-genai-multimodais/solucao_3.saida.txt
"""
import numpy as np

legenda = np.array([0.2, 0.8, 0.3])
imagens = {
    "cachorro": np.array([0.9, 0.1, 0.2]),
    "montanha": np.array([0.1, 0.85, 0.2]),
    "carro":    np.array([0.3, 0.2, 0.9]),
}

# TODO: implementar cosseno(), ordenar e imprimir o ranking.
