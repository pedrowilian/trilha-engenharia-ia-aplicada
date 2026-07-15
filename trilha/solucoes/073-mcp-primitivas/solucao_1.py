"""Solução de referência — Exercício 1 da Lição 073.

Listar e ler resources (dados endereçados por URI). Determinístico (ordem
alfabética das URIs).
"""
resources = {
    "file:///config.yaml": "modo: prod",
    "file:///notas.md": "# Notas",
}

print("total:", len(resources))
for uri in sorted(resources):
    print("-", uri)
print("config:", resources["file:///config.yaml"])
