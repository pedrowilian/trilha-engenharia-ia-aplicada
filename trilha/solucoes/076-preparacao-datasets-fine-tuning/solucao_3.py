"""Solução de referência — Exercício 3 da Lição 076 (round-trip JSONL).

Serializa registros de chat em JSONL e os parseia de volta, confirmando a
igualdade exata do ciclo parse -> serialize -> parse (ida-e-volta).
"""
import json

registros = [
    {"messages": [
        {"role": "system", "content": "Voce e um tutor."},
        {"role": "user", "content": "O que e LoRA?"},
        {"role": "assistant", "content": "Adaptacao de baixo posto."},
    ]},
    {"messages": [
        {"role": "user", "content": "2+2?"},
        {"role": "assistant", "content": "4"},
    ]},
]


def serializar(regs):
    return "\n".join(json.dumps(r, ensure_ascii=False, sort_keys=True) for r in regs)


def parsear(texto):
    return [json.loads(linha) for linha in texto.splitlines() if linha.strip()]


um = parsear(serializar(registros))
dois = parsear(serializar(um))
print("linhas:", len(um))
print("round-trip parse->serialize->parse exato:", um == dois)
print("igual ao original:", um == registros)
