"""Solução de referência — Exercício 3 da Lição 004.

PCA "na mão": centraliza os dados, calcula a matriz de covariância, obtém as
variâncias por componente principal (autovalores) e determina quantos
componentes são necessários para explicar >= 90% da variância total.
"""
import numpy as np

X = np.array([
    [2.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [-2.0, 0.0, 0.0],
    [0.0, -1.0, 0.0],
])

Xc = X - X.mean(axis=0)
cov = (Xc.T @ Xc) / (len(X) - 1)

valores, _ = np.linalg.eigh(cov)
valores = np.sort(valores)[::-1]
valores = np.clip(valores, 0.0, None)        # remove ruído numérico negativo

razao = valores / valores.sum()
acum = np.cumsum(razao)

print(f"Razao de variancia explicada: {[round(float(r), 4) + 0.0 for r in razao]}")
print(f"Variancia acumulada: {[round(float(a), 4) for a in acum]}")
k = int(np.argmax(acum >= 0.90)) + 1
print(f"Componentes para >=90% da variancia: {k}")
