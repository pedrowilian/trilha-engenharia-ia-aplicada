"""Exercício 2 — Renderizar um template com variáveis.

Setup: o `template` com placeholders nomeados e o dict de variáveis, abaixo.

Tarefa:
    Implemente `renderizar(template, variaveis)` usando `str.format(**...)`.
    Renderize o template com {"texto": "bom dia", "idioma": "ingles"} e imprima
    a string resultante e seu tamanho (len).

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/052-prompt-engineering-fundamentos/solucao_2.saida.txt
"""

template = "Traduza '{texto}' para {idioma}."
variaveis = {"texto": "bom dia", "idioma": "ingles"}

# TODO: implementar renderizar() e imprimir saida + tamanho.
