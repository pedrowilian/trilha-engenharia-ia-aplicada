"""Solução de referência — Exercício 3 da Lição 077.

Matriz de decisão ponderada entre RAG e fine-tuning: cada critério tem um peso
e uma nota (0..5) para cada abordagem; o vencedor é o de maior total ponderado.
"""
criterios = [
    # (nome, peso, nota_rag, nota_ft)
    ("conhecimento muda rapido", 3, 5, 1),
    ("comportamento/estilo fixo", 3, 2, 5),
    ("controle total do modelo", 1, 1, 5),
    ("setup rapido", 2, 5, 1),
]

total_rag = sum(peso * sr for _, peso, sr, _ in criterios)
total_ft = sum(peso * sf for _, peso, _, sf in criterios)

print(f"{'criterio':<28}{'peso':>5}{'RAG':>5}{'FT':>5}")
for nome, peso, sr, sf in criterios:
    print(f"{nome:<28}{peso:>5}{sr:>5}{sf:>5}")
print("-" * 43)
print(f"{'TOTAL ponderado':<28}{'':>5}{total_rag:>5}{total_ft:>5}")
print("vencedor:", "RAG" if total_rag > total_ft else "fine-tuning" if total_ft > total_rag else "empate")
