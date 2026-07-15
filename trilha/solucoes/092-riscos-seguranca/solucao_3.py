"""Solução de referência — Exercício 3 da Lição 092.

Redação de PII: substitui e-mails e telefones por marcadores, contando quantos
trechos sensíveis foram removidos. Determinístico.
"""
import re

texto = "Fale com joao.silva@empresa.com.br ou bruno@x.io; tel (21) 99888-7766."

texto, n_email = re.subn(r"[\w.]+@[\w.]+", "[EMAIL]", texto)
texto, n_tel = re.subn(r"\(\d{2}\) \d{4,5}-\d{4}", "[TELEFONE]", texto)

print(texto)
print(f"emails redigidos: {n_email}")
print(f"telefones redigidos: {n_tel}")
