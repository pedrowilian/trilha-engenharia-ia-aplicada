"""Exercício 1 — Recomendar a abordagem (RAG / fine-tuning / ambos / prompt).

Setup: a lista `casos` (abaixo), cada um com as flags conhecimento_dinamico,
precisa_formato_fixo e orcamento_treino.

Tarefa:
    Implemente `recomendar(conhecimento_dinamico, precisa_formato_fixo,
    orcamento_treino)` seguindo a regra: conhecimento dinâmico E formato fixo
    -> "RAG + fine-tuning"; só conhecimento dinâmico -> "RAG"; formato fixo com
    orçamento -> "fine-tuning"; caso contrário -> "prompt engineering". Imprima
    cada recomendação alinhada à direita (largura 18) seguida de "  <-  " e a
    descrição.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/077-fine-tuning-completo/solucao_1.saida.txt
"""
casos = [
    ("Politicas internas mudam todo mes",
     dict(conhecimento_dinamico=True, precisa_formato_fixo=False, orcamento_treino=False)),
    ("Classificar tickets num esquema fixo",
     dict(conhecimento_dinamico=False, precisa_formato_fixo=True, orcamento_treino=True)),
    ("Catalogo dinamico + tom de marca fixo",
     dict(conhecimento_dinamico=True, precisa_formato_fixo=True, orcamento_treino=True)),
    ("Resumir texto colado pelo usuario",
     dict(conhecimento_dinamico=False, precisa_formato_fixo=False, orcamento_treino=True)),
]

# TODO: implementar recomendar(...) e imprimir as recomendações.
