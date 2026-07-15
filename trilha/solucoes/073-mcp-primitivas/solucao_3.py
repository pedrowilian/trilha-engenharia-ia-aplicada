"""Solução de referência — Exercício 3 da Lição 073.

Renderização de um prompt a partir de um template com argumentos. Determinístico.
"""
prompts = {
    "traduzir": "Traduza para {idioma}: {texto}",
}

def renderizar_prompt(nome, argumentos):
    return prompts[nome].format(**argumentos)

print(renderizar_prompt("traduzir", {"idioma": "ingles", "texto": "bom dia"}))
