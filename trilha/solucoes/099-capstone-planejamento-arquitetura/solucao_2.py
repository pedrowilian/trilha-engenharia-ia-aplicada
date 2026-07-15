"""Solução de referência — Exercício 2 da Lição 099.

Ordena os componentes pela dependência (quem depende de quem) para obter a ordem
de montagem (dependências primeiro) e o fluxo da requisição (ordem inversa).
Determinístico: desempate alfabético.
"""

dependencias = {
    "cliente_mcp": ["servidor_mcp"],
    "servidor_mcp": ["agente"],
    "agente": ["rag"],
    "rag": [],
}


def ordem_de_montagem(deps):
    pendentes = dict(deps)
    ordem = []
    while pendentes:
        prontos = sorted(n for n, ds in pendentes.items()
                         if all(d not in pendentes for d in ds))
        for n in prontos:
            ordem.append(n)
            del pendentes[n]
    return ordem


ordem = ordem_de_montagem(dependencias)
print("ordem de montagem (dependencias primeiro):")
for i, n in enumerate(ordem, 1):
    print(f"  {i}. {n}")
print("fluxo da requisicao:", " -> ".join(reversed(ordem)))
