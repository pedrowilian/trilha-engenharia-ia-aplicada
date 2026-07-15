"""Solução de referência — Exercício 1 da Lição 051.

Constrói o corpo (payload) de uma requisição de chat no formato comum às APIs
de LLM (lista de mensagens com papéis) e o serializa em JSON canônico. Nenhuma
chamada de rede é feita: apenas a *forma* da requisição é montada localmente.
"""
import json


def construir_requisicao(modelo, sistema, usuario, temperatura):
    return {
        "model": modelo,
        "messages": [
            {"role": "system", "content": sistema},
            {"role": "user", "content": usuario},
        ],
        "temperature": temperatura,
    }


req = construir_requisicao(
    "llm-pequeno",
    "Voce e um assistente conciso.",
    "Explique JSON em uma frase.",
    0.2,
)
corpo = json.dumps(req, ensure_ascii=False, sort_keys=True)
print("n mensagens:", len(req["messages"]))
print("papeis:", [m["role"] for m in req["messages"]])
print("json:", corpo)
