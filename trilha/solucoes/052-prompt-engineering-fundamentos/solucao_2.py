"""Solução de referência — Exercício 2 da Lição 052.

Renderiza um template de prompt com variáveis nomeadas via str.format, tornando
o prompt reutilizável para entradas diferentes.
"""


def renderizar(template, variaveis):
    return template.format(**variaveis)


template = "Traduza '{texto}' para {idioma}."
saida = renderizar(template, {"texto": "bom dia", "idioma": "ingles"})
print(saida)
print("tamanho:", len(saida))
