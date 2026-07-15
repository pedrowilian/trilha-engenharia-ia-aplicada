"""Exercício 3 — Sumarização de histórico.

Setup:
    antigas = ["usuario relatou erro", "time investigou causa",
               "bug foi corrigido", "deploy realizado"]
    resumo = "resumo: bug corrigido e publicado"

Tarefa:
    Conte os tokens (palavras) das mensagens antigas e do resumo. Imprima
    `tokens antes: {soma}`, `tokens depois: {resumo}` e
    `reducao: {antes - depois}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/068-gerenciamento-de-contexto/solucao_3.saida.txt
"""


def contar(t):
    return len(t.split())


antigas = ["usuario relatou erro", "time investigou causa", "bug foi corrigido", "deploy realizado"]
resumo = "resumo: bug corrigido e publicado"

# TODO: calcule a redução de tokens pela sumarização.
