"""Licao 017 — Exercicio 1: diagnostico under/overfitting.

Tarefa:
- Implemente `diagnosticar(erro_treino, erro_val, limiar_alto=0.20, folga_max=0.10)`:
    * ambos os erros > limiar_alto  -> "underfitting"
    * (erro_val - erro_treino) > folga_max -> "overfitting"
    * caso contrario -> "bom ajuste"
- Para os casos A..D dados, imprima `<nome>: treino=.. val=.. -> <diagnostico>`.

Criterio binario: saida IDENTICA a
trilha/solucoes/017-overfitting-validacao-cruzada/solucao_1.saida.txt
"""


def diagnosticar(erro_treino, erro_val, limiar_alto=0.20, folga_max=0.10):
    raise NotImplementedError


def main():
    casos = [("A", 0.40, 0.42), ("B", 0.03, 0.25), ("C", 0.07, 0.10), ("D", 0.30, 0.31)]
    raise NotImplementedError


if __name__ == "__main__":
    main()
