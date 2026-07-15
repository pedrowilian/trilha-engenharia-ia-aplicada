#!/usr/bin/env python3
"""Gera, de forma REPRODUTÍVEL, as figuras das lições do módulo M06.

As figuras são artefatos de build (PNG) versionados no repositório para que a
pré-visualização local do Markdown (VS Code) as renderize offline, sem depender
de execução. Este script é a fonte da verdade dessas imagens: rodá-lo regenera
TODOS os PNGs do zero, de maneira determinística.

Princípios de reprodutibilidade:
  - Backend "Agg" (sem janela/interatividade);
  - Estilo e tamanhos fixos (sem depender de configuração do usuário);
  - Semente fixa de RNG onde há aleatoriedade.

Uso:
    python trilha/tools/figuras/gerar_figuras_m06.py

As imagens são salvas em:
    trilha/modulos/M06-genai-prompt-apis/assets/<NNN>-<slug>/<nome>.png
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
ASSETS = RAIZ_TRILHA / "modulos" / "M06-genai-prompt-apis" / "assets"

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
# Lição 050 — Panorama de GenAI e modelos multimodais
# ===========================================================================
SLUG_050 = "050-genai-multimodais"


def fig_050_panorama_multimodal():
    """Esquema do fluxo multimodal: três modalidades (texto, imagem, áudio)
    são convertidas em tokens, projetadas num espaço de embedding comum e
    consumidas por um único modelo generativo."""
    fig, ax = plt.subplots(figsize=(9.4, 4.4))
    ax.set_axis_off()

    # Modalidades de entrada (coluna da esquerda)
    _caixa(ax, 0.12, 0.80, 0.18, 0.20, "Texto\n(palavras)", COR_A, 9)
    _caixa(ax, 0.12, 0.50, 0.18, 0.20, "Imagem\n(patches)", COR_C, 9)
    _caixa(ax, 0.12, 0.20, 0.18, 0.20, "Áudio\n(frames)", COR_E, 9)

    # Tokenização por modalidade
    _caixa(ax, 0.40, 0.50, 0.20, 0.64,
           "Tokenização\n(sequência de\nIDs inteiros)", CINZA, 9)
    for y in (0.80, 0.50, 0.20):
        _seta(ax, 0.21, y, 0.30, 0.50 if y != 0.50 else 0.50)

    # Espaço de embedding compartilhado
    _caixa(ax, 0.66, 0.50, 0.18, 0.40,
           "Embedding\ncompartilhado", COR_D, 9)
    _seta(ax, 0.50, 0.50, 0.57, 0.50)

    # Modelo generativo
    _caixa(ax, 0.90, 0.50, 0.16, 0.40,
           "Modelo\ngenerativo", COR_B, 9)
    _seta(ax, 0.75, 0.50, 0.82, 0.50)

    ax.text(0.5, 0.97,
            "Modelos multimodais: modalidades distintas viram tokens num espaço comum",
            ha="center", fontsize=11)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return _salvar(fig, SLUG_050, "panorama-multimodal")


# ===========================================================================
# Lição 051 — APIs de provedores de LLM
# ===========================================================================
SLUG_051 = "051-apis-provedores-llm"


def fig_051_token_custo():
    """Decomposição de tokens (entrada vs saída) e do custo correspondente
    para uma chamada de API, com preços distintos por 1k tokens."""
    prompt_tokens = 1200
    completion_tokens = 400
    preco_in = 0.50 / 1000     # USD por token de entrada
    preco_out = 1.50 / 1000    # USD por token de saída
    custo_in = prompt_tokens * preco_in
    custo_out = completion_tokens * preco_out

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))

    # (a) tokens
    axes[0].bar(["entrada", "saída"], [prompt_tokens, completion_tokens],
                color=[COR_A, COR_B])
    axes[0].set_ylabel("tokens")
    axes[0].set_title("Tokens por chamada")
    for i, v in enumerate([prompt_tokens, completion_tokens]):
        axes[0].text(i, v + 20, str(v), ha="center", fontsize=10)

    # (b) custo (barra empilhada)
    axes[1].bar(["custo"], [custo_in], color=COR_A, label="entrada")
    axes[1].bar(["custo"], [custo_out], bottom=[custo_in], color=COR_B,
                label="saída")
    axes[1].set_ylabel("custo (USD)")
    axes[1].set_title(f"Custo total = ${custo_in + custo_out:.4f}")
    axes[1].legend(fontsize=9)
    axes[1].text(0, custo_in / 2, f"${custo_in:.4f}", ha="center",
                 va="center", color="white", fontsize=9)
    axes[1].text(0, custo_in + custo_out / 2, f"${custo_out:.4f}", ha="center",
                 va="center", color="white", fontsize=9)

    fig.suptitle("Saída custa mais por token: 400 tokens de saída pesam mais que 1200 de entrada",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return _salvar(fig, SLUG_051, "token-custo")


# ===========================================================================
# Lição 052 — Prompt engineering: fundamentos e padrões
# ===========================================================================
SLUG_052 = "052-prompt-engineering-fundamentos"


def fig_052_anatomia_prompt():
    """Anatomia de um prompt bem estruturado: papel/sistema, instrução,
    contexto, exemplos e a consulta do usuário, empilhados na ordem de leitura."""
    partes = [
        ("Sistema / papel", COR_D, "define persona e regras gerais"),
        ("Instrução", COR_A, "a tarefa a ser executada"),
        ("Contexto", COR_C, "dados e documentos de apoio"),
        ("Exemplos", COR_E, "demonstrações (few-shot)"),
        ("Consulta do usuário", COR_B, "a entrada concreta a resolver"),
    ]
    fig, ax = plt.subplots(figsize=(8.6, 4.8))
    ax.set_axis_off()
    n = len(partes)
    h = 0.16
    for i, (nome, cor, desc) in enumerate(partes):
        y = 0.9 - i * (h + 0.03)
        ax.add_patch(plt.Rectangle((0.08, y - h / 2), 0.84, h,
                                   facecolor=cor, alpha=0.18,
                                   edgecolor=cor, lw=1.8))
        ax.text(0.12, y, nome, ha="left", va="center", fontsize=11,
                fontweight="bold", color="#222")
        ax.text(0.88, y, desc, ha="right", va="center", fontsize=9,
                style="italic", color="#444")
    ax.text(0.5, 0.98, "Anatomia de um prompt: do papel geral à consulta concreta",
            ha="center", fontsize=11)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return _salvar(fig, SLUG_052, "anatomia-prompt")


# ===========================================================================
# Lição 053 — Prompt engineering avançado: few-shot, CoT, decomposição
# ===========================================================================
SLUG_053 = "053-prompt-engineering-avancado"


def fig_053_acuracia_tecnicas():
    """Acurácia simulada (ilustrativa) de quatro estratégias de prompting num
    benchmark de raciocínio: zero-shot, few-shot, chain-of-thought e
    decomposição. Valores fixos para fins didáticos."""
    tecnicas = ["zero-shot", "few-shot", "chain-of-\nthought", "decomposição"]
    acuracia = [0.42, 0.61, 0.78, 0.85]
    cores = [CINZA, COR_A, COR_C, COR_D]

    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    barras = ax.bar(tecnicas, acuracia, color=cores)
    ax.set_ylim(0, 1.0)
    ax.set_ylabel("acurácia (ilustrativa)")
    ax.set_title("Estratégias de prompting em tarefas de raciocínio")
    for b, v in zip(barras, acuracia):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.02, f"{v:.2f}",
                ha="center", fontsize=10)
    return _salvar(fig, SLUG_053, "acuracia-tecnicas")


# ===========================================================================
# Lição 054 — Saídas estruturadas e JSON mode
# ===========================================================================
SLUG_054 = "054-saidas-estruturadas-json-mode"


def fig_054_round_trip():
    """Pipeline de ida-e-volta (round-trip) de uma saída estruturada:
    dict -> serialização JSON -> string -> parsing -> dict, com checagem de
    igualdade exata fechando o ciclo."""
    fig, ax = plt.subplots(figsize=(9.6, 3.4))
    ax.set_axis_off()
    y = 0.6
    _caixa(ax, 0.13, y, 0.20, 0.34, "dict\n(Python)", COR_A, 10)
    _caixa(ax, 0.42, y, 0.22, 0.34, "json.dumps\n→ string", COR_E, 10)
    _caixa(ax, 0.72, y, 0.22, 0.34, "json.loads\n→ dict", COR_C, 10)
    _seta(ax, 0.23, y, 0.31, y)
    _seta(ax, 0.53, y, 0.61, y)

    # laço de igualdade de volta ao início
    ax.annotate("", xy=(0.13, 0.40), xytext=(0.72, 0.40),
                arrowprops=dict(arrowstyle="-|>", color=COR_B, lw=1.8,
                                connectionstyle="arc3,rad=0.3"))
    ax.text(0.42, 0.16, "igualdade exata:  dict_final == dict_inicial",
            ha="center", fontsize=10, color=COR_B)
    ax.text(0.5, 0.95,
            "Round-trip: serializar e re-parsear deve preservar a estrutura exatamente",
            ha="center", fontsize=11)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return _salvar(fig, SLUG_054, "round-trip")


# ---------------------------------------------------------------------------
TODAS_AS_FIGURAS = [
    fig_050_panorama_multimodal,
    fig_051_token_custo,
    fig_052_anatomia_prompt,
    fig_053_acuracia_tecnicas,
    fig_054_round_trip,
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
