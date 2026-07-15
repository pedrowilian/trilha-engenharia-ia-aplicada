#!/usr/bin/env python3
"""Gera, de forma REPRODUTIVEL, as figuras das licoes do modulo M12.

Modulo M12 - Avaliacao, Custo/Latencia e MLOps/LLMOps (licoes 085-089).

As figuras sao artefatos de build (PNG) versionados no repositorio para que a
pre-visualizacao local do Markdown (VS Code) as renderize offline, sem depender
de execucao. Este script e a fonte da verdade dessas imagens: roda-lo regenera
TODOS os PNGs do zero, de maneira deterministica.

Principios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuracao do usuario);
  - Semente fixa de RNG onde ha aleatoriedade.

Uso:
    python3 trilha/tools/figuras/gerar_figuras_m12.py

As imagens sao salvas em:
    trilha/modulos/M12-avaliacao-custo-latencia-llmops/assets/<NNN>-<slug>/<nome>.png
e referenciadas nas licoes por caminho RELATIVO (assets/<...>.png).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # backend nao interativo (deterministico, sem display)

import matplotlib.pyplot as plt
import numpy as np

# --- Estilo fixo, independente da config do usuario -------------------------
plt.rcParams.update({
    "figure.dpi": 110,
    "savefig.dpi": 110,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# --- Localizacao dos assets (relativa a este arquivo) -----------------------
RAIZ_TRILHA = Path(__file__).resolve().parents[2]   # .../trilha
ASSETS = RAIZ_TRILHA / "modulos" / "M12-avaliacao-custo-latencia-llmops" / "assets"

COR_A = "#1f5fa8"
COR_B = "#c1432a"
COR_C = "#2e8b57"
COR_D = "#8e6abf"
COR_E = "#d39a00"
CINZA = "#9aa7b5"


def _salvar(fig, slug: str, nome: str) -> Path:
    """Salva a figura em assets/<slug>/<nome>.png e fecha a figura."""
    destino = ASSETS / slug / f"{nome}.png"
    destino.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destino, bbox_inches="tight")
    plt.close(fig)
    return destino


def _caixa(ax, x, y, w, h, texto, cor, fontsize=10):
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=cor, alpha=0.18,
                               edgecolor=cor, lw=1.8, zorder=2))
    ax.text(x + w / 2, y + h / 2, texto, ha="center", va="center",
            fontsize=fontsize, color="#1a1a1a", zorder=3)


def _seta(ax, x0, y0, x1, y1, cor="#444"):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=cor, lw=2.0))


# ===========================================================================
# Licao 085 - Metodologia de avaliacao e evals
# ===========================================================================
SLUG_085 = "085-evals-metodologia"


def fig_085_harness_evals():
    """Anatomia de um harness de eval: dataset -> sistema -> scorer -> agregacao."""
    fig, ax = plt.subplots(figsize=(9.4, 3.8))
    ax.set_axis_off()
    y, h = 0.40, 0.30
    _caixa(ax, 0.00, y, 0.17, h, "Dataset\n(input, esperado)", COR_A, 9)
    _caixa(ax, 0.22, y, 0.17, h, "Sistema sob\nteste (SUT)", COR_D, 9)
    _caixa(ax, 0.44, y, 0.17, h, "Scorer\n(metrica)", COR_C, 9)
    _caixa(ax, 0.66, y, 0.17, h, "Agregacao\n(accuracy)", COR_E, 9)
    _caixa(ax, 0.88, y, 0.12, h, "Relatorio\n+ veredito", COR_B, 9)
    for x0, x1 in [(0.17, 0.22), (0.39, 0.44), (0.61, 0.66), (0.83, 0.88)]:
        _seta(ax, x0, y + h / 2, x1, y + h / 2)
    # gabarito alimentando o scorer
    _caixa(ax, 0.44, 0.82, 0.17, 0.14, "Gabarito\n(esperado)", CINZA, 9)
    _seta(ax, 0.525, 0.82, 0.525, y + h, COR_C)
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(0.30, 1.02)
    ax.set_title("Harness de eval: dados rotulados entram, veredito reprodutivel sai")
    return _salvar(fig, SLUG_085, "harness-evals")


# ===========================================================================
# Licao 086 - Metricas e datasets de avaliacao
# ===========================================================================
SLUG_086 = "086-metricas-datasets-avaliacao"


def fig_086_metricas_classificacao():
    """Compara precisao/revocacao/F1 de dois sistemas de recuperacao."""
    metricas = ["Precisao", "Revocacao", "F1"]
    sist_a = [0.80, 0.50, 0.6154]
    sist_b = [0.60, 0.75, 0.6667]
    x = np.arange(len(metricas))
    largura = 0.36

    fig, ax = plt.subplots(figsize=(8.0, 4.4))
    ax.bar(x - largura / 2, sist_a, largura, label="Sistema A (preciso)",
           color=COR_A, edgecolor="white")
    ax.bar(x + largura / 2, sist_b, largura, label="Sistema B (abrangente)",
           color=COR_C, edgecolor="white")
    ax.set_xticks(x)
    ax.set_xticklabels(metricas)
    ax.set_ylim(0, 1.0)
    ax.set_ylabel("valor da metrica")
    ax.legend()
    ax.set_title("Precisao x Revocacao: o F1 resume o equilibrio entre as duas")
    return _salvar(fig, SLUG_086, "metricas-classificacao")


# ===========================================================================
# Licao 087 - Otimizacao de custo de inferencia
# ===========================================================================
SLUG_087 = "087-custo-inferencia"


def fig_087_custo_vs_throughput():
    """Custo por requisicao cai conforme o tamanho do lote (overhead amortizado)."""
    lotes = np.array([1, 2, 4, 8, 16, 32, 64])
    # custo = custo variavel fixo por req + overhead fixo do lote dividido pelo lote
    custo_variavel = 0.0020         # $/req (tokens)
    overhead_lote = 0.0160          # $/lote (chamada/infra), amortizado
    custo_por_req = custo_variavel + overhead_lote / lotes
    throughput = lotes              # proxy: req atendidas por chamada em lote

    fig, ax = plt.subplots(figsize=(8.2, 4.4))
    ax.plot(throughput, custo_por_req * 1000, "o-", color=COR_A, lw=2.0,
            markersize=7, label="custo por requisicao")
    ax.axhline(custo_variavel * 1000, color=COR_B, ls="--", lw=1.5)
    ax.text(throughput[-1], custo_variavel * 1000 + 0.3,
            "piso = custo variavel", color=COR_B, ha="right", fontsize=9)
    ax.set_xlabel("throughput (requisicoes por lote)")
    ax.set_ylabel("custo por requisicao (milesimos de $)")
    ax.set_title("Custo de inferencia: lotes maiores amortizam o overhead fixo")
    ax.legend()
    return _salvar(fig, SLUG_087, "custo-vs-throughput")


# ===========================================================================
# Licao 088 - Otimizacao de latencia de inferencia
# ===========================================================================
SLUG_088 = "088-latencia-inferencia"


def fig_088_percentis_latencia():
    """Distribuicao de latencias com marcadores p50/p95/p99."""
    rng = np.random.default_rng(42)
    # latencias em ms: corpo log-normal + cauda pesada (alguns lentos)
    amostras = rng.lognormal(mean=5.4, sigma=0.45, size=4000)
    p50 = np.percentile(amostras, 50)
    p95 = np.percentile(amostras, 95)
    p99 = np.percentile(amostras, 99)

    fig, ax = plt.subplots(figsize=(8.4, 4.4))
    ax.hist(amostras, bins=60, color=CINZA, alpha=0.55, edgecolor="white")
    for valor, cor, rotulo in [(p50, COR_C, "p50"), (p95, COR_E, "p95"),
                               (p99, COR_B, "p99")]:
        ax.axvline(valor, color=cor, lw=2.0, ls="--")
        ax.text(valor, ax.get_ylim()[1] * 0.92, f" {rotulo}={valor:.0f}ms",
                color=cor, fontsize=9, rotation=90, va="top")
    ax.set_xlabel("latencia (ms)")
    ax.set_ylabel("frequencia")
    ax.set_title("Latencia tem cauda: a media engana, os percentis revelam")
    return _salvar(fig, SLUG_088, "percentis-latencia")


# ===========================================================================
# Licao 089 - MLOps / LLMOps e observabilidade
# ===========================================================================
SLUG_089 = "089-mlops-llmops-observabilidade"


def fig_089_pipeline_llmops():
    """Ciclo LLMOps: tracing -> metricas -> deploy/rollout -> observar."""
    fig, ax = plt.subplots(figsize=(9.2, 4.0))
    ax.set_axis_off()
    y, h = 0.42, 0.30
    _caixa(ax, 0.00, y, 0.18, h, "Tracing\n(prompts/spans)", COR_A, 9)
    _caixa(ax, 0.23, y, 0.18, h, "Metricas\n(custo/lat/erros)", COR_C, 9)
    _caixa(ax, 0.46, y, 0.18, h, "SLO/alertas\n(verifica metas)", COR_E, 9)
    _caixa(ax, 0.69, y, 0.18, h, "Deploy/rollout\n(canary)", COR_D, 9)
    for x0, x1 in [(0.18, 0.23), (0.41, 0.46), (0.64, 0.69)]:
        _seta(ax, x0, y + h / 2, x1, y + h / 2)
    # producao realimenta o tracing (laco de observabilidade)
    _caixa(ax, 0.69, 0.04, 0.18, 0.16, "Producao", CINZA, 9)
    _seta(ax, 0.78, 0.42, 0.78, 0.20, COR_D)
    ax.annotate("", xy=(0.09, y), xytext=(0.69, 0.12),
                arrowprops=dict(arrowstyle="-|>", color="#555", lw=1.6,
                                connectionstyle="arc3,rad=-0.18"))
    ax.text(0.39, 0.14, "telemetria realimenta o tracing", color="#555",
            fontsize=9, ha="center")
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(0.0, 1.0)
    ax.set_title("LLMOps: observar em producao fecha o ciclo de melhoria")
    return _salvar(fig, SLUG_089, "pipeline-llmops")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_085_harness_evals,
    fig_086_metricas_classificacao,
    fig_087_custo_vs_throughput,
    fig_088_percentis_latencia,
    fig_089_pipeline_llmops,
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
