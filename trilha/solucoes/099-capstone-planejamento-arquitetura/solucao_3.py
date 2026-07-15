"""Solução de referência — Exercício 3 da Lição 099.

Contrato de evidência observável: cada componente expõe um contador e o fluxo só
é considerado completo quando os três contadores são > 0. Para cada cenário,
imprime se está completo e quais componentes estão ausentes. Determinístico.
"""
from dataclasses import dataclass


@dataclass
class Evidencia:
    rag: int = 0
    agente: int = 0
    mcp: int = 0

    def completo(self):
        return self.rag > 0 and self.agente > 0 and self.mcp > 0

    def ausentes(self):
        return [c for c in ("rag", "agente", "mcp") if getattr(self, c) == 0]


cenarios = {
    "completo": Evidencia(rag=1, agente=1, mcp=2),
    "sem_rag": Evidencia(rag=0, agente=1, mcp=2),
    "vazio": Evidencia(),
}
for nome in ("completo", "sem_rag", "vazio"):
    ev = cenarios[nome]
    print(f"{nome}: completo={ev.completo()} ausentes={ev.ausentes()}")
