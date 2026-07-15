#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M14.

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Semente fixa de RNG onde há aleatoriedade.

Uso:
    python trilha/tools/figuras/gerar_figuras_m14.py

As imagens são salvas em:
    trilha/modulos/M14-ferramentas-aplicadas/assets/<NNN>-<slug>/<nome>.png
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
ASSETS = RAIZ_TRILHA / "modulos" / "M14-ferramentas-aplicadas" / "assets"

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


def _seta(ax, x0, y0, x1, y1, cor="#444", rad=0.0):
    estilo = dict(arrowstyle="-|>", color=cor, lw=2.0)
    if rad:
        estilo["connectionstyle"] = f"arc3,rad={rad}"
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=estilo, zorder=1)


# ===========================================================================
# Lição 095 — IA para DevOps I (AIOps: detecção de anomalias em métricas)
# ===========================================================================
SLUG_095 = "095-ia-devops-i"


def fig_095_deteccao_anomalias():
    """Série temporal de latência (ms) com baseline aprendido e anomalias
    sinalizadas por z-score robusto (AIOps). A faixa cinza é a banda normal
    (mediana ± k·MAD); os pontos vermelhos são as anomalias detectadas."""
    rng = np.random.default_rng(20240514)
    n = 120
    t = np.arange(n)
    # baseline com leve sazonalidade + ruído gaussiano
    base = 100.0 + 8.0 * np.sin(2 * np.pi * t / 24.0)
    ruido = rng.normal(0.0, 4.0, size=n)
    serie = base + ruido
    # injeta picos (incidentes) em índices fixos
    picos = [33, 70, 71, 98]
    serie[picos] += np.array([55.0, 70.0, 60.0, 80.0])

    mediana = np.median(serie)
    mad = np.median(np.abs(serie - mediana)) * 1.4826
    k = 3.5
    limite_sup = mediana + k * mad
    limite_inf = mediana - k * mad
    z = np.abs(serie - mediana) / mad
    anomalias = z > k

    fig, ax = plt.subplots(figsize=(9.2, 4.6))
    ax.plot(t, serie, color=COR_A, lw=1.6, label="latência (ms)")
    ax.axhspan(limite_inf, limite_sup, color=CINZA, alpha=0.25,
               label="banda normal (mediana ± k·MAD)")
    ax.scatter(t[anomalias], serie[anomalias], color=COR_B, s=55, zorder=5,
               label="anomalia detectada")
    ax.set_xlabel("tempo (amostras)")
    ax.set_ylabel("latência (ms)")
    ax.set_title("AIOps: detecção de anomalias por z-score robusto (mediana/MAD)")
    ax.legend(loc="upper left", fontsize=9)
    return _salvar(fig, SLUG_095, "deteccao-anomalias")


# ===========================================================================
# Lição 096 — IA para DevOps II (auto-remediação com guardrails)
# ===========================================================================
SLUG_096 = "096-ia-devops-ii"


def fig_096_auto_remediacao():
    """Fluxo de auto-remediação com guardrails: do achado de compliance à ação,
    passando por recuperação do runbook (RAG) e pelos portões de segurança."""
    fig, ax = plt.subplots(figsize=(9.6, 5.0))
    ax.set_axis_off()

    _caixa(ax, 0.10, 0.50, 0.15, 0.20, "Achado\n(scan)", COR_B, 10)
    _caixa(ax, 0.32, 0.50, 0.16, 0.20, "RAG sobre\nrunbooks", COR_A, 10)
    _caixa(ax, 0.54, 0.50, 0.17, 0.22, "Guardrails\n(severidade,\nallowlist)", COR_E, 9.5)
    _caixa(ax, 0.78, 0.72, 0.18, 0.20, "Auto-remediar\n(dry-run→apply)", COR_C, 9.5)
    _caixa(ax, 0.78, 0.28, 0.18, 0.20, "Escalar p/\nhumano", COR_D, 9.5)

    _seta(ax, 0.175, 0.50, 0.24, 0.50)
    _seta(ax, 0.40, 0.50, 0.455, 0.50)
    _seta(ax, 0.625, 0.56, 0.69, 0.68, cor="#2e8b57")
    ax.text(0.63, 0.66, "permitido", fontsize=8, color="#2e8b57")
    _seta(ax, 0.625, 0.44, 0.69, 0.32, cor="#8e6abf")
    ax.text(0.63, 0.34, "bloqueado", fontsize=8, color="#8e6abf")

    ax.text(0.5, 0.95,
            "Auto-remediação com guardrails: ações seguras automatizam; o resto escala",
            ha="center", fontsize=10.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0.1, 1)
    return _salvar(fig, SLUG_096, "auto-remediacao")


# ===========================================================================
# Lição 097 — IA para UX & UI (pipeline text-to-UI)
# ===========================================================================
SLUG_097 = "097-ia-ux-ui"


def fig_097_text_to_ui():
    """Pipeline text-to-UI: da intenção em linguagem natural à árvore de
    componentes, à renderização e à validação de fluxos."""
    fig, ax = plt.subplots(figsize=(9.6, 4.2))
    ax.set_axis_off()

    _caixa(ax, 0.12, 0.5, 0.17, 0.26, "Intenção\n(texto)", COR_A, 10)
    _caixa(ax, 0.37, 0.5, 0.17, 0.26, "Árvore de\ncomponentes", COR_D, 10)
    _caixa(ax, 0.62, 0.5, 0.17, 0.26, "Render\n(markup)", COR_C, 10)
    _caixa(ax, 0.87, 0.5, 0.17, 0.26, "Validação\nde fluxo", COR_E, 10)

    _seta(ax, 0.205, 0.5, 0.285, 0.5)
    _seta(ax, 0.455, 0.5, 0.535, 0.5)
    _seta(ax, 0.705, 0.5, 0.785, 0.5)
    # laço de feedback de validação -> intenção
    _seta(ax, 0.87, 0.63, 0.12, 0.63, cor="#9aa7b5", rad=-0.18)
    ax.text(0.5, 0.80, "feedback de validação refina a intenção", fontsize=8.5,
            color="#666", ha="center")

    ax.text(0.5, 0.95,
            "text-to-UI: intenção → árvore → render → validação (com realimentação)",
            ha="center", fontsize=10.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0.2, 1)
    return _salvar(fig, SLUG_097, "text-to-ui")


# ===========================================================================
# Lição 098 — IA para Gestão de Projetos (priorização RICE)
# ===========================================================================
SLUG_098 = "098-ia-gestao-projetos"


def fig_098_priorizacao():
    """Ranking de itens de backlog pelo score RICE = (Reach·Impact·Confidence)/
    Effort. As barras mostram a priorização resultante (maior score no topo)."""
    itens = [
        ("Busca semântica", 8000, 2.0, 0.8, 5.0),
        ("Onboarding guiado", 5000, 1.0, 0.9, 2.0),
        ("Modo offline", 2000, 1.5, 0.5, 8.0),
        ("Exportar PDF", 3000, 0.5, 1.0, 1.0),
        ("Painel de custos", 4000, 2.0, 0.7, 3.0),
    ]
    nomes = []
    scores = []
    for nome, reach, impact, conf, effort in itens:
        score = (reach * impact * conf) / effort
        nomes.append(nome)
        scores.append(score)

    ordem = np.argsort(scores)  # crescente -> maior fica no topo do barh
    nomes_ord = [nomes[i] for i in ordem]
    scores_ord = [scores[i] for i in ordem]

    fig, ax = plt.subplots(figsize=(8.8, 4.6))
    cores = [COR_C if s == max(scores_ord) else COR_A for s in scores_ord]
    ax.barh(nomes_ord, scores_ord, color=cores, alpha=0.85)
    for i, s in enumerate(scores_ord):
        ax.text(s + max(scores_ord) * 0.01, i, f"{s:,.0f}", va="center",
                fontsize=9, color="#222")
    ax.set_xlabel("score RICE = (Reach · Impact · Confidence) / Effort")
    ax.set_title("Priorização de backlog por RICE (verde = maior prioridade)")
    ax.grid(axis="y", alpha=0)
    return _salvar(fig, SLUG_098, "priorizacao-rice")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_095_deteccao_anomalias,
    fig_096_auto_remediacao,
    fig_097_text_to_ui,
    fig_098_priorizacao,
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
