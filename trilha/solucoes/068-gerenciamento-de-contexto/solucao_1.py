"""Solução de referência — Exercício 1 da Lição 068.

Orçamento de tokens: conta tokens (aproximados por palavras) e compara ao limite
da janela de contexto. Determinístico.
"""


def contar_tokens(texto):
    return len(texto.split())


mensagens = ["bom dia", "quero saber sobre agentes de ia", "obrigado"]
limite = 10
total = sum(contar_tokens(m) for m in mensagens)

print("tokens por mensagem:", [contar_tokens(m) for m in mensagens])
print("total:", total)
print("cabe no limite?", total <= limite)
