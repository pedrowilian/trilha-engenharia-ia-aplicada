"""Exercício 3 — Lição 007: Regra da cadeia (backprop de um neurônio).

Tarefa:
  Seja L(w) = (w*x - y)^2 com w = 2, x = 3, y = 5. Calcule o forward
  (z = w*x e L) e o gradiente do peso pela regra da cadeia:
  dL/dw = 2 * (w*x - y) * x. Imprima z, L e dL/dw.

Critério de conclusão (binário): a saída deve ser exatamente
  z = 6.0
  L = 1.0
  dL/dw = 6.0
Solução de referência: trilha/solucoes/007-derivadas-parciais-gradiente-regra-da-cadeia/solucao_3.py
"""


def forward(w, x, y):
    # TODO: calcule z = w * x e L = (z - y) ** 2 e retorne (z, L)
    raise NotImplementedError


def grad_w(w, x, y):
    # TODO: implemente dL/dw = 2 * (w * x - y) * x
    raise NotImplementedError


w, x, y = 2.0, 3.0, 5.0
# TODO: imprima z, L e dL/dw.
