"""Exercício 3 — Contrato de evidência observável.

Setup:
    cenarios = {
        "completo": Evidencia(rag=1, agente=1, mcp=2),
        "sem_rag": Evidencia(rag=0, agente=1, mcp=2),
        "vazio": Evidencia(),
    }

Tarefa:
    Crie uma dataclass `Evidencia` com contadores `rag`, `agente`, `mcp`
    (default 0), o método `completo()` (True sse os três são > 0) e
    `ausentes()` (lista dos componentes com contador 0, na ordem rag, agente,
    mcp). Para cada cenário (na ordem completo, sem_rag, vazio) imprima
    `nome: completo={...} ausentes={...}`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/099-capstone-planejamento-arquitetura/solucao_3.saida.txt.
"""
from dataclasses import dataclass


@dataclass
class Evidencia:
    rag: int = 0
    agente: int = 0
    mcp: int = 0
    # TODO: implemente completo() e ausentes().


# TODO: monte os cenarios e imprima completo/ausentes para cada um.
