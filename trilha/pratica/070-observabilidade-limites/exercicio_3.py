"""Exercício 3 — Prevenção de loop descontrolado.

Setup: `executar(acoes, max_passos=5)` deve parar se a mesma ação aparecer 3x
seguidas OU se o número de passos exceder `max_passos`. Casos a imprimir:
    executar(["a", "b"])
    executar(["z", "z", "z"])
    executar(["a", "b", "c", "d", "e", "f"])

Tarefa:
    Implemente `executar`: a cada passo, primeiro cheque o limite de passos,
    depois a repetição (as duas últimas ações vistas iguais à atual). Retorne
    "concluiu sem incidentes", "parou: acao repetida '{acao}'" ou
    "parou: limite de {max_passos} passos". Imprima o retorno de cada caso.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/070-observabilidade-limites/solucao_3.saida.txt
"""

# TODO: implemente executar com as duas salvaguardas.
