#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M01.

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Semente fixa de RNG onde há aleatoriedade (nuvens de pontos, amostragem).

Uso:
    python trilha/tools/figuras/gerar_figuras_m01.py

As imagens são salvas em:
    trilha/modulos/M01-fundamentos-de-ml/assets/<NNN>-<slug>/<nome>.png
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
ASSETS = RAIZ_TRILHA / "modulos" / "M01-fundamentos-de-ml" / "assets"

COR_A = "#1f5fa8"
COR_B = "#c1432a"
COR_C = "#2e8b57"
CINZA = "#9aa7b5"


def _salvar(fig, slug: str, nome: str) -> Path:
    """Salva a figura em assets/<slug>/<nome>.png e fecha a figura."""
    destino = ASSETS / slug / f"{nome}.png"
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, bbox_inches="tight")
    plt.close(fig)
    return destino


# ===========================================================================
# Lição 011 — O que é ML (supervisionado vs não-supervisionado)
# ===========================================================================
SLUG_011 = "011-o-que-e-ml"


def fig_011_supervisionado_vs_nao():
    rng = np.random.default_rng(0)
    # dois grupos no plano
    g1 = rng.normal([2, 2], 0.6, size=(40, 2))
    g2 = rng.normal([5, 5], 0.6, size=(40, 2))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.4))

    # supervisionado: cores por classe + fronteira linear
    ax1.scatter(g1[:, 0], g1[:, 1], c=COR_A, s=18, label="classe 0")
    ax1.scatter(g2[:, 0], g2[:, 1], c=COR_B, s=18, label="classe 1")
    xs = np.linspace(0, 7, 50)
    ax1.plot(xs, 7 - xs, "--", color="#444", lw=1.5, label="fronteira aprendida")
    ax1.set_title("Supervisionado: rótulos conhecidos")
    ax1.legend(loc="upper right", fontsize=8)
    ax1.set_xlim(0, 7)
    ax1.set_ylim(0, 7)

    # nao-supervisionado: tudo cinza, sem rotulos
    todos = np.vstack([g1, g2])
    ax2.scatter(todos[:, 0], todos[:, 1], c=CINZA, s=18)
    ax2.set_title("Não-supervisionado: sem rótulos")
    ax2.set_xlim(0, 7)
    ax2.set_ylim(0, 7)
    return _salvar(fig, SLUG_011, "supervisionado-vs-nao-supervisionado")


# ===========================================================================
# Lição 012 — Funções de perda (MSE e BCE)
# ===========================================================================
SLUG_012 = "012-funcoes-de-perda"


def fig_012_perdas():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.2))
    # MSE como funcao do erro
    e = np.linspace(-3, 3, 200)
    ax1.plot(e, e ** 2, color=COR_A)
    ax1.set_title(r"MSE: $L = (y-\hat{y})^2$")
    ax1.set_xlabel("erro $y-\\hat{y}$")
    ax1.set_ylabel("perda")
    # BCE para y=1 como funcao de p
    p = np.linspace(1e-3, 1 - 1e-3, 300)
    ax2.plot(p, -np.log(p), color=COR_B)
    ax2.set_title(r"Cross-entropy ($y=1$): $L=-\log p$")
    ax2.set_xlabel("prob. prevista $p$")
    ax2.set_ylabel("perda")
    ax2.set_ylim(0, 7)
    return _salvar(fig, SLUG_012, "perdas")


# ===========================================================================
# Lição 013 — Gradient descent
# ===========================================================================
SLUG_013 = "013-gradient-descent"


def fig_013_superficie_e_passos():
    # perda quadratica 2D L = x^2 + 3y^2, GD a partir de (-3.5, 2.5)
    g = np.linspace(-4, 4, 200)
    X, Y = np.meshgrid(g, g)
    Z = X ** 2 + 3 * Y ** 2
    fig, ax = plt.subplots(figsize=(5.8, 5.2))
    cont = ax.contour(X, Y, Z, levels=[2, 6, 14, 26, 42], colors=CINZA)
    ax.clabel(cont, inline=True, fontsize=8)
    # passos de GD
    eta = 0.12
    p = np.array([-3.5, 2.5])
    pts = [p.copy()]
    for _ in range(12):
        grad = np.array([2 * p[0], 6 * p[1]])
        p = p - eta * grad
        pts.append(p.copy())
    pts = np.array(pts)
    ax.plot(pts[:, 0], pts[:, 1], "-o", color=COR_B, ms=4, lw=1.5,
            label="passos do gradient descent")
    ax.plot([0], [0], "*", color=COR_C, ms=16, label="mínimo")
    ax.set_aspect("equal")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_title(r"Curvas de nível de $L=x^2+3y^2$ e a descida")
    return _salvar(fig, SLUG_013, "superficie-e-passos")


def fig_013_taxa_de_aprendizado():
    def grad(theta):
        return 2.0 * (theta - 3.0)

    def trajetoria(eta, passos=20):
        theta = 0.0
        perdas = []
        for _ in range(passos):
            perdas.append((theta - 3.0) ** 2)
            theta = theta - eta * grad(theta)
        return perdas

    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    for eta, cor, rot in [(0.1, COR_A, "η=0.1 (lento)"),
                          (0.5, COR_C, "η=0.5 (ótimo)"),
                          (1.0, COR_B, "η=1.0 (oscila)")]:
        ax.plot(trajetoria(eta), "-o", color=cor, ms=3, label=rot)
    ax.set_xlabel("passo")
    ax.set_ylabel("perda")
    ax.set_title("Convergência da perda por taxa de aprendizado")
    ax.legend(fontsize=9)
    return _salvar(fig, SLUG_013, "taxa-de-aprendizado")


# ===========================================================================
# Lição 014 — Backpropagation (grafo computacional)
# ===========================================================================
SLUG_014 = "014-backpropagation"


def fig_014_grafo_computacional():
    # grafo de f = (a*b + c)^2 com forward (preto) e backward (vermelho)
    fig, ax = plt.subplots(figsize=(8.2, 4.4))
    ax.axis("off")
    nos = {
        "a": (0.0, 3.0, "a=2"),
        "b": (0.0, 1.5, "b=3"),
        "c": (0.0, 0.0, "c=1"),
        "u": (2.0, 2.25, "u=a·b=6"),
        "v": (4.0, 1.5, "v=u+c=7"),
        "f": (6.0, 1.5, "f=v²=49"),
    }
    for k, (x, y, rot) in nos.items():
        ax.add_patch(plt.Circle((x, y), 0.28, color="#eef2f7", ec=COR_A, lw=1.6, zorder=3))
        ax.text(x, y, k, ha="center", va="center", fontsize=12, fontweight="bold", zorder=4)
        ax.text(x, y - 0.5, rot, ha="center", va="center", fontsize=9, color="#222")

    arestas = [("a", "u"), ("b", "u"), ("u", "v"), ("c", "v"), ("v", "f")]
    grads = {("a", "u"): "∂f/∂a=42", ("b", "u"): "∂f/∂b=28",
             ("u", "v"): "∂f/∂u=14", ("c", "v"): "∂f/∂c=14", ("v", "f"): "∂f/∂v=14"}
    for (o, d) in arestas:
        xo, yo, _ = nos[o]
        xd, yd, _ = nos[d]
        ax.annotate("", xy=(xd - 0.3, yd), xytext=(xo + 0.3, yo),
                    arrowprops=dict(arrowstyle="-|>", color="#444", lw=1.4))
        ax.text((xo + xd) / 2, (yo + yd) / 2 + 0.18, grads[(o, d)],
                color=COR_B, fontsize=8, ha="center")
    ax.set_xlim(-0.6, 6.8)
    ax.set_ylim(-0.8, 3.7)
    ax.set_title("Grafo computacional: forward (valores) e backward (gradientes)")
    return _salvar(fig, SLUG_014, "grafo-computacional")


# ===========================================================================
# Lição 015 — Regularização (efeito L2 e L1)
# ===========================================================================
SLUG_015 = "015-regularizacao"


def fig_015_l1_l2_efeito():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.3))
    # L2: norma dos pesos cai suavemente com lambda
    lambdas = np.linspace(0, 20, 50)
    # pesos de exemplo encolhendo como w0 / (1 + lambda*k)
    w_base = np.array([3.0, -2.0, 1.5])
    normas = [np.linalg.norm(w_base / (1 + 0.15 * lam)) for lam in lambdas]
    ax1.plot(lambdas, normas, color=COR_A)
    ax1.set_title("L2: norma dos pesos encolhe com λ")
    ax1.set_xlabel("λ (força da regularização)")
    ax1.set_ylabel(r"$\|w\|_2$")

    # L1: soft-thresholding zera coeficientes pequenos
    w = np.array([2.0, -0.3, 0.5, -1.5, 0.1])
    def soft(w, t):
        return np.sign(w) * np.maximum(np.abs(w) - t, 0.0)
    idx = np.arange(len(w))
    largura = 0.35
    ax2.bar(idx - largura / 2, w, largura, color=COR_A, label="original")
    ax2.bar(idx + largura / 2, soft(w, 0.5), largura, color=COR_B, label="após L1 (t=0.5)")
    ax2.axhline(0, color="black", lw=0.8)
    ax2.set_title("L1: soft-thresholding gera esparsidade")
    ax2.set_xlabel("índice do peso")
    ax2.set_ylabel("valor")
    ax2.legend(fontsize=8)
    return _salvar(fig, SLUG_015, "l1-l2-efeito")


# ===========================================================================
# Lição 016 — Trade-off viés-variância
# ===========================================================================
SLUG_016 = "016-vies-variancia"


def fig_016_tradeoff():
    c = np.linspace(0.5, 6, 200)         # complexidade
    vies2 = 4.0 / c ** 1.6               # cai com a complexidade
    var = 0.06 * c ** 1.8                # sobe com a complexidade
    total = vies2 + var
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    ax.plot(c, vies2, color=COR_A, label="viés²")
    ax.plot(c, var, color=COR_B, label="variância")
    ax.plot(c, total, color="#222", lw=2.2, label="erro total")
    cmin = c[np.argmin(total)]
    ax.axvline(cmin, color=COR_C, ls="--", lw=1.4)
    ax.text(cmin + 0.1, ax.get_ylim()[1] * 0.7, "complexidade\nótima", color=COR_C, fontsize=9)
    ax.set_xlabel("complexidade do modelo")
    ax.set_ylabel("erro esperado")
    ax.set_title("Trade-off viés-variância")
    ax.legend(fontsize=9)
    return _salvar(fig, SLUG_016, "tradeoff")


# ===========================================================================
# Lição 017 — Overfitting e validação cruzada (curvas treino/val)
# ===========================================================================
SLUG_017 = "017-overfitting-validacao-cruzada"


def fig_017_curvas_treino_val():
    graus = np.arange(1, 12)
    erro_treino = 1.2 / (graus ** 1.3)              # cai sempre
    erro_val = 1.2 / (graus ** 1.3) + 0.015 * (graus - 3) ** 2  # formato de U
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    ax.plot(graus, erro_treino, "-o", color=COR_A, ms=4, label="erro de treino")
    ax.plot(graus, erro_val, "-o", color=COR_B, ms=4, label="erro de validação")
    gmin = graus[np.argmin(erro_val)]
    ax.axvline(gmin, color=COR_C, ls="--", lw=1.4, label="melhor complexidade")
    ax.text(2, ax.get_ylim()[1] * 0.85, "underfitting", color="#555", fontsize=9)
    ax.text(8.5, ax.get_ylim()[1] * 0.85, "overfitting", color="#555", fontsize=9)
    ax.set_xlabel("complexidade (grau do polinômio)")
    ax.set_ylabel("erro")
    ax.set_title("Erro de treino vs. validação")
    ax.legend(fontsize=9)
    return _salvar(fig, SLUG_017, "curvas-treino-val")


# ===========================================================================
# Lição 018 — Calibração (diagrama de confiabilidade)
# ===========================================================================
SLUG_018 = "018-calibracao"


def fig_018_curva_confiabilidade():
    rng = np.random.default_rng(0)
    N = 20000
    p_true = rng.uniform(0, 1, size=N)
    y = (rng.uniform(0, 1, size=N) < p_true).astype(int)
    # modelo superconfiante: logits ampliados
    logit = np.log(p_true / (1 - p_true))
    p_super = 1 / (1 + np.exp(-2.0 * logit))
    bins = np.linspace(0, 1, 11)
    centros, freqs = [], []
    idx = np.clip(np.digitize(p_super, bins) - 1, 0, 9)
    for b in range(10):
        sel = idx == b
        if sel.sum() == 0:
            continue
        centros.append(p_super[sel].mean())
        freqs.append(y[sel].mean())
    fig, ax = plt.subplots(figsize=(5.6, 5.2))
    ax.plot([0, 1], [0, 1], "--", color="#444", label="calibração perfeita")
    ax.plot(centros, freqs, "-o", color=COR_B, label="modelo superconfiante")
    ax.set_xlabel("confiança prevista")
    ax.set_ylabel("frequência observada")
    ax.set_title("Diagrama de confiabilidade")
    ax.legend(fontsize=9)
    ax.set_aspect("equal")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return _salvar(fig, SLUG_018, "curva-confiabilidade")


# ===========================================================================
# Lição 019 — Desbalanceamento (precision-recall vs limiar)
# ===========================================================================
SLUG_019 = "019-desbalanceamento-de-classes"


def fig_019_precision_recall():
    rng = np.random.default_rng(0)
    N = 5000
    y = (rng.uniform(0, 1, size=N) < 0.10).astype(int)
    score = np.where(y == 1, rng.normal(0.65, 0.15, size=N),
                     rng.normal(0.35, 0.15, size=N))
    score = np.clip(score, 0, 1)
    limiares = np.linspace(0.05, 0.95, 40)
    precs, recs = [], []
    for t in limiares:
        pred = (score >= t).astype(int)
        VP = int(((pred == 1) & (y == 1)).sum())
        FP = int(((pred == 1) & (y == 0)).sum())
        FN = int(((pred == 0) & (y == 1)).sum())
        precs.append(VP / (VP + FP) if (VP + FP) else 1.0)
        recs.append(VP / (VP + FN) if (VP + FN) else 0.0)
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    ax.plot(limiares, precs, "-o", color=COR_A, ms=3, label="precision")
    ax.plot(limiares, recs, "-o", color=COR_B, ms=3, label="recall")
    ax.set_xlabel("limiar de decisão")
    ax.set_ylabel("métrica")
    ax.set_title("Trade-off precision-recall (10% positivos)")
    ax.legend(fontsize=9)
    return _salvar(fig, SLUG_019, "precision-recall")


# ===========================================================================
# Lição 020 — Data leakage (score inflado vs honesto)
# ===========================================================================
SLUG_020 = "020-data-leakage"


def fig_020_leakage_cv():
    cenarios = ["com leakage\n(otimista)", "sem leakage\n(honesto)"]
    scores = [0.985, 0.793]
    fig, ax = plt.subplots(figsize=(5.6, 4.4))
    barras = ax.bar(cenarios, scores, color=[COR_B, COR_C], width=0.55)
    for b, s in zip(barras, scores):
        ax.text(b.get_x() + b.get_width() / 2, s + 0.01, f"{s:.3f}",
                ha="center", fontsize=10)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("score de validação")
    ax.set_title("Data leakage infla a métrica offline")
    return _salvar(fig, SLUG_020, "leakage-cv")


# ===========================================================================
# Lição 021 — Testes A/B (distribuições amostrais)
# ===========================================================================
SLUG_021 = "021-experimentacao-testes-ab"


def fig_021_distribuicoes_ab():
    # distribuicoes amostrais da taxa de conversao (normal pelo TLC)
    n = 5000
    pc, pt = 0.10, 0.12
    sc = np.sqrt(pc * (1 - pc) / n)
    st = np.sqrt(pt * (1 - pt) / n)
    x = np.linspace(0.08, 0.14, 400)
    def normal(x, mu, s):
        return np.exp(-(x - mu) ** 2 / (2 * s ** 2)) / (s * np.sqrt(2 * np.pi))
    fig, ax = plt.subplots(figsize=(6.6, 4.4))
    ax.plot(x, normal(x, pc, sc), color=COR_A, label="controle (10%)")
    ax.fill_between(x, normal(x, pc, sc), color=COR_A, alpha=0.15)
    ax.plot(x, normal(x, pt, st), color=COR_B, label="tratamento (12%)")
    ax.fill_between(x, normal(x, pt, st), color=COR_B, alpha=0.15)
    ax.set_xlabel("taxa de conversão observada")
    ax.set_ylabel("densidade")
    ax.set_title("Distribuições amostrais (n=5000 por grupo)")
    ax.legend(fontsize=9)
    return _salvar(fig, SLUG_021, "distribuicoes-ab")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_011_supervisionado_vs_nao,
    fig_012_perdas,
    fig_013_superficie_e_passos,
    fig_013_taxa_de_aprendizado,
    fig_014_grafo_computacional,
    fig_015_l1_l2_efeito,
    fig_016_tradeoff,
    fig_017_curvas_treino_val,
    fig_018_curva_confiabilidade,
    fig_019_precision_recall,
    fig_020_leakage_cv,
    fig_021_distribuicoes_ab,
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
