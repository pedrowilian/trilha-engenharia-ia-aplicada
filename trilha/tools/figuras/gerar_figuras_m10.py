#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M10.

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Semente fixa de RNG onde há aleatoriedade.

Uso:
    python trilha/tools/figuras/gerar_figuras_m10.py

As imagens são salvas em:
    trilha/modulos/M10-fine-tuning-dados/assets/<NNN>-<slug>/<nome>.png
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
ASSETS = RAIZ_TRILHA / "modulos" / "M10-fine-tuning-dados" / "assets"

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
# Lição 076 — Preparação de datasets para fine-tuning
# ===========================================================================
SLUG_076 = "076-preparacao-datasets-fine-tuning"


def fig_076_pipeline_datasets():
    """Pipeline de preparação de dados para fine-tuning: dos exemplos crus à
    coleção JSONL pronta para treino, passando por limpeza e balanceamento."""
    fig, ax = plt.subplots(figsize=(9.6, 3.2))
    ax.set_axis_off()
    y = 0.5
    _caixa(ax, 0.10, y, 0.18, 0.5,
           "1. Coleta\n(exemplos\ncrus)", CINZA, 9)
    _caixa(ax, 0.34, y, 0.18, 0.5,
           "2. Limpeza\n(dedup, vazios,\nnormalização)", COR_A, 9)
    _caixa(ax, 0.58, y, 0.18, 0.5,
           "3. Balanceamento\n(classes/tópicos\nuniformes)", COR_E, 9)
    _caixa(ax, 0.82, y, 0.18, 0.5,
           "4. Formato JSONL\n(1 exemplo por\nlinha, chat)", COR_C, 9)
    _seta(ax, 0.19, y, 0.25, y)
    _seta(ax, 0.43, y, 0.49, y)
    _seta(ax, 0.67, y, 0.73, y)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Preparação de datasets: pipeline da coleta crua ao JSONL de treino")
    return _salvar(fig, SLUG_076, "pipeline-datasets")


# ===========================================================================
# Lição 077 — Fine-tuning completo: quando e por quê
# ===========================================================================
SLUG_077 = "077-fine-tuning-completo"


def fig_077_rag_vs_fine_tuning():
    """Árvore de decisão simplificada: RAG resolve conhecimento dinâmico/factual;
    fine-tuning resolve comportamento/formato/estilo persistente."""
    fig, ax = plt.subplots(figsize=(9.4, 4.4))
    ax.set_axis_off()
    _caixa(ax, 0.5, 0.86, 0.34, 0.20,
           "O problema é falta de\nCONHECIMENTO ou de\nCOMPORTAMENTO?", CINZA, 9.5)
    # ramo conhecimento -> RAG
    _caixa(ax, 0.22, 0.50, 0.30, 0.18,
           "conhecimento factual,\nmuda com frequência", COR_A, 9)
    _caixa(ax, 0.22, 0.16, 0.26, 0.18, "→ RAG\n(recuperação)", COR_A, 10)
    # ramo comportamento -> fine-tuning
    _caixa(ax, 0.78, 0.50, 0.30, 0.18,
           "formato/estilo/tarefa\nestável e repetida", COR_B, 9)
    _caixa(ax, 0.78, 0.16, 0.26, 0.18, "→ Fine-tuning", COR_B, 10)
    _seta(ax, 0.42, 0.78, 0.28, 0.60)
    _seta(ax, 0.58, 0.78, 0.72, 0.60)
    _seta(ax, 0.22, 0.41, 0.22, 0.26)
    _seta(ax, 0.78, 0.41, 0.78, 0.26)
    ax.text(0.30, 0.69, "conhecimento", fontsize=8.5, color=COR_A, ha="center")
    ax.text(0.70, 0.69, "comportamento", fontsize=8.5, color=COR_B, ha="center")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title("RAG vs fine-tuning: que tipo de lacuna você está resolvendo?")
    return _salvar(fig, SLUG_077, "rag-vs-fine-tuning")


# ===========================================================================
# Lição 078 — LoRA / PEFT
# ===========================================================================
SLUG_078 = "078-lora-peft"


def fig_078_parametros_lora():
    """Comparação do número de parâmetros treináveis: fine-tuning completo
    treina toda a matriz d×k; LoRA treina apenas B (d×r) e A (r×k), com r<<d,k."""
    d, k = 1024, 1024
    rs = [4, 8, 16, 32]
    completo = d * k
    lora = [r * (d + k) for r in rs]

    fig, ax = plt.subplots(figsize=(8.2, 4.6))
    rotulos = ["completo\n(d·k)"] + [f"LoRA r={r}\n(r·(d+k))" for r in rs]
    valores = [completo] + lora
    cores = [COR_B] + [COR_C] * len(rs)
    x = np.arange(len(valores))
    barras = ax.bar(x, valores, color=cores, alpha=0.85)
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(rotulos, fontsize=9)
    ax.set_ylabel("parâmetros treináveis (escala log)")
    ax.set_title(f"LoRA reduz parâmetros treináveis numa camada d=k={d}")
    for b, v in zip(barras, valores):
        pct = 100.0 * v / completo
        ax.text(b.get_x() + b.get_width() / 2, v,
                f"{v:,}\n({pct:.1f}%)", ha="center", va="bottom", fontsize=8)
    ax.set_ylim(top=completo * 3)
    return _salvar(fig, SLUG_078, "parametros-lora")


# ===========================================================================
# Lição 079 — Fine-tuning via OpenAI API
# ===========================================================================
SLUG_079 = "079-fine-tuning-openai-api"


# (Lição 079 não usa figura: o conteúdo é operacional/sequencial e melhor
#  servido por blocos de código simulando o cliente. Mantido aqui por
#  completude documental do módulo.)


# ===========================================================================
# Lição 080 — Avaliação do modelo ajustado e modelo de domínio
# ===========================================================================
SLUG_080 = "080-avaliacao-modelo-ajustado"


def fig_080_comparacao_ab():
    """Comparação A/B entre o modelo base e o modelo ajustado em métricas de
    qualidade, mais a curva de validação que revela overfitting após certo ponto."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.4))

    # (a) A/B em três métricas
    metricas = ["acurácia", "formato\nválido", "satisfação"]
    base = [0.72, 0.80, 0.66]
    ajustado = [0.86, 0.98, 0.81]
    x = np.arange(len(metricas))
    largura = 0.38
    ax1.bar(x - largura / 2, base, largura, label="base", color=CINZA)
    ax1.bar(x + largura / 2, ajustado, largura, label="ajustado", color=COR_C)
    ax1.set_xticks(x)
    ax1.set_xticklabels(metricas, fontsize=9)
    ax1.set_ylim(0, 1.05)
    ax1.set_ylabel("score (maior é melhor)")
    ax1.set_title("A/B: base vs ajustado")
    ax1.legend(fontsize=9)

    # (b) curva de treino/validação: overfitting
    epocas = np.arange(1, 13)
    treino = 0.9 * np.exp(-0.35 * epocas) + 0.05
    val = 0.9 * np.exp(-0.35 * epocas) + 0.05 + 0.012 * (epocas - 4) ** 2 * (epocas > 4)
    ax2.plot(epocas, treino, "-o", color=COR_A, lw=2, ms=4, label="perda de treino")
    ax2.plot(epocas, val, "-s", color=COR_B, lw=2, ms=4, label="perda de validação")
    melhor = int(epocas[np.argmin(val)])
    ax2.axvline(melhor, color=CINZA, ls="--", lw=1.4)
    ax2.text(melhor + 0.2, ax2.get_ylim()[1] * 0.8,
             f"melhor época = {melhor}\n(early stopping)", fontsize=8.5, color="#444")
    ax2.set_xlabel("época")
    ax2.set_ylabel("perda")
    ax2.set_title("Overfitting: validação sobe após o ponto ótimo")
    ax2.legend(fontsize=9)

    fig.suptitle("Avaliação do modelo ajustado: ganho A/B e diagnóstico de overfitting",
                 fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return _salvar(fig, SLUG_080, "comparacao-ab")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_076_pipeline_datasets,
    fig_077_rag_vs_fine_tuning,
    fig_078_parametros_lora,
    fig_080_comparacao_ab,
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
