"""Exercício 3 — Round-trip request → JSON → request (ida-e-volta).

Setup: a request
    request = {"jsonrpc": "2.0", "id": 3, "method": "prompts/get",
               "params": {"name": "resumir", "arguments": {"n": 2}}}

Tarefa (ida-e-volta / round-trip):
    Serialize com `json.dumps(request, ensure_ascii=False, sort_keys=True)`,
    parseie de volta com `json.loads` e verifique a IGUALDADE EXATA entre o dict
    final e o original. Imprima a string JSON (`linha:`), `igual?` (com
    `volta == request`) e `re-serializa identico?` comparando
    `json.dumps(volta, ...)` com a string original.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/074-mcp-jsonrpc/solucao_3.saida.txt
    (em particular, `igual? True`).
"""
import json

request = {
    "jsonrpc": "2.0",
    "id": 3,
    "method": "prompts/get",
    "params": {"name": "resumir", "arguments": {"n": 2}},
}

# TODO: serializar (sort_keys=True), parsear de volta e checar igualdade exata.
