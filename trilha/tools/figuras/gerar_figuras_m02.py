#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M02.

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Semente fixa de RNG onde há aleatoriedade.

Uso:
    python trilha/tools/figuras/gerar_figuras_m02.py

As imagens são salvas em:
    trilha/modulos/M02-redes-neurais-deep-learning/assets/<NNN>-<slug>/<nome>.png
e referenciadas nas lições por caminho RELATIVO (assets/<...>.png).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # backend não interativo (determinístico, sem display)

import matplotlib.pyplot as plt
import numpy as np

# --- Estilo fixo, independente da config do usuário -------------------------
plt.rcParams.update({
    "figure.dpi": 110,
    "savefig.dpi": 110,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# --- Localização dos assets (relativa a este arquivo) -----------------------
RAIZ_TRILHA = Path(__file__).resolve().parents[2]   # .../trilha
ASSETS = RAIZ_TRILHA / "modulos" / "M02-redes-neurais-deep-learning" / "assets"

COR_A = "#1f5fa8"
COR_B = "#c1432a"
COR_C = "#2e8b57"
COR_D = "#8a5fb0"
CINZA = "#9aa7b5"


def _salvar(fig, slug: str, nome: str) -> Path:
    """Salva a figura em assets/<slug>/<nome>.png e fecha a figura."""
    destino = ASSETS / slug / f"{nome}.png"
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, bbox_inches="tight")
    plt.close(fig)
    return destino


# ===========================================================================
# Lição 022 — Perceptron (separabilidade linear: AND vs XOR)
# ===========================================================================
SLUG_022 = "022-perceptron"


def fig_022_separabilidade_linear():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.6))
    pts = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)

    # AND: separavel por reta
    y_and = np.array([0, 0, 0, 1])
    for p, c in zip(pts, y_and):
        cor = COR_B if c == 1 else COR_A
        ax1.scatter(p[0], p[1], c=cor, s=120, zorder=3,
                    edgecolors="k", linewidths=0.6)
    xs = np.linspace(-0.3, 1.3, 50)
    ax1.plot(xs, 1.5 - xs, "--", color="#444", lw=1.6, label="reta separadora")
    ax1.set_title("AND: linearmente separável")
    ax1.legend(loc="upper right", fontsize=8)

    # XOR: nao separavel
    y_xor = np.array([0, 1, 1, 0])
    for p, c in zip(pts, y_xor):
        cor = COR_B if c == 1 else COR_A
        ax2.scatter(p[0], p[1], c=cor, s=120, zorder=3,
                    edgecolors="k", linewidths=0.6)
    ax2.set_title("XOR: nenhuma reta separa")

    for ax in (ax1, ax2):
        ax.set_xlim(-0.3, 1.3)
        ax.set_ylim(-0.3, 1.3)
        ax.set_xlabel(r"$x_1$")
        ax.set_ylabel(r"$x_2$")
        ax.set_aspect("equal")
    return _salvar(fig, SLUG_022, "separabilidade-linear")


# ===========================================================================
# Lição 023 — Funções de ativação
# ===========================================================================
SLUG_023 = "023-funcoes-de-ativacao"


def fig_023_ativacoes():
    from math import erf, sqrt
    z = np.linspace(-4, 4, 400)
    sig = 1.0 / (1.0 + np.exp(-z))
    th = np.tanh(z)
    relu = np.maximum(0.0, z)
    gelu = np.array([x * 0.5 * (1.0 + erf(x / sqrt(2.0))) for x in z])
    fig, ax = plt.subplots(figsize=(6.8, 4.8))
    ax.plot(z, sig, color=COR_A, label="sigmoid")
    ax.plot(z, th, color=COR_C, label="tanh")
    ax.plot(z, relu, color=COR_B, label="ReLU")
    ax.plot(z, gelu, color=COR_D, ls="--", label="GELU")
    ax.axhline(0, color="black", lw=0.7)
    ax.axvline(0, color="black", lw=0.7)
    ax.set_xlabel("z")
    ax.set_ylabel(r"$\phi(z)$")
    ax.set_title("Funções de ativação")
    ax.set_ylim(-1.5, 4)
    ax.legend(fontsize=9)
    return _salvar(fig, SLUG_023, "ativacoes")


# ===========================================================================
# Lição 024 — MLP (diagrama de arquitetura 2-4-1)
# ===========================================================================
SLUG_024 = "024-mlp"


def fig_024_mlp_arquitetura():
    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    ax.axis("off")
    camadas = [2, 4, 1]
    rotulos = ["entrada", "oculta (ReLU)", "saída"]
    xs = [0.0, 2.5, 5.0]
    posicoes = []
    for ci, (n, x) in enumerate(zip(camadas, xs)):
        ys = np.linspace(0, 3, n) if n > 1 else [1.5]
        col = []
        for y in ys:
            cor = COR_A if ci == 0 else (COR_B if ci == len(camadas) - 1 else COR_C)
            ax.add_patch(plt.Circle((x, y), 0.22, color="#eef2f7", ec=cor,
                                    lw=1.8, zorder=3))
            col.append((x, y))
        posicoes.append(col)
        ax.text(x, 3.5, rotulos[ci], ha="center", fontsize=10, color="#333")
    # arestas totalmente conectadas
    for esq, dir_ in zip(posicoes[:-1], posicoes[1:]):
        for (xo, yo) in esq:
            for (xd, yd) in dir_:
                ax.plot([xo + 0.22, xd - 0.22], [yo, yd], color=CINZA,
                        lw=0.8, zorder=1)
    ax.set_xlim(-0.6, 5.6)
    ax.set_ylim(-0.6, 4.0)
    ax.set_title("MLP 2-4-1: camadas densas totalmente conectadas")
    return _salvar(fig, SLUG_024, "mlp-arquitetura")


# ===========================================================================
# Lição 025 — Inicialização de pesos (variância das ativações)
# ===========================================================================
SLUG_025 = "025-treino-redes-profundas-inicializacao"


def fig_025_variancia_init():
    def propaga(escala, ativacao, n_camadas=6, n=256, semente=0):
        rng = np.random.default_rng(semente)
        a = rng.standard_normal(n)
        stds = []
        for _ in range(n_camadas):
            W = rng.standard_normal((n, n)) * escala(n)
            z = W @ a
            a = ativacao(z)
            stds.append(a.std())
        return stds

    ident = lambda z: z
    relu = lambda z: np.maximum(0.0, z)
    naive = propaga(lambda n: 1.0, ident)
    xavier = propaga(lambda n: 1.0 / np.sqrt(n), ident)
    he = propaga(lambda n: np.sqrt(2.0 / n), relu)

    camadas = np.arange(1, 7)
    fig, ax = plt.subplots(figsize=(6.8, 4.6))
    ax.plot(camadas, naive, "-o", color=COR_B, ms=4, label="naive std=1 (linear)")
    ax.plot(camadas, xavier, "-o", color=COR_A, ms=4, label="Xavier (linear)")
    ax.plot(camadas, he, "-o", color=COR_C, ms=4, label="He (ReLU)")
    ax.set_yscale("log")
    ax.set_xlabel("camada")
    ax.set_ylabel("desvio-padrão das ativações (log)")
    ax.set_title("Inicialização e a variância do sinal")
    ax.legend(fontsize=9)
    return _salvar(fig, SLUG_025, "variancia-init")


# ===========================================================================
# Lição 026 — Normalização (eixos de batch norm e layer norm)
# ===========================================================================
SLUG_026 = "026-batch-layer-norm"


def fig_026_eixos_normalizacao():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.4))
    n_linhas, n_cols = 4, 5
    for ax, titulo, modo in [(ax1, "Batch Norm (por coluna)", "col"),
                             (ax2, "Layer Norm (por linha)", "lin")]:
        ax.set_xlim(-0.5, n_cols - 0.5)
        ax.set_ylim(-0.5, n_linhas - 0.5)
        ax.set_aspect("equal")
        ax.set_xticks(range(n_cols))
        ax.set_yticks(range(n_linhas))
        ax.set_xlabel("features")
        ax.set_ylabel("exemplos (batch)")
        ax.grid(False)
        for i in range(n_linhas):
            for j in range(n_cols):
                if modo == "col":
                    cor = COR_A if j == 1 else "#eef2f7"
                else:
                    cor = COR_B if i == 2 else "#eef2f7"
                ax.add_patch(plt.Rectangle((j - 0.45, i - 0.45), 0.9, 0.9,
                             facecolor=cor, edgecolor="#888", lw=0.8))
        ax.set_title(titulo, fontsize=11)
    ax1.invert_yaxis()
    ax2.invert_yaxis()
    fig.suptitle("Sobre qual eixo cada normalização calcula μ e σ", fontsize=11)
    return _salvar(fig, SLUG_026, "eixos-normalizacao")


# ===========================================================================
# Lição 027 — Vanishing e exploding gradients
# ===========================================================================
SLUG_027 = "027-vanishing-exploding-gradients"


def fig_027_vanishing_exploding():
    L = np.arange(0, 51)
    fig, ax = plt.subplots(figsize=(6.8, 4.6))
    ax.plot(L, 0.8 ** L, "-o", color=COR_A, ms=3, label="r=0.8 (vanishing)")
    ax.plot(L, 1.0 ** L, "-o", color=COR_C, ms=3, label="r=1.0 (estável)")
    ax.plot(L, 1.1 ** L, "-o", color=COR_B, ms=3, label="r=1.1 (exploding)")
    ax.set_yscale("log")
    ax.axhline(1.0, color="#888", lw=0.8, ls="--")
    ax.set_xlabel("profundidade (nº de camadas)")
    ax.set_ylabel("magnitude do gradiente (log)")
    ax.set_title("Gradiente como produto de fatores")
    ax.legend(fontsize=9)
    return _salvar(fig, SLUG_027, "vanishing-exploding")


# ===========================================================================
# Lição 028 — Otimizadores (trajetórias numa ravina mal condicionada)
# ===========================================================================
SLUG_028 = "028-otimizadores"


def fig_028_trajetorias_otimizadores():
    def grad(w):
        return np.array([w[0], 20.0 * w[1]])

    def trajetoria(passo_fn, passos=40):
        w = np.array([5.0, 1.0])
        estado = {}
        pts = [w.copy()]
        for t in range(1, passos + 1):
            w = passo_fn(w, grad(w), t, estado)
            pts.append(w.copy())
        return np.array(pts)

    def gd(w, g, t, st):
        return w - 0.05 * g

    def momentum(w, g, t, st):
        st["v"] = 0.9 * st.get("v", np.zeros(2)) + g
        return w - 0.05 * st["v"]

    def adam(w, g, t, st):
        st["m"] = 0.9 * st.get("m", np.zeros(2)) + 0.1 * g
        st["v2"] = 0.999 * st.get("v2", np.zeros(2)) + 0.001 * g * g
        mh = st["m"] / (1 - 0.9 ** t)
        vh = st["v2"] / (1 - 0.999 ** t)
        return w - 0.2 * mh / (np.sqrt(vh) + 1e-8)

    g_ = np.linspace(-5.5, 5.5, 200)
    h_ = np.linspace(-1.2, 1.2, 200)
    GX, GY = np.meshgrid(g_, h_)
    Z = 0.5 * (GX ** 2 + 20.0 * GY ** 2)
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.contour(GX, GY, Z, levels=[1, 4, 10, 25, 50], colors=CINZA)
    for fn, cor, rot in [(gd, COR_A, "GD"), (momentum, COR_C, "Momentum"),
                         (adam, COR_B, "Adam")]:
        pts = trajetoria(fn)
        ax.plot(pts[:, 0], pts[:, 1], "-o", color=cor, ms=2.5, lw=1.2, label=rot)
    ax.plot([0], [0], "*", color="#222", ms=14, label="mínimo")
    ax.set_xlabel(r"$w_0$")
    ax.set_ylabel(r"$w_1$")
    ax.set_title("Trajetórias numa ravina mal condicionada")
    ax.legend(fontsize=8, loc="upper right")
    return _salvar(fig, SLUG_028, "trajetorias-otimizadores")


# ===========================================================================
# Lição 029 — CNN (convolução e pooling)
# ===========================================================================
SLUG_029 = "029-cnn"


def fig_029_convolucao_pooling():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.0, 4.4))

    # --- convolucao: imagem com kernel destacado ---
    img = np.array([[1, 1, 1, 0, 0],
                    [1, 1, 1, 0, 0],
                    [1, 1, 1, 0, 0],
                    [1, 1, 1, 0, 0],
                    [1, 1, 1, 0, 0]], dtype=float)
    ax1.imshow(img, cmap="Blues", vmin=-1, vmax=1)
    # destaca a janela 3x3 do kernel no canto superior esquerdo
    ax1.add_patch(plt.Rectangle((-0.5, -0.5), 3, 3, fill=False,
                  edgecolor=COR_B, lw=2.5))
    ax1.set_title("Convolução: kernel 3×3 desliza pela imagem")
    ax1.set_xticks(range(5))
    ax1.set_yticks(range(5))
    ax1.grid(False)

    # --- pooling: matriz 4x4 e blocos 2x2 ---
    x = np.array([[1, 3, 2, 4],
                  [5, 6, 1, 2],
                  [0, 1, 3, 8],
                  [2, 1, 0, 7]], dtype=float)
    ax2.imshow(x, cmap="Oranges")
    for i in range(4):
        for j in range(4):
            ax2.text(j, i, int(x[i, j]), ha="center", va="center", fontsize=10)
    for (bi, bj) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        ax2.add_patch(plt.Rectangle((bj - 0.5, bi - 0.5), 2, 2, fill=False,
                      edgecolor=COR_A, lw=2.0))
    ax2.set_title("Max pooling 2×2: maior valor por bloco")
    ax2.set_xticks(range(4))
    ax2.set_yticks(range(4))
    ax2.grid(False)
    return _salvar(fig, SLUG_029, "convolucao-pooling")


# ===========================================================================
# Lição 030 — RNN desenrolada no tempo
# ===========================================================================
SLUG_030 = "030-rnn-lstm-gru"


def fig_030_rnn_desenrolada():
    fig, ax = plt.subplots(figsize=(8.4, 3.8))
    ax.axis("off")
    passos = 4
    for t in range(passos):
        x = t * 2.0
        # celula
        ax.add_patch(plt.Rectangle((x - 0.4, 0.6), 0.8, 0.8, facecolor="#eef2f7",
                     edgecolor=COR_A, lw=1.8, zorder=3))
        ax.text(x, 1.0, "RNN", ha="center", va="center", fontsize=10, zorder=4)
        # entrada
        ax.annotate("", xy=(x, 0.6), xytext=(x, 0.0),
                    arrowprops=dict(arrowstyle="-|>", color="#444", lw=1.3))
        ax.text(x, -0.2, fr"$x_{t}$", ha="center", fontsize=11)
        # saida/estado para cima
        ax.annotate("", xy=(x, 2.0), xytext=(x, 1.4),
                    arrowprops=dict(arrowstyle="-|>", color="#444", lw=1.3))
        ax.text(x, 2.15, fr"$h_{t}$", ha="center", fontsize=11)
        # conexao recorrente horizontal
        if t < passos - 1:
            ax.annotate("", xy=(x + 2 - 0.4, 1.0), xytext=(x + 0.4, 1.0),
                        arrowprops=dict(arrowstyle="-|>", color=COR_B, lw=1.6))
    ax.set_xlim(-0.8, (passos - 1) * 2 + 0.8)
    ax.set_ylim(-0.5, 2.5)
    ax.set_title("RNN desenrolada no tempo: o estado oculto flui adiante")
    return _salvar(fig, SLUG_030, "rnn-desenrolada")


# ===========================================================================
# Lição 031 — Bloco residual (skip connection)
# ===========================================================================
SLUG_031 = "031-arquiteturas-profundas-transfer-learning"


def fig_031_bloco_residual():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    ax.axis("off")

    def caixa(x, y, w, h, texto, cor):
        ax.add_patch(plt.Rectangle((x, y), w, h, facecolor="#eef2f7",
                     edgecolor=cor, lw=1.8, zorder=3))
        ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center", fontsize=10)

    # caminho principal: x -> peso -> relu -> peso -> (+) -> saida
    caixa(1.2, 2.4, 1.4, 0.7, "peso + ReLU", COR_A)
    caixa(3.2, 2.4, 1.4, 0.7, "peso", COR_A)
    # soma
    ax.add_patch(plt.Circle((5.4, 2.75), 0.25, facecolor="#fff",
                 edgecolor=COR_B, lw=1.8, zorder=4))
    ax.text(5.4, 2.75, "+", ha="center", va="center", fontsize=14, zorder=5)

    # setas do caminho principal
    ax.annotate("", xy=(1.2, 2.75), xytext=(0.3, 2.75),
                arrowprops=dict(arrowstyle="-|>", color="#444", lw=1.4))
    ax.text(0.1, 2.75, "x", ha="center", va="center", fontsize=12)
    ax.annotate("", xy=(3.2, 2.75), xytext=(2.6, 2.75),
                arrowprops=dict(arrowstyle="-|>", color="#444", lw=1.4))
    ax.annotate("", xy=(5.15, 2.75), xytext=(4.6, 2.75),
                arrowprops=dict(arrowstyle="-|>", color="#444", lw=1.4))
    ax.annotate("", xy=(6.6, 2.75), xytext=(5.65, 2.75),
                arrowprops=dict(arrowstyle="-|>", color="#444", lw=1.4))
    ax.text(6.95, 2.75, "y", ha="center", va="center", fontsize=12)

    # atalho (skip): x desce, vai para a soma
    ax.annotate("", xy=(0.3, 1.2), xytext=(0.3, 2.5),
                arrowprops=dict(arrowstyle="-", color=COR_B, lw=1.8))
    ax.annotate("", xy=(5.4, 1.2), xytext=(0.3, 1.2),
                arrowprops=dict(arrowstyle="-", color=COR_B, lw=1.8))
    ax.annotate("", xy=(5.4, 2.5), xytext=(5.4, 1.2),
                arrowprops=dict(arrowstyle="-|>", color=COR_B, lw=1.8))
    ax.text(2.8, 1.0, "atalho (identidade): y = x + F(x)", ha="center",
            fontsize=9, color=COR_B)

    ax.set_xlim(-0.2, 7.3)
    ax.set_ylim(0.5, 3.6)
    ax.set_title("Bloco residual: caminho principal F(x) + atalho")
    return _salvar(fig, SLUG_031, "bloco-residual")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_022_separabilidade_linear,
    fig_023_ativacoes,
    fig_024_mlp_arquitetura,
    fig_025_variancia_init,
    fig_026_eixos_normalizacao,
    fig_027_vanishing_exploding,
    fig_028_trajetorias_otimizadores,
    fig_029_convolucao_pooling,
    fig_030_rnn_desenrolada,
    fig_031_bloco_residual,
]


def main() -> int:
    gerados = []
    for gerar in TODAS_AS_FIGURAS:
        caminho = gerar()
        rel = caminho.relative_to(RAIZ_TRILHA)
        gerados.append(rel)
        print(f"[ok] {rel}")
    print(f"\n{len(gerados)} figura(s) gerada(s) em {ASSETS.relative_to(RAIZ_TRILHA)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
