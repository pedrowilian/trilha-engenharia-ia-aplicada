"""Solução de referência — Exercício 3 da Lição 100.

Integração fim-a-fim com detecção de componente ausente. Cada componente
incrementa seu contador ao executar; `completo()` exige os três > 0. Compara o
fluxo completo com um fluxo em que o MCP nunca é acionado.
"""


def fluxo(acionar_mcp):
    ev = {"rag": 0, "agente": 0, "mcp": 0}
    if acionar_mcp:
        ev["mcp"] += 2          # cliente MCP: tools/list + tools/call
    ev["agente"] += 1           # servidor delega ao agente
    ev["rag"] += 1              # agente consulta o RAG
    return ev


def completo(ev):
    return all(v > 0 for v in ev.values())


def ausentes(ev):
    return [c for c in ("rag", "agente", "mcp") if ev[c] == 0]


for nome, acionar in [("com_mcp", True), ("sem_mcp", False)]:
    ev = fluxo(acionar)
    print(f"{nome}: rag={ev['rag']} agente={ev['agente']} mcp={ev['mcp']} "
          f"completo={completo(ev)} ausentes={ausentes(ev)}")
