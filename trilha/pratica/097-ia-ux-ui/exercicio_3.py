"""Exercício 3 — Ida-e-volta (round-trip) da especificação de UI.

Setup: spec = "input: Nome\\nbutton: Ok".

Tarefa:
    Implemente `parse_ui(texto)` e `serializar(arvore)` de modo que
    parse_ui(serializar(parse_ui(spec))) recupere EXATAMENTE a mesma árvore.
    Imprima `ida-e-volta exata: {bool}` e `componentes: {n}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/097-ia-ux-ui/solucao_3.saida.txt (`ida-e-volta exata: True`).
"""

spec = "input: Nome\nbutton: Ok"

# TODO: implemente parse_ui e serializar; verifique a ida-e-volta exata.
