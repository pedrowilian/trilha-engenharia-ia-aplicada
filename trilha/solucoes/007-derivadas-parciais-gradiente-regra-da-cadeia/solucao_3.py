"""Solução de referência — Exercício 3 (Lição 007).

Regra da cadeia aplicada a um neurônio: L(w) = (w*x - y)^2.
Pela regra da cadeia, dL/dw = 2 * (w*x - y) * x  (gradiente do peso, base do backprop).
"""


def forward(w, x, y):
    z = w * x
    L = (z - y) ** 2
    return z, L


def grad_w(w, x, y):
    z = w * x
    return 2.0 * (z - y) * x


w, x, y = 2.0, 3.0, 5.0
z, L = forward(w, x, y)

print(f"z = {z}")
print(f"L = {L}")
print(f"dL/dw = {grad_w(w, x, y)}")
