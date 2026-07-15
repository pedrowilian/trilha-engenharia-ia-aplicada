"""Exercicio 2 - Pipeline retrieve -> augment -> generate.

Setup (dado):
    corpus = {
        "d1": "A politica de reembolso da empresa e de 30 dias corridos.",
        "d2": "O prazo de entrega padrao e de 5 dias uteis.",
        "d3": "O horario de atendimento e das 9h as 18h.",
    }
    pergunta = "quantos dias para reembolso"

Tarefa:
    Implemente as tres etapas:
      - recuperar(pergunta, corpus): devolve o id do documento mais relevante;
      - aumentar(pergunta, doc_texto): monta o prompt
            "Contexto: <texto>\\nPergunta: <pergunta>\\nResposta:";
      - gerar(prompt): gerador-stub que devolve a sentenca apos "Contexto: ".
    Imprima "doc recuperado: <id>" e "resposta: <texto>".

Criterio de conclusao (binario): a saida deve ser identica a
    trilha/solucoes/055-rag-fundamentos/solucao_2.saida.txt
"""
import re

corpus = {
    "d1": "A politica de reembolso da empresa e de 30 dias corridos.",
    "d2": "O prazo de entrega padrao e de 5 dias uteis.",
    "d3": "O horario de atendimento e das 9h as 18h.",
}
pergunta = "quantos dias para reembolso"

# TODO: implemente recuperar, aumentar e gerar; imprima o doc e a resposta.
