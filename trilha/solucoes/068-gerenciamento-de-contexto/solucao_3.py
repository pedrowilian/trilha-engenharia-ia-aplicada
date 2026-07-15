"""Solução de referência — Exercício 3 da Lição 068.

Sumarização: comprime mensagens antigas num resumo curto, reduzindo a contagem
de tokens para caber no contexto. Determinístico.
"""


def contar(t):
    return len(t.split())


antigas = ["usuario relatou erro", "time investigou causa", "bug foi corrigido", "deploy realizado"]
resumo = "resumo: bug corrigido e publicado"

tokens_antes = sum(contar(m) for m in antigas)
tokens_depois = contar(resumo)

print("tokens antes:", tokens_antes)
print("tokens depois:", tokens_depois)
print("reducao:", tokens_antes - tokens_depois)
