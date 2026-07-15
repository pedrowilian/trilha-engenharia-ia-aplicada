"""Exercício 3 — RAG sobre runbooks + auto-remediação com guardrails.

Setup:
    runbooks = {
        "disco_cheio": "limpar_logs_antigos",
        "memoria_alta": "reiniciar_servico",
        "cert_expirado": "rotacionar_certificado",
    }
    ACOES_SEGURAS = {"limpar_logs_antigos", "reiniciar_servico"}

Tarefa:
    Implemente `recuperar(sintoma)` (consulta o runbook) e
    `remediar(sintoma, severidade)`: se não há runbook, "sem_runbook -> escalar";
    se a severidade é HIGH ou a ação não é segura, "ação -> requer_aprovacao
    (escalar)"; caso contrário, "ação -> aplicado (dry-run ok)". Imprima o
    resultado de `remediar("memoria_alta", "LOW")`, `remediar("disco_cheio",
    "HIGH")` e `remediar("api_lenta", "LOW")`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/096-ia-devops-ii/solucao_3.saida.txt.
"""

runbooks = {
    "disco_cheio": "limpar_logs_antigos",
    "memoria_alta": "reiniciar_servico",
    "cert_expirado": "rotacionar_certificado",
}
ACOES_SEGURAS = {"limpar_logs_antigos", "reiniciar_servico"}

# TODO: implemente recuperar e remediar; imprima os tres casos.
