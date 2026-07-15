"""Solução de referência — Exercício 1 da Lição 077.

Recomenda a abordagem (RAG, fine-tuning, ambos ou prompt engineering) a partir
de três flags do problema.
"""


def recomendar(conhecimento_dinamico, precisa_formato_fixo, orcamento_treino):
    if conhecimento_dinamico and precisa_formato_fixo:
        return "RAG + fine-tuning"
    if conhecimento_dinamico:
        return "RAG"
    if precisa_formato_fixo and orcamento_treino:
        return "fine-tuning"
    return "prompt engineering"


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
for descricao, flags in casos:
    print(f"{recomendar(**flags):>18}  <-  {descricao}")
