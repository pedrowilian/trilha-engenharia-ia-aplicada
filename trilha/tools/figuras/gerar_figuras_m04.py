#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M04.

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Semente fixa de RNG onde há aleatoriedade.

Uso:
    python trilha/tools/figuras/gerar_figuras_m04.py

As imagens são salvas em:
    trilha/modulos/M04-transformers/assets/<NNN>-<slug>/<nome>.png
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
ASSETS = RAIZ_TRILHA / "modulos" / "M04-transformers" / "assets"

COR_A = "#1f5fa8"
COR_B = "#c1432a"
COR_C = "#2e8b57"
COR_D = "#8e6abf"
CINZA = "#9aa7b5"


def _salvar(fig, slug: str, nome: str) -> Path:
    """Salva a figura em assets/<slug>/<nome>.png e fecha a figura."""
    destino = ASSETS / slug / f"{nome}.png"
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, bbox_inches="tight")
    plt.close(fig)
    return destino


# ===========================================================================
# Lição 039 — Limitações de RNNs e a motivação para atenção
# ===========================================================================
SLUG_039 = "039-motivacao-atencao"


def fig_039_decaimento_influencia():
    """Mostra o problema da dependência de longo alcance: numa recorrência
    linear h_t = a·h_{t-1} + x_t, a influência de x_0 sobre h_t decai como a^t.
    A atenção, em contraste, conecta qualquer par de posições diretamente."""
    t = np.arange(0, 21)
    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    for a, cor in [(0.5, COR_B), (0.7, COR_D), (0.9, COR_A)]:
        ax.plot(t, a ** t, color=cor, lw=2.2, marker="o", markersize=3,
                label=f"RNN, fator a={a}")
    ax.axhline(1.0, color=COR_C, lw=2.2, ls="--",
               label="atenção (caminho direto)")
    ax.set_xlabel("distância temporal t (passos entre as posições)")
    ax.set_ylabel(r"influência de $x_0$ sobre $h_t$  ($\partial h_t/\partial x_0$)")
    ax.set_title("Dependência de longo alcance: na RNN a influência decai como $a^t$")
    ax.legend(loc="upper right", fontsize=9)
    ax.set_xlim(0, 20)
    ax.set_ylim(-0.02, 1.05)
    return _salvar(fig, SLUG_039, "decaimento-influencia")


# ===========================================================================
# Lição 040 — Self-attention com Query/Key/Value
# ===========================================================================
SLUG_040 = "040-self-attention-qkv"


def _softmax(x, axis=-1):
    x = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(x)
    return e / np.sum(e, axis=axis, keepdims=True)


def fig_040_mapa_atencao():
    """Heatmap da matriz de pesos de atenção (linhas = consultas, colunas =
    chaves). Cada linha soma 1 (distribuição softmax)."""
    rng = np.random.default_rng(40)
    n, d_model, d_k = 6, 8, 4
    X = rng.normal(0, 1, size=(n, d_model))
    Wq = rng.normal(0, 1, size=(d_model, d_k))
    Wk = rng.normal(0, 1, size=(d_model, d_k))
    Q = X @ Wq
    K = X @ Wk
    scores = Q @ K.T / np.sqrt(d_k)
    W = _softmax(scores, axis=-1)

    fig, ax = plt.subplots(figsize=(6.2, 5.4))
    im = ax.imshow(W, cmap="viridis", vmin=0.0, vmax=W.max())
    ax.set_xlabel("chave (posição atendida)")
    ax.set_ylabel("consulta (posição que atende)")
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    for i in range(n):
        for j in range(n):
            ax.text(j, i, f"{W[i, j]:.2f}", ha="center", va="center",
                    color="white" if W[i, j] < 0.5 else "black", fontsize=8)
    ax.grid(False)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="peso de atenção")
    ax.set_title("Matriz de atenção: cada linha é uma softmax (soma 1)")
    return _salvar(fig, SLUG_040, "mapa-atencao")


# ===========================================================================
# Lição 041 — Positional encoding (sinusoidal)
# ===========================================================================
SLUG_041 = "041-positional-encoding"


def _positional_encoding(n_pos, d, base=10000.0):
    pos = np.arange(n_pos)[:, None]
    i = np.arange(d)[None, :]
    angulo = pos / (base ** (2 * (i // 2) / d))
    pe = np.zeros((n_pos, d))
    pe[:, 0::2] = np.sin(angulo[:, 0::2])
    pe[:, 1::2] = np.cos(angulo[:, 1::2])
    return pe


def fig_041_padroes_pe():
    """Heatmap do positional encoding sinusoidal (posições × dimensões).
    Dimensões baixas oscilam rápido; dimensões altas, devagar."""
    n_pos, d = 50, 32
    pe = _positional_encoding(n_pos, d)
    fig, ax = plt.subplots(figsize=(7.6, 5.2))
    im = ax.imshow(pe, aspect="auto", cmap="RdBu", vmin=-1, vmax=1)
    ax.set_xlabel("dimensão do embedding")
    ax.set_ylabel("posição na sequência")
    ax.grid(False)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="valor do encoding")
    ax.set_title("Positional encoding sinusoidal: frequências distintas por dimensão")
    return _salvar(fig, SLUG_041, "padroes-pe")


# ===========================================================================
# Lição 042 — Multi-head attention
# ===========================================================================
SLUG_042 = "042-multi-head-attention"


def fig_042_multiplas_cabecas():
    """Três cabeças de atenção sobre a MESMA sequência produzem matrizes de
    atenção distintas — cada uma especializada num tipo de relação."""
    rng = np.random.default_rng(42)
    n, d_model, d_k = 7, 12, 4
    X = rng.normal(0, 1, size=(n, d_model))
    fig, axes = plt.subplots(1, 3, figsize=(11.4, 4.0))
    for h, ax in enumerate(axes):
        Wq = rng.normal(0, 1, size=(d_model, d_k))
        Wk = rng.normal(0, 1, size=(d_model, d_k))
        scores = (X @ Wq) @ (X @ Wk).T / np.sqrt(d_k)
        W = _softmax(scores, axis=-1)
        im = ax.imshow(W, cmap="viridis", vmin=0, vmax=1)
        ax.set_title(f"cabeça {h + 1}")
        ax.set_xlabel("chave")
        if h == 0:
            ax.set_ylabel("consulta")
        ax.set_xticks(range(n))
        ax.set_yticks(range(n))
        ax.grid(False)
    fig.colorbar(im, ax=axes, fraction=0.025, pad=0.02, label="peso")
    fig.suptitle("Multi-head: cabeças paralelas aprendem padrões de atenção diferentes")
    return _salvar(fig, SLUG_042, "multiplas-cabecas")


# ===========================================================================
# Lição 043 — Arquitetura completa do Transformer
# ===========================================================================
SLUG_043 = "043-arquitetura-transformer"


def _caixa(ax, xy, larg, alt, texto, cor):
    ax.add_patch(plt.Rectangle(xy, larg, alt, facecolor=cor, alpha=0.20,
                               edgecolor=cor, lw=1.8, zorder=3))
    ax.text(xy[0] + larg / 2, xy[1] + alt / 2, texto, ha="center", va="center",
            fontsize=9, zorder=4)


def _seta(ax, p0, p1, cor="#444", estilo="-|>"):
    ax.annotate("", xy=p1, xytext=p0,
                arrowprops=dict(arrowstyle=estilo, color=cor, lw=1.6), zorder=2)


def fig_043_bloco_transformer():
    """Diagrama do bloco Transformer (encoder e decoder) desenhado com caixas e
    setas: sub-camadas de atenção e FFN, cada uma com conexão residual + norm."""
    fig, ax = plt.subplots(figsize=(9.6, 6.6))
    ax.set_axis_off()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 11)

    # --- Encoder (coluna esquerda) ---
    ax.text(2.0, 10.6, "Encoder", ha="center", fontsize=12, fontweight="bold",
            color=COR_A)
    _caixa(ax, (0.6, 0.4), 2.8, 0.7, "Input Embedding + PE", CINZA)
    _caixa(ax, (0.6, 2.0), 2.8, 0.9, "Multi-Head\nSelf-Attention", COR_A)
    _caixa(ax, (0.6, 3.4), 2.8, 0.6, "Add & Norm", COR_C)
    _caixa(ax, (0.6, 4.8), 2.8, 0.9, "Feed-Forward\n(position-wise)", COR_B)
    _caixa(ax, (0.6, 6.2), 2.8, 0.6, "Add & Norm", COR_C)
    _seta(ax, (2.0, 1.1), (2.0, 2.0))
    _seta(ax, (2.0, 2.9), (2.0, 3.4))
    _seta(ax, (2.0, 4.0), (2.0, 4.8))
    _seta(ax, (2.0, 5.7), (2.0, 6.2))
    _seta(ax, (2.0, 6.8), (2.0, 7.6))
    # residuais (setas laterais que contornam cada sub-camada)
    _seta(ax, (0.6, 1.5), (0.2, 1.5), cor=COR_C)
    ax.annotate("", xy=(0.6, 3.7), xytext=(0.2, 1.5),
                arrowprops=dict(arrowstyle="-|>", color=COR_C, lw=1.4,
                                connectionstyle="arc3,rad=-0.3"), zorder=1)
    ax.text(0.05, 2.6, "residual", rotation=90, va="center", fontsize=7,
            color=COR_C)

    # --- Decoder (coluna direita) ---
    ax.text(7.6, 10.6, "Decoder", ha="center", fontsize=12, fontweight="bold",
            color=COR_B)
    _caixa(ax, (6.2, 0.4), 2.8, 0.7, "Output Embedding + PE", CINZA)
    _caixa(ax, (6.2, 1.8), 2.8, 0.9, "Masked Multi-Head\nSelf-Attention", COR_A)
    _caixa(ax, (6.2, 3.1), 2.8, 0.5, "Add & Norm", COR_C)
    _caixa(ax, (6.2, 4.1), 2.8, 0.9, "Cross-Attention\n(Q=dec, K,V=enc)", COR_D)
    _caixa(ax, (6.2, 5.4), 2.8, 0.5, "Add & Norm", COR_C)
    _caixa(ax, (6.2, 6.2), 2.8, 0.9, "Feed-Forward", COR_B)
    _caixa(ax, (6.2, 7.5), 2.8, 0.5, "Add & Norm", COR_C)
    _caixa(ax, (6.2, 8.6), 2.8, 0.7, "Linear + Softmax", CINZA)
    for y0, y1 in [(1.1, 1.8), (2.7, 3.1), (3.6, 4.1), (5.0, 5.4),
                   (5.9, 6.2), (7.1, 7.5), (8.0, 8.6)]:
        _seta(ax, (7.6, y0), (7.6, y1))

    # cross-attention recebe K,V do topo do encoder
    ax.annotate("", xy=(6.2, 4.5), xytext=(3.4, 6.5),
                arrowprops=dict(arrowstyle="-|>", color=COR_D, lw=1.6,
                                connectionstyle="arc3,rad=-0.2"), zorder=2)
    ax.text(4.9, 5.9, "K, V do encoder", ha="center", fontsize=8, color=COR_D)

    ax.set_title("Arquitetura Transformer: blocos de encoder e decoder")
    return _salvar(fig, SLUG_043, "bloco-transformer")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_039_decaimento_influencia,
    fig_040_mapa_atencao,
    fig_041_padroes_pe,
    fig_042_multiplas_cabecas,
    fig_043_bloco_transformer,
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
