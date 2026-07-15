"""Exercício 1 — text-to-UI: especificação textual → árvore de componentes.

Setup: spec = "checkbox: Lembrar\\nbutton: Login".

Tarefa:
    Implemente `parse_ui(texto)` que, para cada linha "tipo: rotulo", produz um
    dict {"tipo": ..., "rotulo": ...} (use partition(":") e strip). Imprima
    cada componente como `tipo -> rotulo` e, ao final, `componentes:`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/097-ia-ux-ui/solucao_1.saida.txt.
"""

spec = "checkbox: Lembrar\nbutton: Login"

# TODO: implemente parse_ui e imprima os componentes e o total.
