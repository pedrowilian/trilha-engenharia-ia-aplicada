"""Solução de referência — Exercício 2 da Lição 070.

Guardrails + HITL: bloqueia ações fora da allowlist e exige aprovação humana para
ações sensíveis. Determinístico (humano simulado aprova).
"""

permitidas = {"ler", "escrever", "apagar"}
sensiveis = {"apagar"}


def aprovacao_humana(acao):
    return True


def verificar(acao):
    if acao not in permitidas:
        return "bloqueada"
    if acao in sensiveis:
        return "aprovada" if aprovacao_humana(acao) else "negada"
    return "liberada"


for acao in ["ler", "apagar", "enviar"]:
    print(f"{acao}: {verificar(acao)}")
