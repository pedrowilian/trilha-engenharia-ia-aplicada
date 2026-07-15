"""Exercício 3 — Renderizar um prompt.

Setup: o template `prompts = {"traduzir": "Traduza para {idioma}: {texto}"}`.

Tarefa:
    Implemente `renderizar_prompt(nome, argumentos)` usando
    `str.format(**argumentos)` e imprima o resultado para os argumentos
    {"idioma": "ingles", "texto": "bom dia"}.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/073-mcp-primitivas/solucao_3.saida.txt
"""
prompts = {
    "traduzir": "Traduza para {idioma}: {texto}",
}

# TODO: implemente renderizar_prompt e imprima o resultado.
