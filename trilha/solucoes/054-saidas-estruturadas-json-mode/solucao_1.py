"""Solução de referência — Exercício 1 da Lição 054.

Faz o parsing de uma saída estruturada (JSON) "produzida pelo modelo" e extrai
os campos. Demonstra como tipos JSON viram tipos Python (true -> True).
"""
import json

saida_modelo = '{"nome": "Ana", "idade": 30, "ativo": true}'
dados = json.loads(saida_modelo)
print("tipo:", type(dados).__name__)
print("nome:", dados["nome"])
print("idade:", dados["idade"])
print("ativo:", dados["ativo"])
