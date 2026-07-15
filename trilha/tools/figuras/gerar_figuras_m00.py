#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M00.

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Semente fixa de RNG onde há aleatoriedade (nuvens de pontos, amostragem).

Uso:
    python trilha/tools/figuras/gerar_figuras_m00.py

As imagens são salvas em:
    trilha/modulos/M00-fundamentos-matematicos/assets/<NNN>-<slug>/<nome>.png
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
ASSETS = RAIZ_TRILHA / "modulos" / "M00-fundamentos-matematicos" / "assets"

COR_A = "#1f5fa8"
COR_B = "#c1432a"
COR_C = "#2e8b57"


def _salvar(fig, slug: str, nome: str) -> Path:
    """Salva a figura em assets/<slug>/<nome>.png e fecha a figura."""
    destino = ASSETS / slug / f"{nome}.png"
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, bbox_inches="tight")
    plt.close(fig)
    return destino


def _seta(ax, origem, vetor, cor, rotulo=None, lw=2.2):
    ax.annotate("", xy=(origem[0] + vetor[0], origem[1] + vetor[1]),
                xytext=(origem[0], origem[1]),
                arrowprops=dict(arrowstyle="-|>", color=cor, lw=lw))
    if rotulo:
        ax.text(origem[0] + vetor[0] * 1.05, origem[1] + vetor[1] * 1.05,
                rotulo, color=cor, fontsize=12, fontweight="bold")


# ===========================================================================
# Lição 001 — Vetores e espaços vetoriais
# ===========================================================================
SLUG_001 = "001-vetores-e-espacos-vetoriais"


def fig_001_soma_vetores():
    u = np.array([3.0, 1.0])
    v = np.array([1.0, 2.0])
    s = u + v
    fig, ax = plt.subplots(figsize=(5.2, 5.0))
    _seta(ax, (0, 0), u, COR_A, r"$\mathbf{u}$")
    _seta(ax, (0, 0), v, COR_B, r"$\mathbf{v}$")
    _seta(ax, (0, 0), s, COR_C, r"$\mathbf{u}+\mathbf{v}$")
    # regra do paralelogramo (linhas tracejadas)
    ax.plot([u[0], s[0]], [u[1], s[1]], "--", color=COR_B, alpha=0.6)
    ax.plot([v[0], s[0]], [v[1], s[1]], "--", color=COR_A, alpha=0.6)
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4)
    ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_title("Soma de vetores (regra do paralelogramo)")
    return _salvar(fig, SLUG_001, "soma-vetores")


def fig_001_span():
    u = np.array([2.0, 1.0])
    v = np.array([1.0, 2.0])
    fig, ax = plt.subplots(figsize=(5.2, 5.0))
    # nuvem de combinações lineares a*u + b*v cobrindo o plano
    coefs = np.linspace(-1.5, 1.5, 13)
    for a in coefs:
        for b in coefs:
            p = a * u + b * v
            ax.plot(p[0], p[1], ".", color="#9aa7b5", markersize=3)
    _seta(ax, (0, 0), u, COR_A, r"$\mathbf{u}$")
    _seta(ax, (0, 0), v, COR_B, r"$\mathbf{v}$")
    ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_title(r"Span de $\{\mathbf{u},\mathbf{v}\}$: todo o plano $\mathbb{R}^2$")
    return _salvar(fig, SLUG_001, "span-r2")


# ===========================================================================
# Lição 002 — Matrizes e operações
# ===========================================================================
SLUG_002 = "002-matrizes-e-operacoes"


def fig_002_matriz_vetor_colunas():
    A = np.array([[1.0, 2.0], [3.0, 4.0]])
    x = np.array([1.0, 2.0])
    c1, c2 = A[:, 0], A[:, 1]
    r = A @ x
    fig, ax = plt.subplots(figsize=(5.4, 5.0))
    _seta(ax, (0, 0), c1, COR_A, r"col$_1$")
    _seta(ax, (0, 0), x[1] * c2, COR_B, r"$2\cdot$col$_2$", lw=1.8)
    # col1 + 2*col2 = resultado, mostrando a soma encadeada
    ax.plot([c1[0], r[0]], [c1[1], r[1]], "--", color=COR_B, alpha=0.6)
    _seta(ax, (0, 0), r, COR_C, r"$A\mathbf{x}$")
    ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-0.5, 12)
    ax.set_title(r"$A\mathbf{x}=x_1\cdot$col$_1+x_2\cdot$col$_2$")
    return _salvar(fig, SLUG_002, "matriz-vetor-colunas")


# ===========================================================================
# Lição 003 — Transformações lineares
# ===========================================================================
SLUG_003 = "003-transformacoes-lineares-multiplicacao-matriz-vetor"


def _quadrado_unitario():
    return np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]], dtype=float)


def fig_003_cisalhamento():
    sq = _quadrado_unitario()
    S = np.array([[1.0, 1.0], [0.0, 1.0]])  # cisalhamento horizontal
    t = S @ sq
    fig, ax = plt.subplots(figsize=(6.0, 4.6))
    ax.plot(sq[0], sq[1], "-o", color=COR_A, label="original (quadrado unitário)")
    ax.fill(sq[0], sq[1], color=COR_A, alpha=0.12)
    ax.plot(t[0], t[1], "-o", color=COR_B, label="após cisalhamento $S$")
    ax.fill(t[0], t[1], color=COR_B, alpha=0.12)
    ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 1.8)
    ax.legend(loc="upper right", fontsize=9)
    ax.set_title("Cisalhamento horizontal  S = [[1, 1], [0, 1]]")
    return _salvar(fig, SLUG_003, "cisalhamento")


def fig_003_rotacao():
    sq = _quadrado_unitario() - np.array([[0.5], [0.5]])  # centra no zero
    ang = np.deg2rad(45.0)
    R = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
    t = R @ sq
    fig, ax = plt.subplots(figsize=(5.2, 5.0))
    ax.plot(sq[0], sq[1], "-o", color=COR_A, label="original")
    ax.fill(sq[0], sq[1], color=COR_A, alpha=0.12)
    ax.plot(t[0], t[1], "-o", color=COR_B, label=r"rotação $45^\circ$")
    ax.fill(t[0], t[1], color=COR_B, alpha=0.12)
    ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.legend(loc="upper right", fontsize=9)
    ax.set_title("Rotação preserva comprimentos e ângulos")
    return _salvar(fig, SLUG_003, "rotacao")


# ===========================================================================
# Lição 004 — Autovalores, SVD, PCA
# ===========================================================================
SLUG_004 = "004-autovalores-autovetores-svd-pca"


def fig_004_pca_nuvem():
    rng = np.random.default_rng(42)
    n = 200
    base = rng.normal(size=(n, 2)) * np.array([2.6, 0.7])
    ang = np.deg2rad(30.0)
    R = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
    X = base @ R.T
    Xc = X - X.mean(axis=0)
    cov = (Xc.T @ Xc) / (n - 1)
    valores, vetores = np.linalg.eigh(cov)
    ordem = np.argsort(valores)[::-1]
    valores, vetores = valores[ordem], vetores[:, ordem]
    fig, ax = plt.subplots(figsize=(5.6, 5.2))
    ax.scatter(Xc[:, 0], Xc[:, 1], s=10, color="#9aa7b5", alpha=0.7)
    for i, cor, nome in [(0, COR_B, "PC1"), (1, COR_C, "PC2")]:
        comp = vetores[:, i] * np.sqrt(valores[i]) * 2.2
        _seta(ax, (0, 0), comp, cor, nome)
    ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_title("PCA: componentes principais de uma nuvem de pontos")
    return _salvar(fig, SLUG_004, "pca-nuvem")


# ===========================================================================
# Lição 005 — Normas, produto interno e distâncias
# ===========================================================================
SLUG_005 = "005-normas-produto-interno-distancias"


def fig_005_angulo_projecao():
    u = np.array([3.0, 1.0])
    v = np.array([1.0, 2.0])
    proj = (np.dot(u, v) / np.dot(u, u)) * u  # projeção de v sobre u
    fig, ax = plt.subplots(figsize=(5.4, 5.0))
    _seta(ax, (0, 0), u, COR_A, r"$\mathbf{u}$")
    _seta(ax, (0, 0), v, COR_B, r"$\mathbf{v}$")
    _seta(ax, (0, 0), proj, COR_C, r"proj$_\mathbf{u}\,\mathbf{v}$")
    ax.plot([v[0], proj[0]], [v[1], proj[1]], "--", color="#7a7a7a")
    # arco do ângulo
    ang_u = np.arctan2(u[1], u[0])
    ang_v = np.arctan2(v[1], v[0])
    ts = np.linspace(ang_u, ang_v, 40)
    ax.plot(0.8 * np.cos(ts), 0.8 * np.sin(ts), color="#444", lw=1.2)
    ax.text(0.95, 0.7, r"$\theta$", fontsize=13)
    ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-0.5, 2.6)
    ax.set_title(r"Ângulo entre vetores e projeção de $\mathbf{v}$ sobre $\mathbf{u}$")
    return _salvar(fig, SLUG_005, "angulo-projecao")


def fig_005_bolas_normas():
    fig, ax = plt.subplots(figsize=(5.2, 5.0))
    # L2: círculo unitário
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(t), np.sin(t), color=COR_A, label=r"$\|\cdot\|_2=1$")
    # L1: losango
    ax.plot([1, 0, -1, 0, 1], [0, 1, 0, -1, 0], color=COR_B,
            label=r"$\|\cdot\|_1=1$")
    # Linf: quadrado
    ax.plot([1, 1, -1, -1, 1], [1, -1, -1, 1, 1], color=COR_C,
            label=r"$\|\cdot\|_\infty=1$")
    ax.set_aspect("equal")
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.legend(loc="upper right", fontsize=9)
    ax.set_title("Bolas unitárias das normas L1, L2 e L∞")
    return _salvar(fig, SLUG_005, "bolas-normas")


# ===========================================================================
# Lição 006 — Funções, limites e derivadas
# ===========================================================================
SLUG_006 = "006-funcoes-limites-derivadas"


def fig_006_tangente():
    x = np.linspace(-1, 5, 400)
    f = x ** 2
    x0 = 2.0
    tang = 2 * x0 * (x - x0) + x0 ** 2  # reta tangente em x0
    fig, ax = plt.subplots(figsize=(6.0, 4.6))
    ax.plot(x, f, color=COR_A, label=r"$f(x)=x^2$")
    ax.plot(x, tang, "--", color=COR_B,
            label=r"tangente em $x_0=2$ (inclinação $f'=4$)")
    ax.plot([x0], [x0 ** 2], "o", color=COR_B)
    ax.set_ylim(-2, 20)
    ax.legend(loc="upper center", fontsize=9)
    ax.set_title("Derivada = inclinação da reta tangente")
    return _salvar(fig, SLUG_006, "tangente")


# ===========================================================================
# Lição 007 — Derivadas parciais, gradiente, regra da cadeia
# ===========================================================================
SLUG_007 = "007-derivadas-parciais-gradiente-regra-da-cadeia"


def fig_007_gradiente_campo():
    g = np.linspace(-3, 3, 200)
    X, Y = np.meshgrid(g, g)
    Z = X ** 2 + Y ** 2
    fig, ax = plt.subplots(figsize=(5.6, 5.2))
    cont = ax.contour(X, Y, Z, levels=[1, 4, 9, 16], colors="#9aa7b5")
    ax.clabel(cont, inline=True, fontsize=8)
    # campo de gradiente ∇f = (2x, 2y) em pontos esparsos
    gx = np.linspace(-2.5, 2.5, 9)
    GX, GY = np.meshgrid(gx, gx)
    ax.quiver(GX, GY, 2 * GX, 2 * GY, color=COR_B, alpha=0.8,
              angles="xy", scale_units="xy", scale=8)
    ax.set_aspect("equal")
    ax.set_title(r"Gradiente $\nabla f=(2x,2y)$ de $f=x^2+y^2$")
    return _salvar(fig, SLUG_007, "gradiente-campo")


# ===========================================================================
# Lição 008 — Probabilidade e distribuições
# ===========================================================================
SLUG_008 = "008-probabilidade-e-distribuicoes"


def fig_008_distribuicoes():
    from math import comb
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 4.0))
    # Binomial(n=10, p=0.5) — discreta
    n, p = 10, 0.5
    ks = np.arange(n + 1)
    pmf = np.array([comb(n, int(k)) * p ** k * (1 - p) ** (n - k) for k in ks])
    ax1.bar(ks, pmf, color=COR_A, alpha=0.85)
    ax1.set_title("Binomial(n=10, p=0.5) — PMF discreta")
    ax1.set_xlabel("k (sucessos)")
    ax1.set_ylabel("P(X=k)")
    # Normal padrão — contínua
    x = np.linspace(-4, 4, 400)
    pdf = np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi)
    ax2.plot(x, pdf, color=COR_B)
    ax2.fill_between(x, pdf, where=(np.abs(x) <= 1), color=COR_B, alpha=0.2)
    ax2.set_title("Normal padrão — densidade contínua")
    ax2.set_xlabel("x")
    ax2.set_ylabel("f(x)")
    return _salvar(fig, SLUG_008, "distribuicoes")


# ===========================================================================
# Lição 009 — Estatística descritiva e inferência
# ===========================================================================
SLUG_009 = "009-estatistica-descritiva-e-inferencia"


def fig_009_tlc():
    rng = np.random.default_rng(7)
    # População fortemente assimétrica (exponencial); médias de amostras n=30.
    medias = np.array([rng.exponential(scale=1.0, size=30).mean()
                       for _ in range(5000)])
    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    ax.hist(medias, bins=40, density=True, color=COR_A, alpha=0.75,
            label="médias amostrais ($n=30$)")
    # normal teórica do TLC: média 1, desvio = 1/sqrt(30)
    mu, sigma = 1.0, 1.0 / np.sqrt(30)
    x = np.linspace(medias.min(), medias.max(), 300)
    pdf = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    ax.plot(x, pdf, color=COR_B, lw=2, label="normal do TLC")
    ax.legend(fontsize=9)
    ax.set_title("Teorema do Limite Central: médias amostrais ≈ normais")
    return _salvar(fig, SLUG_009, "tlc")


# ===========================================================================
# Lição 010 — Verossimilhança, entropia, KL
# ===========================================================================
SLUG_010 = "010-verossimilhanca-entropia-kl"


def fig_010_entropia_binaria():
    p = np.linspace(1e-6, 1 - 1e-6, 400)
    H = -(p * np.log2(p) + (1 - p) * np.log2(1 - p))
    fig, ax = plt.subplots(figsize=(6.0, 4.4))
    ax.plot(p, H, color=COR_A)
    ax.plot([0.5], [1.0], "o", color=COR_B)
    ax.annotate("máx = 1 bit em p=0.5", xy=(0.5, 1.0), xytext=(0.55, 0.6),
                arrowprops=dict(arrowstyle="-|>", color=COR_B))
    ax.set_xlabel("p")
    ax.set_ylabel("H(p) [bits]")
    ax.set_title(r"Entropia binária $H(p)=-p\log_2 p-(1-p)\log_2(1-p)$")
    return _salvar(fig, SLUG_010, "entropia-binaria")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_001_soma_vetores,
    fig_001_span,
    fig_002_matriz_vetor_colunas,
    fig_003_cisalhamento,
    fig_003_rotacao,
    fig_004_pca_nuvem,
    fig_005_angulo_projecao,
    fig_005_bolas_normas,
    fig_006_tangente,
    fig_007_gradiente_campo,
    fig_008_distribuicoes,
    fig_009_tlc,
    fig_010_entropia_binaria,
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
