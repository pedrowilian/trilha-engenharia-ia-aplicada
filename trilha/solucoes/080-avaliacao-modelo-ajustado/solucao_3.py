"""Solução de referência — Exercício 3 da Lição 080.

Detecta overfitting comparando as curvas de perda de treino e validação,
localizando a melhor época (mínimo da validação) e recomendando early stopping.
"""
treino = [1.00, 0.70, 0.50, 0.38, 0.30, 0.24, 0.20]
validacao = [1.05, 0.80, 0.62, 0.55, 0.57, 0.63, 0.71]

melhor = min(range(len(validacao)), key=lambda i: validacao[i])
gap = validacao[melhor] - treino[melhor]
overfitting = any(validacao[i + 1] > validacao[i] for i in range(melhor, len(validacao) - 1))

print("epocas:", len(validacao))
print("melhor epoca (min val):", melhor)
print(f"val minima: {validacao[melhor]:.2f}")
print(f"gap treino-val na melhor epoca: {gap:.2f}")
print("overfitting detectado:", overfitting)
print("recomendacao: early stopping na epoca", melhor)
