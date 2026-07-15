"""Solução de referência — Exercício 1 da Lição 096.

Scan de segurança/compliance: regras determinísticas inspecionam uma
configuração e emitem achados com severidade.
"""


def scan(config):
    achados = []
    if config.get("public", False):
        achados.append(("HIGH", "recurso exposto publicamente"))
    if not config.get("encryption", False):
        achados.append(("MEDIUM", "armazenamento sem criptografia"))
    if config.get("user") == "root":
        achados.append(("HIGH", "execucao como root"))
    return achados


config = {"public": False, "encryption": False, "user": "admin"}
achados = scan(config)
for sev, msg in achados:
    print(f"[{sev}] {msg}")
print("total:", len(achados))
