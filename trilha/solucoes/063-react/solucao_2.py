"""Solução de referência — Exercício 2 da Lição 063.

Parsing da ação no formato `ferramenta[arg1, arg2, ...]`. Ações inválidas
viram `("?", [])`. Determinístico.
"""
import re


def parse_acao(texto):
    m = re.match(r"\s*(\w+)\[(.*)\]\s*$", texto)
    if not m:
        return ("?", [])
    args = [a.strip() for a in m.group(2).split(",") if a.strip()]
    return (m.group(1), args)


for s in ["soma[1, 2, 3]", "kb[capital]", "ruim"]:
    nome, args = parse_acao(s)
    print(f"{s!r} -> nome={nome} args={args}")
