"""Componente RAG — recuperação em memória sobre um corpus minúsculo.

Implementação determinística e offline: indexa documentos por frequência de
termos (bag-of-words) e pontua a consulta por similaridade de cosseno. Não há
rede, banco de dados externo nem modelo de linguagem — apenas Python puro, para
que o resultado seja sempre o mesmo e verificável.

A evidência de execução (quantos documentos foram consultados e qual o top-1
com seu score) é retornada junto do resultado, e é o que prova, no fluxo
ponta a ponta, que o componente de recuperação efetivamente rodou.
"""
from __future__ import annotations

import math
import re
import unicodedata
from dataclasses import dataclass, field


def _normalizar(texto: str) -> str:
    """Minúsculas + remoção de acentos, para casar termos de forma estável."""
    texto = texto.lower()
    texto = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in texto if not unicodedata.combining(c))


def tokenizar(texto: str) -> list[str]:
    """Tokeniza em palavras alfanuméricas (determinístico, sem dependências)."""
    return re.findall(r"[a-z0-9]+", _normalizar(texto))


@dataclass(frozen=True)
class Documento:
    """Um documento do corpus: identificador estável + texto."""

    doc_id: str
    texto: str


@dataclass(frozen=True)
class Recuperado:
    """Um resultado de recuperação: documento + score arredondado."""

    doc_id: str
    texto: str
    score: float


@dataclass
class EvidenciaRag:
    """Evidência observável de que o RAG executou."""

    consultas: int = 0
    documentos_indexados: int = 0
    ultimo_top_id: str = ""
    ultimo_top_score: float = 0.0

    def executou(self) -> bool:
        return self.consultas > 0


def _frequencias(tokens: list[str]) -> dict[str, int]:
    freq: dict[str, int] = {}
    for tok in tokens:
        freq[tok] = freq.get(tok, 0) + 1
    return freq


def _cosseno(a: dict[str, int], b: dict[str, int]) -> float:
    if not a or not b:
        return 0.0
    comuns = set(a) & set(b)
    produto = sum(a[t] * b[t] for t in comuns)
    norma_a = math.sqrt(sum(v * v for v in a.values()))
    norma_b = math.sqrt(sum(v * v for v in b.values()))
    if norma_a == 0.0 or norma_b == 0.0:
        return 0.0
    return produto / (norma_a * norma_b)


@dataclass
class RagEmMemoria:
    """Índice de recuperação em memória sobre um corpus fixo."""

    documentos: list[Documento]
    evidencia: EvidenciaRag = field(default_factory=EvidenciaRag)
    _indice: dict[str, dict[str, int]] = field(default_factory=dict, init=False)

    def __post_init__(self) -> None:
        for doc in self.documentos:
            self._indice[doc.doc_id] = _frequencias(tokenizar(doc.texto))
        self.evidencia.documentos_indexados = len(self.documentos)

    def recuperar(self, consulta: str, k: int = 1) -> list[Recuperado]:
        """Retorna os `k` documentos mais similares à consulta.

        Desempate determinístico: maior score primeiro; em empate, doc_id em
        ordem lexicográfica crescente.
        """
        freq_consulta = _frequencias(tokenizar(consulta))
        pontuados: list[Recuperado] = []
        textos = {d.doc_id: d.texto for d in self.documentos}
        for doc_id, freq_doc in self._indice.items():
            score = round(_cosseno(freq_consulta, freq_doc), 4)
            pontuados.append(Recuperado(doc_id, textos[doc_id], score))
        pontuados.sort(key=lambda r: (-r.score, r.doc_id))
        topo = pontuados[:k]

        self.evidencia.consultas += 1
        if topo:
            self.evidencia.ultimo_top_id = topo[0].doc_id
            self.evidencia.ultimo_top_score = topo[0].score
        return topo


def corpus_padrao() -> list[Documento]:
    """Corpus minúsculo de uma base de conhecimento de suporte (fixo)."""
    return [
        Documento("doc-senha",
                  "Para redefinir a senha acesse configuracoes e clique em "
                  "redefinir senha. Um email de redefinicao sera enviado."),
        Documento("doc-fatura",
                  "A fatura e gerada todo dia primeiro. Voce pode baixar a "
                  "fatura em PDF no painel de cobranca."),
        Documento("doc-reembolso",
                  "Reembolsos sao processados em ate cinco dias uteis apos a "
                  "solicitacao de reembolso no painel."),
        Documento("doc-limite-api",
                  "O limite da API e de mil requisicoes por minuto no plano "
                  "padrao da plataforma."),
    ]
