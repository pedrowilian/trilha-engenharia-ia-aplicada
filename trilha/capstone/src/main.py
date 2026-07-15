"""Ponto de entrada do capstone — executa o fluxo e imprime a evidência.

Execute com:
    python3 trilha/capstone/src/main.py

Imprime, de forma determinística, a evidência observável de que cada um dos
três componentes (RAG, agente, MCP) participou do fluxo ponta a ponta. Sai com
código 0 quando todos executaram; 1 caso contrário.
"""
from __future__ import annotations

import sys

# Suporta execução tanto como módulo (`python -m capstone.src.main`) quanto como
# script direto (`python trilha/capstone/src/main.py`).
if __package__ in (None, ""):
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
    from capstone.src.pipeline import MicroSaaS
else:  # pragma: no cover - caminho de import como pacote
    from .pipeline import MicroSaaS


def main() -> int:
    pergunta = "Como redefinir minha senha?"
    app = MicroSaaS()
    resultado = app.executar(pergunta)
    ev = resultado.evidencia

    print("=== Capstone Micro-SaaS: RAG + Agente + MCP ===")
    print(f"pergunta: {pergunta}")
    print(f"resposta: {resultado.resposta}")
    print("--- evidencia por componente ---")
    print(f"[RAG] consultas={ev.rag_consultas} "
          f"top={ev.rag_top_id} score={ev.rag_top_score:.4f}")
    print(f"[AGENTE] passos={ev.agente_passos} "
          f"ferramentas={','.join(ev.agente_ferramentas)}")
    print(f"[MCP] ferramentas_registradas={ev.mcp_ferramentas_registradas} "
          f"chamadas={ev.mcp_chamadas} metodo={ev.mcp_metodo}")

    estados = ev.componentes_executados()
    for nome in ("rag", "agente", "mcp"):
        marca = "ok" if estados[nome] else "FALTANDO"
        print(f"componente {nome}: {marca}")

    if ev.completo():
        print("RESULTADO: fluxo completo (RAG + agente + MCP executaram)")
        return 0
    print("RESULTADO: fluxo incompleto")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
