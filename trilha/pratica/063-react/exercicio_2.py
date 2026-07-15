"""Exercício 2 — Parsing da ação ReAct.

Setup: ações no formato `ferramenta[arg1, arg2, ...]`. Casos a testar:
["soma[1, 2, 3]", "kb[capital]", "ruim"].

Tarefa:
    Implemente `parse_acao(texto)` que retorna `(nome, args)`, onde `args` é a
    lista de argumentos (sem espaços). Para texto fora do formato, retorne
    `("?", [])`. Para cada caso, imprima `{texto!r} -> nome={nome} args={args}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/063-react/solucao_2.saida.txt
"""
import re

casos = ["soma[1, 2, 3]", "kb[capital]", "ruim"]

# TODO: implemente parse_acao e imprima o resultado de cada caso.
