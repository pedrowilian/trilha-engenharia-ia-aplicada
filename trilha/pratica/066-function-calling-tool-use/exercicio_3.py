"""Exercício 3 — Round-trip tool-call → JSON → tool-call (ida-e-volta).

Setup: a tool-call aninhada
    tool_call = {"name": "agendar",
                 "arguments": {"dia": "segunda", "hora": 9, "lembrete": True}}

Tarefa (ida-e-volta / round-trip):
    Serialize com `json.dumps(tool_call, ensure_ascii=False, sort_keys=True)`,
    parseie de volta com `json.loads` e verifique a IGUALDADE EXATA entre o dict
    final e o original. Imprima a string JSON (`json:`), `igual?` (com
    `volta == tool_call`) e `re-serializa identico?` comparando
    `json.dumps(volta, ...)` com a string original.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/066-function-calling-tool-use/solucao_3.saida.txt
    (em particular, `igual? True`).
"""
import json

tool_call = {
    "name": "agendar",
    "arguments": {"dia": "segunda", "hora": 9, "lembrete": True},
}

# TODO: serializar (sort_keys=True), parsear de volta e checar igualdade exata.
