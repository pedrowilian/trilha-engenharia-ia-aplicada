"""Exercício 2 — Cabeçalhos de autenticação com chave mascarada.

Setup: a chave de API `chave`, abaixo.

Tarefa:
    Implemente `mascarar(chave, visivel=4)` que substitui todos os caracteres
    por '*' exceto os últimos `visivel`. Implemente `montar_headers(api_key)`
    devolvendo um dict com "Authorization" (`Bearer <mascarada>`) e
    "Content-Type" ("application/json"). Imprima cada header em ordem
    alfabética de chave, no formato `chave: valor`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/051-apis-provedores-llm/solucao_2.saida.txt
"""

chave = "sk-ABCDEF1234567890"

# TODO: implementar mascarar(), montar_headers() e imprimir os headers.
