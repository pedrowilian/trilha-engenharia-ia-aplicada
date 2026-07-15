"""Solução de referência — Exercício 1 da Lição 070.

Tracing: registra eventos (spans) da execução do agente para observabilidade.
Determinístico.
"""

trace = []


def registrar(evento, detalhe):
    trace.append({"passo": len(trace) + 1, "evento": evento, "detalhe": detalhe})


registrar("inicio", "tarefa")
registrar("tool_call", "calc")
registrar("fim", "ok")

for s in trace:
    print(f"[{s['passo']}] {s['evento']}: {s['detalhe']}")
print("total de eventos:", len(trace))
