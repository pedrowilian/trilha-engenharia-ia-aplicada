"""Solução de referência — Exercício 3 da Lição 096.

RAG sobre runbooks + auto-remediação com guardrails: recupera o procedimento
para um sintoma e só automatiza ações seguras de baixa severidade; o resto
escala. Determinístico.
"""

runbooks = {
    "disco_cheio": "limpar_logs_antigos",
    "memoria_alta": "reiniciar_servico",
    "cert_expirado": "rotacionar_certificado",
}
ACOES_SEGURAS = {"limpar_logs_antigos", "reiniciar_servico"}


def recuperar(sintoma):
    return runbooks.get(sintoma)


def remediar(sintoma, severidade):
    acao = recuperar(sintoma)
    if acao is None:
        return "sem_runbook -> escalar"
    if severidade == "HIGH" or acao not in ACOES_SEGURAS:
        return f"{acao} -> requer_aprovacao (escalar)"
    return f"{acao} -> aplicado (dry-run ok)"


print(remediar("memoria_alta", "LOW"))
print(remediar("disco_cheio", "HIGH"))
print(remediar("api_lenta", "LOW"))
