"""Componente MCP (servidor) — expõe a capacidade do agente como ferramenta.

Reproduz, de forma minimalista e offline, o estilo do Model Context Protocol:
o servidor mantém um registro de ferramentas (cada uma com nome, descrição e
esquema de entrada) e atende requisições no formato JSON-RPC simplificado
(`{"method": ..., "params": ...}`), respondendo `{"result": ...}` ou
`{"error": ...}`.

Não há sockets nem rede: o transporte é uma chamada de função em memória. Isso
mantém o exemplo determinístico, mas preserva a forma do protocolo (descoberta
de ferramentas via `tools/list` e invocação via `tools/call`).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .agent import Agente


@dataclass
class FerramentaMcp:
    """Descritor de uma ferramenta exposta pelo servidor MCP."""

    nome: str
    descricao: str
    esquema_entrada: dict[str, Any]
    handler: Callable[[dict[str, Any]], dict[str, Any]]


@dataclass
class EvidenciaMcp:
    """Evidência observável de que o servidor MCP atendeu requisições."""

    ferramentas_registradas: int = 0
    chamadas_atendidas: int = 0
    ultimo_metodo: str = ""

    def executou(self) -> bool:
        return self.chamadas_atendidas > 0


class ServidorMcp:
    """Servidor MCP em memória com registro e despacho de ferramentas."""

    def __init__(self, agente: Agente) -> None:
        self._agente = agente
        self._ferramentas: dict[str, FerramentaMcp] = {}
        self.evidencia = EvidenciaMcp()
        self._registrar_padrao()

    def registrar(self, ferramenta: FerramentaMcp) -> None:
        self._ferramentas[ferramenta.nome] = ferramenta
        self.evidencia.ferramentas_registradas = len(self._ferramentas)

    def _registrar_padrao(self) -> None:
        self.registrar(FerramentaMcp(
            nome="responder_suporte",
            descricao="Responde uma pergunta de suporte usando agente + RAG.",
            esquema_entrada={"type": "object",
                             "properties": {"pergunta": {"type": "string"}},
                             "required": ["pergunta"]},
            handler=self._handler_responder,
        ))

    def _handler_responder(self, params: dict[str, Any]) -> dict[str, Any]:
        pergunta = params.get("pergunta", "")
        r = self._agente.responder(pergunta)
        return {
            "resposta": r.resposta,
            "ferramentas_usadas": list(r.evidencia.ferramentas_usadas),
            "passos": r.evidencia.passos,
        }

    def atender(self, requisicao: dict[str, Any]) -> dict[str, Any]:
        """Atende uma requisição JSON-RPC simplificada."""
        metodo = requisicao.get("method", "")
        params = requisicao.get("params", {}) or {}
        self.evidencia.ultimo_metodo = metodo

        if metodo == "tools/list":
            self.evidencia.chamadas_atendidas += 1
            return {"result": {"tools": [
                {"name": f.nome, "description": f.descricao,
                 "inputSchema": f.esquema_entrada}
                for f in self._ferramentas.values()
            ]}}

        if metodo == "tools/call":
            nome = params.get("name", "")
            ferramenta = self._ferramentas.get(nome)
            if ferramenta is None:
                return {"error": {"code": -32601,
                                  "message": f"ferramenta desconhecida: {nome}"}}
            self.evidencia.chamadas_atendidas += 1
            resultado = ferramenta.handler(params.get("arguments", {}) or {})
            return {"result": resultado}

        return {"error": {"code": -32601, "message": f"metodo desconhecido: {metodo}"}}
