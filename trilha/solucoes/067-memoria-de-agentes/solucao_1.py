"""Solução de referência — Exercício 1 da Lição 067.

Memória de curto prazo: buffer de tamanho fixo (deque) que mantém apenas os
eventos mais recentes. Determinístico.
"""
from collections import deque

curto = deque(maxlen=2)
for evento in ["p1", "p2", "p3", "p4"]:
    curto.append(evento)
    print("buffer:", list(curto))

print("janela final:", list(curto))
