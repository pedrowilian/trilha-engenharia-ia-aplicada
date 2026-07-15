"""Exercicio 1 - Decisao de recuperar.

Setup (dado):
    interrogativos = {qual, quais, quanto, quantos, como, onde, quando}
    chitchat = {oi, ola, bom, dia, boa, tarde, noite, obrigado, tchau}
    perguntas = ["bom dia", "qual o preco do plano", "obrigado"]

Tarefa:
    Implemente precisa_buscar(pergunta): True se houver termo interrogativo;
    False se TODOS os termos forem chitchat; caso contrario, True (default busca).
    Imprima "<pergunta> -> buscar=<bool>" para cada pergunta.

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/061-agentic-rag/solucao_1.saida.txt
"""
import re

interrogativos = {"qual", "quais", "quanto", "quantos", "como", "onde", "quando"}
chitchat = {"oi", "ola", "bom", "dia", "boa", "tarde", "noite", "obrigado", "tchau"}

# TODO: implemente precisa_buscar e classifique "bom dia", "qual o preco do plano", "obrigado".
