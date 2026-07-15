"""Solução de referência — Exercício 1 da Lição 095.

Copiloto de IaC: gera um manifesto a partir da intenção e o valida contra
políticas determinísticas. Saída exata e reprodutível.
"""


def gerar_manifesto(intencao):
    return {
        "kind": "Deployment",
        "name": intencao["servico"],
        "replicas": intencao.get("replicas", 1),
        "port": intencao.get("porta", 80),
    }


def validar(manifesto):
    erros = []
    if manifesto["replicas"] < 2:
        erros.append("replicas<2")
    if not (1024 <= manifesto["port"] <= 65535):
        erros.append("porta fora da faixa")
    return erros


intencao = {"servico": "cache", "replicas": 1, "porta": 80}
manifesto = gerar_manifesto(intencao)
erros = validar(manifesto)

print("servico:", manifesto["name"])
print("erros:", erros)
