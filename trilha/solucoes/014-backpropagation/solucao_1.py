"""Solucao de referencia — Licao 014, Exercicio 1.

Backprop em um grafo computacional: f = (a + b) * (b + c).
Forward guarda intermediarios; backward aplica a regra da cadeia.
"""


def main():
    a, b, c = 1.0, 2.0, 3.0
    # forward
    u = a + b          # 3
    v = b + c          # 5
    f = u * v          # 15
    # backward
    df_du = v          # f = u*v => df/du = v
    df_dv = u          # df/dv = u
    df_da = df_du * 1.0
    df_db = df_du * 1.0 + df_dv * 1.0   # b alimenta u e v (gradientes somam)
    df_dc = df_dv * 1.0
    print(f"forward: u={u} v={v} f={f}")
    print(f"df/da={df_da} df/db={df_db} df/dc={df_dc}")


if __name__ == "__main__":
    main()
