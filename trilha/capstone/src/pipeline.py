"""Orquestração ponta a ponta: MCP → agente → RAG.

Monta o Micro-SaaS completo e expõe `executar(pergunta)`, que dispara o fluxo
e devolve a resposta junto da evidência de cada componente. A evidência é o
mecanismo de verificação: se qualquer um dos três (RAG, agente, MCP) não tiver
participado, isso é observável no resultado.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .agent import Agente
from .mcp_client import ClienteMcp
from .mcp_server import ServidorMcp
from .rag import Documento, RagEmMemoria, corpus_padrao


@dataclass
class EvidenciaFluxo:
    """Agrega a evidência observável dos três componentes do fluxo."""

    rag_consultas: int
    rag_top_id: str
    rag_top_score: float
    agente_passos: int
    agente_ferramentas: list[str]
    mcp_ferramentas_registradas: int
    mcp_chamadas: int
    mcp_metodo: str

    def componentes_executados(self) -> dict[str, bool]:
        return {
            "rag": self.rag_consultas > 0,
            "agente": self.agente_passos > 0,
            "mcp": self.mcp_chamadas > 0,
        }

    def completo(self) -> bool:
        return all(self.componentes_executados().values())


@dataclass
class ResultadoFluxo:
    resposta: str
    evidencia: EvidenciaFluxo


class MicroSaaS:
    """Composição dos três componentes num único produto."""

    def __init__(self, documentos: list[Documento] | None = None) -> None:
        self.rag = RagEmMemoria(documentos if documentos is not None else corpus_padrao())
        self.agente = Agente(self.rag)
        self.servidor = ServidorMcp(self.agente)
        self.cliente = ClienteMcp(self.servidor)

    def executar(self, pergunta: str) -> ResultadoFluxo:
        # 1) cliente MCP descobre as ferramentas disponíveis (tools/list).
        self.cliente.listar_ferramentas()
        # 2) cliente MCP invoca a capacidade (tools/call -> agente -> RAG).
        resultado: dict[str, Any] = self.cliente.chamar(
            "responder_suporte", {"pergunta": pergunta})

        evidencia = EvidenciaFluxo(
            rag_consultas=self.rag.evidencia.consultas,
            rag_top_id=self.rag.evidencia.ultimo_top_id,
            rag_top_score=self.rag.evidencia.ultimo_top_score,
            agente_passos=resultado["passos"],
            agente_ferramentas=list(resultado["ferramentas_usadas"]),
            mcp_ferramentas_registradas=self.servidor.evidencia.ferramentas_registradas,
            mcp_chamadas=self.servidor.evidencia.chamadas_atendidas,
            mcp_metodo=self.servidor.evidencia.ultimo_metodo,
        )
        return ResultadoFluxo(resposta=resultado["resposta"], evidencia=evidencia)
