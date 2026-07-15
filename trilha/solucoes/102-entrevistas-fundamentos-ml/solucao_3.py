"""Solucao de referencia - Exercicio 3 da Licao 102.

Gradient descent 1D sobre L(theta) = (theta - 7)^2, gradiente 2*(theta-7).
Liga os fundamentos cobrados em entrevista (gradient descent/backprop): cada
passo encolhe a distancia ao minimo pelo fator |1 - 2*eta|.
"""


def perda(theta):
    return (theta - 7.0) ** 2


def gradiente(theta):
    return 2.0 * (theta - 7.0)


theta = 0.0
eta = 0.1
print(f"theta inicial: {theta:.4f} perda inicial: {perda(theta):.4f}")
for passo in range(1, 61):
    theta = theta - eta * gradiente(theta)
    if passo in (1, 10, 30, 60):
        print(f"passo {passo:2d}: theta={theta:.4f} perda={perda(theta):.4f}")
print(f"theta final: {theta:.4f} perda final: {perda(theta):.4f}")
