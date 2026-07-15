"""Solução de referência — Exercício 2 da Lição 100.

Agente determinístico: escolhe a ferramenta por palavra-chave e a executa.
Perguntas com "quantos"/"quantidade" usam `contar`; as demais usam `buscar`.
"""


def buscar(consulta):
    return f"resultado para {consulta!r}"


def contar(consulta):
    return "3 documentos na base"


ferramentas = {"buscar": buscar, "contar": contar}


def decidir(pergunta):
    p = pergunta.lower()
    if "quantos" in p or "quantidade" in p:
        return "contar"
    return "buscar"


perguntas = [
    "Como redefinir a senha?",
    "Quantos documentos existem?",
    "Onde baixo a fatura?",
]
for pergunta in perguntas:
    nome = decidir(pergunta)
    obs = ferramentas[nome](pergunta)
    print(f"ferramenta={nome} obs={obs}")
