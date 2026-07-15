"""Exercício 1 — Upload simulado com validação de JSONL.

Setup: a classe `ClienteSimulado` (a implementar) NÃO faz chamadas de rede.

Tarefa:
    Implemente `ClienteSimulado.upload(linhas)` que valida cada linha (deve ter
    'messages' não vazia, senão `raise ValueError(f"linha {i} invalida: sem
    'messages'")`) e retorna {id: "file-0001", n_exemplos, status:
    "processed"}. Faça upload de 3 linhas válidas (imprima id, n e status) e
    depois de uma lista com uma linha inválida, capturando e imprimindo o erro.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/079-fine-tuning-openai-api/solucao_1.saida.txt
"""
import json

# TODO: implementar ClienteSimulado e exercitar upload válido + inválido.
