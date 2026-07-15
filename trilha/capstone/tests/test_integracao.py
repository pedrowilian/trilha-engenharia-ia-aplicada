"""Teste de integração do capstone — exercita RAG + agente + MCP.

Verifica, com asserções sobre a evidência observável, que cada um dos três
componentes participou do fluxo ponta a ponta, e que a ausência de qualquer
componente é detectável.

Execute com:
    python3 -m pytest trilha/capstone/tests/
"""
from __future__ import annotations

import sys
from pathlib import Path

# Garante que o pacote `capstone` seja importável independentemente do cwd.
RAIZ = Path(__file__).resolve().parents[2]
if str(RAIZ) not in sys.path:
    sys.path.insert(0, str(RAIZ))

from capstone.src.agent import Agente  # noqa: E402
from capstone.src.mcp_client import ClienteMcp  # noqa: E402
from capstone.src.mcp_server import ServidorMcp  # noqa: E402
from capstone.src.pipeline import MicroSaaS  # noqa: E402
from capstone.src.rag import Documento, RagEmMemoria, corpus_padrao  # noqa: E402


# --- Evidência ponta a ponta: os três componentes executam --------------------


def test_fluxo_completo_executa_os_tres_componentes():
    app = MicroSaaS()
    resultado = app.executar("Como redefinir minha senha?")
    ev = resultado.evidencia

    estados = ev.componentes_executados()
    assert estados == {"rag": True, "agente": True, "mcp": True}
    assert ev.completo() is True


# --- Evidência específica de cada componente ----------------------------------


def test_evidencia_rag_recuperou_documento_relevante():
    app = MicroSaaS()
    resultado = app.executar("Como redefinir minha senha?")
    ev = resultado.evidencia
    # RAG: consultou ao menos uma vez e recuperou o documento correto com score > 0.
    assert ev.rag_consultas >= 1
    assert ev.rag_top_id == "doc-senha"
    assert ev.rag_top_score > 0.0


def test_evidencia_agente_usou_ferramenta():
    rag = RagEmMemoria(corpus_padrao())
    agente = Agente(rag)
    resposta = agente.responder("Como redefinir minha senha?")
    # Agente: executou ao menos um passo e usou uma ferramenta registrada.
    assert resposta.evidencia.passos >= 1
    assert "buscar_documentos" in resposta.evidencia.ferramentas_usadas
    assert resposta.trace[0].ferramenta == "buscar_documentos"


def test_evidencia_agente_seleciona_ferramenta_de_contagem():
    rag = RagEmMemoria(corpus_padrao())
    agente = Agente(rag)
    resposta = agente.responder("Quantos documentos existem na base?")
    assert resposta.evidencia.ferramentas_usadas == ["contar_documentos"]


def test_evidencia_mcp_lista_e_invoca_ferramenta():
    rag = RagEmMemoria(corpus_padrao())
    servidor = ServidorMcp(Agente(rag))
    cliente = ClienteMcp(servidor)

    ferramentas = cliente.listar_ferramentas()
    nomes = [f["name"] for f in ferramentas]
    assert "responder_suporte" in nomes

    resultado = cliente.chamar("responder_suporte", {"pergunta": "Como baixar a fatura?"})
    # MCP: servidor registrou ferramentas e atendeu chamadas (list + call).
    assert servidor.evidencia.ferramentas_registradas >= 1
    assert servidor.evidencia.chamadas_atendidas >= 2
    assert servidor.evidencia.ultimo_metodo == "tools/call"
    assert "doc-fatura" in resultado["resposta"]


# --- Detecção de componente ausente -------------------------------------------


def test_detecta_componente_mcp_ausente():
    """Se o cliente nunca invoca o servidor MCP, o fluxo é detectado incompleto.

    Simula a falta do componente MCP indo direto do agente ao RAG, sem passar
    pelo servidor/cliente. A evidência do MCP fica zerada e `completo()` é False.
    """
    from capstone.src.pipeline import EvidenciaFluxo

    rag = RagEmMemoria(corpus_padrao())
    agente = Agente(rag)
    resposta = agente.responder("Como redefinir minha senha?")

    evidencia = EvidenciaFluxo(
        rag_consultas=rag.evidencia.consultas,
        rag_top_id=rag.evidencia.ultimo_top_id,
        rag_top_score=rag.evidencia.ultimo_top_score,
        agente_passos=resposta.evidencia.passos,
        agente_ferramentas=list(resposta.evidencia.ferramentas_usadas),
        mcp_ferramentas_registradas=0,
        mcp_chamadas=0,  # MCP nunca foi acionado
        mcp_metodo="",
    )
    estados = evidencia.componentes_executados()
    assert estados["rag"] is True
    assert estados["agente"] is True
    assert estados["mcp"] is False
    assert evidencia.completo() is False


def test_detecta_chamada_a_ferramenta_inexistente():
    """Invocar uma ferramenta não registrada no MCP gera erro explícito."""
    rag = RagEmMemoria(corpus_padrao())
    servidor = ServidorMcp(Agente(rag))
    cliente = ClienteMcp(servidor)

    try:
        cliente.chamar("ferramenta_inexistente", {})
    except RuntimeError as exc:
        assert "desconhecida" in str(exc)
    else:  # pragma: no cover - falha de teste se não levantar
        raise AssertionError("esperava RuntimeError para ferramenta inexistente")
