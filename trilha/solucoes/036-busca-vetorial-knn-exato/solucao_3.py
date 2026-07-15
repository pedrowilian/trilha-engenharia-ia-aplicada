"""Solução de referência — Exercício 3 da Lição 036.

Mede o custo da busca exata: uma varredura linear calcula UMA distância por
vetor da base, e cada distância custa O(d) operações. Logo o custo total é
O(n*d) — o motivo que justifica a busca aproximada (ANN) das próximas lições.
"""
import math


class BaseVetorial:
    def __init__(self, vetores):
        self.vetores = vetores
        self.calculos_distancia = 0

    def _l2(self, u, v):
        self.calculos_distancia += 1
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))

    def busca_exata(self, q):
        return min(self.vetores,
                   key=lambda nome: (self._l2(q, self.vetores[nome]), nome))


# Base determinística: 8 vetores em 4 dimensões.
vetores = {f"v{i}": [i, i + 1, i + 2, i + 3] for i in range(8)}
base = BaseVetorial(vetores)
q = [3.0, 3.0, 3.0, 3.0]

resultado = base.busca_exata(q)
n = len(vetores)
d = len(q)
print("mais proximo:", resultado)
print("calculos de distancia:", base.calculos_distancia)
print(f"custo O(n*d) = {n} * {d} = {n * d} operacoes por consulta")
