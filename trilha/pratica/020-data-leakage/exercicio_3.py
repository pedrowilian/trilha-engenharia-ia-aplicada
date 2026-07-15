"""Licao 020 — Exercicio 3: leakage temporal (mudanca de regime).

Tarefa:
- Use np.random.default_rng(8), T=220, t=arange(T).
  serie = (0.15*t para t<110, senao 0.15*110 + 1.4*(t-110)) + N(0,3).
- Ajuste uma reta (polyfit grau 1) e avalie o MSE em dois splits:
  (a) aleatorio: treino=perm[:165], teste=perm[165:] (perm = rng.permutation(T));
  (b) temporal: treino=arange(165), teste=arange(165, T).
- Imprima `erro split aleatorio (otimista): ...`, `erro split temporal (honesto): ...`
  (2 casas) e `split temporal e mais conservador: <bool>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/020-data-leakage/solucao_3.saida.txt
"""
import numpy as np


def main():
    raise NotImplementedError


if __name__ == "__main__":
    main()
