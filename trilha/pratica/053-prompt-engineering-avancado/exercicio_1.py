"""Exercício 1 — Montar um prompt few-shot.

Setup: a lista `exemplos` (pares texto → rótulo) e a `consulta`, abaixo.

Tarefa:
    Implemente `montar_few_shot(exemplos, consulta)` que formata cada exemplo
    como duas linhas `Texto: ...` / `Rotulo: ...` e, ao final, adiciona a
    consulta com o rótulo em aberto (`Rotulo:` sem valor). Junte tudo por '\n'
    e imprima o prompt.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/053-prompt-engineering-avancado/solucao_1.saida.txt
"""

exemplos = [
    ("adorei o filme", "positivo"),
    ("que experiencia horrivel", "negativo"),
]
consulta = "o atendimento foi otimo"

# TODO: implementar montar_few_shot() e imprimir o prompt.
