"""Solução de referência — Exercício 1 da Lição 097.

text-to-UI: converte uma especificação textual em árvore de componentes.
Determinístico.
"""


def parse_ui(texto):
    arvore = []
    for linha in texto.strip().splitlines():
        tipo, _, rotulo = linha.partition(":")
        arvore.append({"tipo": tipo.strip(), "rotulo": rotulo.strip()})
    return arvore


spec = "checkbox: Lembrar\nbutton: Login"
arvore = parse_ui(spec)
for comp in arvore:
    print(f"{comp['tipo']} -> {comp['rotulo']}")
print("componentes:", len(arvore))
