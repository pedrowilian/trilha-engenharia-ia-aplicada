"""Exercício 1 — Copiloto de IaC: gerar e validar manifesto.

Setup: intencao = {"servico": "cache", "replicas": 1, "porta": 80}.

Tarefa:
    Implemente `gerar_manifesto(intencao)` (devolve dict com kind="Deployment",
    name, replicas, port) e `validar(manifesto)` que devolve a lista de erros:
    acrescente "replicas<2" se replicas < 2 e "porta fora da faixa" se a porta
    não estiver em [1024, 65535]. Imprima `servico:` e `erros:`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/095-ia-devops-i/solucao_1.saida.txt.
"""

intencao = {"servico": "cache", "replicas": 1, "porta": 80}

# TODO: implemente gerar_manifesto e validar; imprima servico e erros.
