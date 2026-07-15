"""Exercício 1 — Montar o corpo de uma requisição de chat.

Setup: o modelo, o texto de sistema, a mensagem do usuário e a temperatura,
abaixo. Nenhuma chamada de rede é feita.

Tarefa:
    Implemente `construir_requisicao(modelo, sistema, usuario, temperatura)`
    que devolve um dict com as chaves "model", "messages" (lista de
    {"role", "content"} com system e user) e "temperature". Serialize com
    `json.dumps(req, ensure_ascii=False, sort_keys=True)` e imprima:
        n mensagens: 2
        papeis: ['system', 'user']
        json: {...}

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/051-apis-provedores-llm/solucao_1.saida.txt
"""
import json

modelo = "llm-pequeno"
sistema = "Voce e um assistente conciso."
usuario = "Explique JSON em uma frase."
temperatura = 0.2

# TODO: construir a requisicao, serializar e imprimir.
