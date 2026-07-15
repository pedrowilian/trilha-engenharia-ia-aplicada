"""Solução de referência — Exercício 2 da Lição 093.

Checklist de conformidade: fração de requisitos atendidos e status segundo o
limiar de 80%. Determinístico.
"""
requisitos = {
    "documentacao_tecnica": True,
    "supervisao_humana": True,
    "registro_de_logs": True,
    "avaliacao_de_risco": True,
    "transparencia_ao_usuario": False,
}

atendidos = sum(1 for v in requisitos.values() if v)
total = len(requisitos)
score = atendidos / total
print(f"requisitos atendidos: {atendidos}/{total}")
print(f"conformidade: {score:.0%}")
print(f"status: {'conforme' if score >= 0.8 else 'pendente'}")
