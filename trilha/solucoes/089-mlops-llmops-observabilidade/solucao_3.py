"""Solucao de referencia - Exercicio 3 da Licao 089.

Decisao de rollout canary: a nova versao (canary) so e promovida se nao piorar a
taxa de erro nem o p95 alem de uma margem em relacao a versao atual (baseline).
Caso contrario, rollback. E o portao automatico que protege producao.
"""

baseline = {"taxa_erro": 0.03, "p95_ms": 500}
canary = {"taxa_erro": 0.02, "p95_ms": 510}
margem_erro = 0.01
margem_p95 = 50

erro_ok = canary["taxa_erro"] <= baseline["taxa_erro"] + margem_erro
p95_ok = canary["p95_ms"] <= baseline["p95_ms"] + margem_p95
promover = erro_ok and p95_ok

print(f"erro: baseline={baseline['taxa_erro']:.2f} canary={canary['taxa_erro']:.2f} ok={erro_ok}")
print(f"p95: baseline={baseline['p95_ms']} canary={canary['p95_ms']} ok={p95_ok}")
print(f"decisao: {'promover' if promover else 'rollback'}")
