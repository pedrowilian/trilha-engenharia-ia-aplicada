"""Solução de referência — Exercício 1 da Lição 004.

Verifica a equação de autovalores A·v = λ·v para uma matriz simétrica e
confirma as identidades traço = soma dos autovalores e det = produto dos
autovalores.
"""
import numpy as np

B = np.array([[4.0, 1.0],
              [1.0, 4.0]])

# eigh: matriz simétrica -> autovalores reais em ordem crescente.
valores, vetores = np.linalg.eigh(B)

print(f"Autovalores: {[round(float(v), 4) for v in valores]}")
print(f"Traco={np.trace(B):.4f} soma={valores.sum():.4f}")
print(f"Det={np.linalg.det(B):.4f} produto={np.prod(valores):.4f}")

res_max = max(
    np.linalg.norm(B @ vetores[:, i] - valores[i] * vetores[:, i])
    for i in range(len(valores))
)
print(f"residuo maximo: {res_max:.6f}")
ok = abs(np.trace(B) - valores.sum()) < 1e-9 and res_max < 1e-9
print("OK" if ok else "FALHOU")
