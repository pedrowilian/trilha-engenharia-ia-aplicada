"""Exercício 1 — Listar e ler resources.

Setup: o catálogo de resources abaixo (URI -> conteúdo).

Tarefa:
    Imprima `total: {n}`, depois cada URI em ordem alfabética prefixada por
    `- ` (use `print("-", uri)`), e por fim `config: {conteúdo de
    file:///config.yaml}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/073-mcp-primitivas/solucao_1.saida.txt
"""
resources = {
    "file:///config.yaml": "modo: prod",
    "file:///notas.md": "# Notas",
}

# TODO: imprima o total, as URIs ordenadas e o conteúdo do config.yaml.
