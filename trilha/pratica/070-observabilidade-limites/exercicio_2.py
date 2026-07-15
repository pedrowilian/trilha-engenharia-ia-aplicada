"""Exercício 2 — Guardrails e human-in-the-loop (HITL).

Setup:
    permitidas = {"ler", "escrever", "apagar"}; sensiveis = {"apagar"}
    aprovacao_humana(acao) -> True (humano simulado aprova)
    acoes a testar: ["ler", "apagar", "enviar"]

Tarefa:
    Implemente `verificar(acao)`: "bloqueada" se não está em permitidas;
    para ações sensíveis, "aprovada"/"negada" conforme `aprovacao_humana`;
    caso contrário "liberada". Imprima `{acao}: {resultado}` para cada ação.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/070-observabilidade-limites/solucao_2.saida.txt
"""

permitidas = {"ler", "escrever", "apagar"}
sensiveis = {"apagar"}

# TODO: implemente verificar e avalie cada ação.
