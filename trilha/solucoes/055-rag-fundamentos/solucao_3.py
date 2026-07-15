"""Solucao de referencia - Exercicio 3 da Licao 055.

Resposta com atribuicao: recupera os documentos que sustentam a resposta e
devolve a lista de fontes citadas. Grounding e atribuicao sao o que torna a
saida de um sistema RAG verificavel.
"""
import re


corpus = {
    "d1": "O plano basico custa 10 reais por mes.",
    "d2": "O plano basico inclui 5 projetos.",
    "d3": "O plano pro custa 30 reais por mes.",
}


def tokenizar(texto):
    return set(re.findall(r"[a-z0-9]+", texto.lower()))


def recuperar(pergunta, corpus, k=2):
    q = tokenizar(pergunta)
    pont = sorted(((did, len(q & tokenizar(corpus[did]))) for did in corpus),
                  key=lambda t: (-t[1], t[0]))
    return [did for did, s in pont[:k] if s > 0]


pergunta = "o que o plano basico inclui e quanto custa"
fontes = recuperar(pergunta, corpus)
print("fontes:", fontes)
print("citacao:", ", ".join(sorted(fontes)))
