#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M05.

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Semente fixa de RNG onde há aleatoriedade.

Uso:
    python trilha/tools/figuras/gerar_figuras_m05.py

As imagens são salvas em:
    trilha/modulos/M05-llms-pipeline-de-treino/assets/<NNN>-<slug>/<nome>.png
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
ASSETS = RAIZ_TRILHA / "modulos" / "M05-llms-pipeline-de-treino" / "assets"

COR_A = "#1f5fa8"
COR_B = "#c1432a"
COR_C = "#2e8b57"
COR_D = "#8e6abf"
COR_E = "#d9920a"
CINZA = "#9aa7b5"


def _salvar(fig, slug: str, nome: str) -> Path:
    """Salva a figura em assets/<slug>/<nome>.png e fecha a figura."""
    destino = ASSETS / slug / f"{nome}.png"
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, bbox_inches="tight")
    plt.close(fig)
    return destino


def _caixa(ax, x, y, w, h, texto, cor, fontsize=10):
    """Desenha uma caixa rotulada centrada em (x, y)."""
    ax.add_patch(plt.Rectangle((x - w / 2, y - h / 2), w, h,
                               facecolor=cor, alpha=0.18,
                               edgecolor=cor, lw=1.8, zorder=2))
    ax.text(x, y, texto, ha="center", va="center", fontsize=fontsize,
            color="#222", zorder=3)


def _seta(ax, x0, y0, x1, y1, cor="#444"):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=cor, lw=2.0), zorder=1)


# ===========================================================================
# Lição 044 — O que são LLMs: modelagem de linguagem e leis de escala
# ===========================================================================
SLUG_044 = "044-llms-modelagem-linguagem-escala"


def fig_044_leis_de_escala():
    """Leis de escala: a perda de teste cai como uma lei de potência no número
    de parâmetros (reta em escala log-log), saturando num piso irredutível."""
    N = np.logspace(6, 11, 200)           # nº de parâmetros (1e6 .. 1e11)
    E = 1.6                               # piso irredutível (entropia dos dados)
    A = 2.1e3
    alpha = 0.34
    perda = E + A * N ** (-alpha)         # forma típica de Kaplan/Chinchilla

    fig, ax = plt.subplots(figsize=(7.0, 4.8))
    ax.loglog(N, perda - E, color=COR_A, lw=2.4,
              label=r"parte redutível $A\,N^{-\alpha}$")
    ax.loglog(N, perda, color=COR_B, lw=2.0, ls="--",
              label=r"perda total $E + A\,N^{-\alpha}$")
    ax.axhline(E, color=CINZA, lw=1.4, ls=":", label=r"piso irredutível $E$")
    ax.set_xlabel("número de parâmetros  $N$  (escala log)")
    ax.set_ylabel("perda de teste  (escala log)")
    ax.set_title("Leis de escala: perda cai como lei de potência em $N$")
    ax.legend(fontsize=9, loc="lower left")
    return _salvar(fig, SLUG_044, "leis-de-escala")


# ===========================================================================
# Lição 045 — Pré-treinamento (objetivo, dados, custo)
# ===========================================================================
SLUG_045 = "045-pre-treinamento"


def fig_045_curva_pretreino():
    """Curva de pré-treino: a perda de validação (cross-entropy) cai com o
    número de tokens vistos; a regra empírica C ≈ 6·N·D liga compute a custo."""
    tokens = np.logspace(8, 12, 200)      # tokens vistos (1e8 .. 1e12)
    perda = 1.8 + 9.0 * tokens ** (-0.095)

    fig, ax = plt.subplots(figsize=(7.0, 4.8))
    ax.semilogx(tokens, perda, color=COR_C, lw=2.4)
    # anota a regra de custo de compute
    ax.text(0.97, 0.92,
            r"compute  $C \approx 6\,N\,D$" "\n" r"($N$ params, $D$ tokens)",
            transform=ax.transAxes, ha="right", va="top", fontsize=10,
            bbox=dict(boxstyle="round", fc="white", ec=CINZA))
    ax.set_xlabel("tokens de treino vistos  $D$  (escala log)")
    ax.set_ylabel("perda de validação (cross-entropy / nat)")
    ax.set_title("Pré-treinamento: a perda decresce com os tokens vistos")
    return _salvar(fig, SLUG_045, "curva-pretreino")


# ===========================================================================
# Lição 046 — Instruction tuning / SFT
# ===========================================================================
SLUG_046 = "046-instruction-tuning-sft"


def fig_046_mascara_de_perda():
    """No SFT, a perda é mascarada: tokens do prompt não contam, só os da
    resposta-alvo contribuem para o gradiente."""
    tokens = ["<usuário>", "Traduza", "'cat'", "<assistente>", "gato", "</s>"]
    mascara = [0, 0, 0, 0, 1, 1]          # 1 = entra na perda
    fig, ax = plt.subplots(figsize=(8.6, 2.8))
    ax.set_axis_off()
    x = 0.0
    for tok, m in zip(tokens, mascara):
        largura = 0.04 * len(tok) + 0.06
        cor = COR_C if m else CINZA
        ax.add_patch(plt.Rectangle((x, 0.3), largura, 0.5,
                                   facecolor=cor, alpha=0.25 if m else 0.15,
                                   edgecolor=cor, lw=1.6))
        ax.text(x + largura / 2, 0.55, tok, ha="center", va="center", fontsize=10)
        rotulo = "perda" if m else "ignorado"
        ax.text(x + largura / 2, 0.16, rotulo, ha="center", va="center",
                fontsize=8, color=cor)
        x += largura + 0.015
    ax.set_xlim(-0.02, x)
    ax.set_ylim(0, 1.0)
    ax.set_title("SFT: a perda é aplicada apenas aos tokens da resposta-alvo")
    return _salvar(fig, SLUG_046, "mascara-de-perda")


# ===========================================================================
# Lição 047 — Otimização por preferência: RLHF e PPO
# ===========================================================================
SLUG_047 = "047-rlhf-ppo"


def fig_047_pipeline_rlhf():
    """As três etapas clássicas do RLHF: SFT → Reward Model → PPO."""
    fig, ax = plt.subplots(figsize=(9.0, 3.2))
    ax.set_axis_off()
    y = 0.5
    _caixa(ax, 0.13, y, 0.22, 0.42,
           "1. SFT\n(modelo base\ninstruído)", COR_A)
    _caixa(ax, 0.5, y, 0.24, 0.42,
           "2. Reward Model\n(treina em pares\nde preferência)", COR_E)
    _caixa(ax, 0.87, y, 0.22, 0.42,
           "3. PPO\n(otimiza política\ncontra a recompensa)", COR_B)
    _seta(ax, 0.245, y, 0.375, y)
    _seta(ax, 0.625, y, 0.755, y)
    # laço de KL de volta ao SFT
    ax.annotate("", xy=(0.13, 0.74), xytext=(0.87, 0.74),
                arrowprops=dict(arrowstyle="-|>", color=COR_D, lw=1.6,
                                connectionstyle="arc3,rad=-0.25"))
    ax.text(0.5, 0.93, r"penalidade KL mantém a política perto do SFT",
            ha="center", fontsize=9, color=COR_D)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("RLHF: pipeline de três etapas")
    return _salvar(fig, SLUG_047, "pipeline-rlhf")


# ===========================================================================
# Lição 048 — DPO e comparação DPO vs PPO
# ===========================================================================
SLUG_048 = "048-dpo-vs-ppo"


def fig_048_dpo_vs_ppo():
    """Comparação de pipelines: PPO (RLHF) usa reward model + RL online; DPO
    otimiza diretamente sobre os pares de preferência, sem RM nem amostragem."""
    fig, ax = plt.subplots(figsize=(9.4, 4.6))
    ax.set_axis_off()

    # Linha PPO (RLHF clássico)
    yp = 0.74
    ax.text(0.02, yp + 0.16, "PPO (RLHF)", fontsize=11, fontweight="bold",
            color=COR_B)
    _caixa(ax, 0.16, yp, 0.18, 0.26, "pares de\npreferência", CINZA, 9)
    _caixa(ax, 0.40, yp, 0.18, 0.26, "treina\nReward Model", COR_E, 9)
    _caixa(ax, 0.64, yp, 0.18, 0.26, "amostra +\nrecompensa", COR_E, 9)
    _caixa(ax, 0.88, yp, 0.18, 0.26, "política via\nRL (PPO)", COR_B, 9)
    for x0, x1 in [(0.25, 0.31), (0.49, 0.55), (0.73, 0.79)]:
        _seta(ax, x0, yp, x1, yp)

    # Linha DPO
    yd = 0.26
    ax.text(0.02, yd + 0.16, "DPO", fontsize=11, fontweight="bold", color=COR_C)
    _caixa(ax, 0.16, yd, 0.18, 0.26, "pares de\npreferência", CINZA, 9)
    _caixa(ax, 0.52, yd, 0.30, 0.26,
           "perda de classificação direta\n(política + ref. congelada)", COR_C, 9)
    _caixa(ax, 0.88, yd, 0.18, 0.26, "política\notimizada", COR_C, 9)
    _seta(ax, 0.25, yd, 0.37, yd)
    _seta(ax, 0.67, yd, 0.79, yd)

    ax.text(0.5, 0.50, "DPO elimina o reward model e a amostragem online de RL",
            ha="center", fontsize=9.5, style="italic", color="#444")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("DPO vs PPO: pipelines de otimização por preferência")
    return _salvar(fig, SLUG_048, "dpo-vs-ppo")


# ===========================================================================
# Lição 049 — Sampling e decodificação: temperature, top-p, top-k
# ===========================================================================
SLUG_049 = "049-sampling-decodificacao"


def _softmax(logits, T=1.0):
    z = np.asarray(logits, dtype=float) / T
    z = z - z.max()
    e = np.exp(z)
    return e / e.sum()


def fig_049_temperatura_topp():
    """Efeito da temperatura e do top-p sobre a distribuição de probabilidade
    do próximo token."""
    logits = np.array([3.0, 2.0, 1.0, 0.5, 0.0, -1.0])
    rotulos = [f"t{i}" for i in range(len(logits))]
    x = np.arange(len(logits))

    fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.8), sharey=True)

    # (a) temperatura baixa: distribuição mais "afiada"
    p_baixa = _softmax(logits, T=0.5)
    axes[0].bar(x, p_baixa, color=COR_A)
    axes[0].set_title("temperature = 0.5 (afiada)")

    # (b) temperatura alta: distribuição mais "achatada"
    p_alta = _softmax(logits, T=2.0)
    axes[1].bar(x, p_alta, color=COR_B)
    axes[1].set_title("temperature = 2.0 (achatada)")

    # (c) top-p (p=0.9) sobre T=1.0: mantém o núcleo, zera a cauda
    p1 = _softmax(logits, T=1.0)
    ordem = np.argsort(-p1)
    acum = np.cumsum(p1[ordem])
    corte = np.searchsorted(acum, 0.9) + 1
    manter = set(ordem[:corte].tolist())
    cores = [COR_C if i in manter else CINZA for i in range(len(logits))]
    p_top = p1.copy()
    for i in range(len(logits)):
        if i not in manter:
            p_top[i] = 0.0
    p_top = p_top / p_top.sum()
    axes[2].bar(x, p_top, color=cores)
    axes[2].set_title("top-p = 0.9 (núcleo mantido)")

    for ax in axes:
        ax.set_xticks(x)
        ax.set_xticklabels(rotulos, fontsize=8)
        ax.set_xlabel("token candidato")
    axes[0].set_ylabel("probabilidade")
    fig.suptitle("Temperatura reescala os logits; top-p trunca a cauda da distribuição",
                 fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return _salvar(fig, SLUG_049, "temperatura-topp")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_044_leis_de_escala,
    fig_045_curva_pretreino,
    fig_046_mascara_de_perda,
    fig_047_pipeline_rlhf,
    fig_048_dpo_vs_ppo,
    fig_049_temperatura_topp,
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
