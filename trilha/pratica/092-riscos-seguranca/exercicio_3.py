"""Exercício 3 — Redação de PII.

Setup: `texto = "Fale com joao.silva@empresa.com.br ou bruno@x.io; tel (21) 99888-7766."`

Tarefa:
    Use `re.subn` para substituir e-mails (`[\\w.]+@[\\w.]+`) por `"[EMAIL]"` e
    telefones (`\\(\\d{2}\\) \\d{4,5}-\\d{4}`) por `"[TELEFONE]"`, contando as
    substituições. Imprima o texto redigido, depois `"emails redigidos: {n}"` e
    `"telefones redigidos: {n}"`.

Critério de conclusão (binário): a saída deve ser idêntica a
    trilha/solucoes/092-riscos-seguranca/solucao_3.saida.txt
"""
import re

# TODO: redija e-mails e telefones com re.subn e conte as substituições.
