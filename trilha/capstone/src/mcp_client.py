"""Componente MCP (cliente) — descobre e invoca ferramentas do servidor.

O cliente fala o mesmo dialeto JSON-RPC simplificado do servidor: lista as
ferramentas (`tools/list`) e invoca uma delas (`tools/call`). O transporte é
uma chamada de função em memória ao servidor — determinístico e offline — mas a
forma das mensagens é a do MCP.
"""
from __future__ import annotations

from typing import Any

from .mcp_server import ServidorMcp


class ClienteMcp:
    """Cliente MCP que conversa com um `ServidorMcp` em memória."""

    def __init__(self, servidor: ServidorMcp) -> None:
        self._servidor = servidor

    def listar_ferramentas(self) -> list[dict[str, Any]]:
        resposta = self._servidor.atender({"method": "tools/list", "params": {}})
        return resposta.get("result", {}).get("tools", [])

    def chamar(self, nome: str, argumentos: dict[str, Any]) -> dict[str, Any]:
        resposta = self._servidor.atender({
            "method": "tools/call",
            "params": {"name": nome, "arguments": argumentos},
        })
        if "error" in resposta:
            raise RuntimeError(resposta["error"]["message"])
        return resposta["result"]
