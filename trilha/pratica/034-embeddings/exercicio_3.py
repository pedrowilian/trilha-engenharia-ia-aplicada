"""Exercício 3 — Embedding contextual desambigua "manga".

Setup:
    estatico = {
        "manga": [0.5, 0.5],
        "fruta": [1.0, 0.0],
        "comer": [0.9, 0.1],
        "camisa": [0.0, 1.0],
        "costura": [0.1, 0.9],
    }

Tarefa:
    Implemente contextual(palavra, contexto) = média (arredondada a 4 casas) do
    vetor da palavra com os vetores do contexto. Compute a representação de
    "manga" em ["comer", "fruta"] e em ["camisa", "costura"] e mostre que diferem.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/034-embeddings/solucao_3.saida.txt
"""

estatico = {
    "manga": [0.5, 0.5],
    "fruta": [1.0, 0.0],
    "comer": [0.9, 0.1],
    "camisa": [0.0, 1.0],
    "costura": [0.1, 0.9],
}

# TODO: implementar contextual(palavra, contexto) e comparar os dois sentidos.
