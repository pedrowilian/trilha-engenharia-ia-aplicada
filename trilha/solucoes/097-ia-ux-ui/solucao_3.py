"""Solução de referência — Exercício 3 da Lição 097.

Ida-e-volta (round-trip) da especificação de UI: parse -> serialize -> parse deve
recuperar exatamente a mesma árvore de componentes. Determinístico.
"""


def parse_ui(texto):
    arvore = []
    for linha in texto.strip().splitlines():
        tipo, _, rotulo = linha.partition(":")
        arvore.append({"tipo": tipo.strip(), "rotulo": rotulo.strip()})
    return arvore


def serializar(arvore):
    return "\n".join(f"{c['tipo']}: {c['rotulo']}" for c in arvore)


spec = "input: Nome\nbutton: Ok"
a1 = parse_ui(spec)
a2 = parse_ui(serializar(a1))

print("ida-e-volta exata:", a1 == a2)
print("componentes:", len(a2))
