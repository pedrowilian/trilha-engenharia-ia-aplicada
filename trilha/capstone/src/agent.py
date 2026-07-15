"""Componente Agente — laço ReAct determinístico com uso de ferramentas.

O agente recebe uma pergunta de suporte e decide, por uma política explícita
(baseada em palavras-chave), qual ferramenta chamar. As ferramentas são
funções Python registradas — uma delas consulta o RAG. O agente registra um
*trace* (pensamento → ação → observação) que serve de evidência observável de
que o componente de orquestração rodou.

Sem LLM e sem rede: a "decisão" é uma função pura e determinística, então a
mesma pergunta sempre produz o mesmo trace.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

from .rag import RagEmMemoria, _normalizar


@dataclass
class PassoTrace:
    """Um passo do raciocínio do agente."""

    pensamento: str
    ferramenta: str
    observacao: str


@dataclass
class EvidenciaAgente:
    """Evidência observável de que o agente executou."""

    passos: int = 0
    ferramentas_usadas: list[str] = field(default_factory=list)

    def executou(self) -> bool:
        return self.passos > 0


@dataclass
class RespostaAgente:
    """Resultado final do agente: resposta + trace + evidência."""

    resposta: str
    trace: list[PassoTrace]
    evidencia: EvidenciaAgente


class Agente:
    """Agente determinístico que escolhe uma ferramenta por palavra-chave."""

    def __init__(self, rag: RagEmMemoria) -> None:
        self.rag = rag
        self.ferramentas: dict[str, Callable[[str], str]] = {
            "buscar_documentos": self._ferramenta_buscar,
            "contar_documentos": self._ferramenta_contar,
        }

    def _ferramenta_buscar(self, consulta: str) -> str:
        topo = self.rag.recuperar(consulta, k=1)
        if not topo:
            return "nenhum documento encontrado"
        melhor = topo[0]
        return f"{melhor.doc_id} (score={melhor.score:.4f})"

    def _ferramenta_contar(self, consulta: str) -> str:
        return f"{len(self.rag.documentos)} documentos na base"

    def _decidir(self, pergunta: str) -> str:
        """Política determinística: escolhe a ferramenta pela pergunta."""
        texto = _normalizar(pergunta)
        if "quantos" in texto or "quantidade" in texto:
            return "contar_documentos"
        return "buscar_documentos"

    def responder(self, pergunta: str) -> RespostaAgente:
        evidencia = EvidenciaAgente()
        trace: list[PassoTrace] = []

        nome_ferramenta = self._decidir(pergunta)
        pensamento = f"a pergunta exige a ferramenta '{nome_ferramenta}'"
        observacao = self.ferramentas[nome_ferramenta](pergunta)
        trace.append(PassoTrace(pensamento, nome_ferramenta, observacao))
        evidencia.passos += 1
        evidencia.ferramentas_usadas.append(nome_ferramenta)

        resposta = f"resposta via {nome_ferramenta}: {observacao}"
        return RespostaAgente(resposta=resposta, trace=trace, evidencia=evidencia)
