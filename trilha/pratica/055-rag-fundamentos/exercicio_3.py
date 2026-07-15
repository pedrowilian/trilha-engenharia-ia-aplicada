"""Exercicio 3 - Resposta com atribuicao de fontes.

Setup (dado):
    corpus = {
        "d1": "O plano basico custa 10 reais por mes.",
        "d2": "O plano basico inclui 5 projetos.",
        "d3": "O plano pro custa 30 reais por mes.",
    }
    pergunta = "o que o plano basico inclui e quanto custa"

Tarefa:
    Implemente recuperar(pergunta, corpus, k=2) devolvendo apenas os ids com
    score > 0, ordenados por (-score, id). Imprima:
      "fontes: <lista de ids>" e "citacao: <ids ordenados separados por virgula>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/055-rag-fundamentos/solucao_3.saida.txt
"""
import re

corpus = {
    "d1": "O plano basico custa 10 reais por mes.",
    "d2": "O plano basico inclui 5 projetos.",
    "d3": "O plano pro custa 30 reais por mes.",
}
pergunta = "o que o plano basico inclui e quanto custa"

# TODO: implemente recuperar com atribuicao e imprima as fontes citadas.
