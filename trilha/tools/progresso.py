#!/usr/bin/env python3
"""Helper de progresso da Trilha (R11.3, R11.4, R11.6).

Atualiza e consulta o estado de conclusão das lições em `progresso.yaml`,
mantendo a separação entre conteúdo (imutável) e estado (mutável).

Uso:
    python tools/progresso.py set <NNN> <estado>     # ex.: set 013 concluida
    python tools/progresso.py get <NNN>              # mostra o estado de uma lição
    python tools/progresso.py retomar                # mostra o ponto de retomada
    python tools/progresso.py listar                 # lista estados registrados

Estados válidos: nao_iniciada, em_andamento, concluida (R11.3).
A ausência de registro equivale a "nao_iniciada" (R11.4).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

# Permite rodar como script (`python tools/progresso.py`) ou como módulo.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from validar_trilha import (  # noqa: E402
    EstadoLicao,
    calcular_ponto_de_retomada,
    carregar_licoes,
    ler_progresso,
)

ESTADOS_VALIDOS = [e.value for e in EstadoLicao]


def _raiz_trilha() -> Path:
    """Diretório raiz da Trilha (pai de tools/)."""
    return Path(__file__).resolve().parent.parent


def _caminho_progresso(trilha_dir: Path) -> Path:
    return trilha_dir / "progresso.yaml"


def _carregar_doc(caminho: Path) -> dict:
    if caminho.exists():
        return yaml.safe_load(caminho.read_text(encoding="utf-8")) or {}
    return {}


def _normalizar_ordinal(nnn: str) -> str:
    try:
        return f"{int(nnn):03d}"
    except ValueError:
        return str(nnn)


def _cabecalho_doc(caminho: Path) -> str:
    """Texto do arquivo antes da chave `licoes:` (preserva os comentários-doc)."""
    if not caminho.exists():
        return ""
    linhas = caminho.read_text(encoding="utf-8").splitlines()
    cabecalho: list[str] = []
    for ln in linhas:
        if re.match(r"^licoes\s*:", ln):
            break
        cabecalho.append(ln)
    return "\n".join(cabecalho).rstrip("\n")


def _escrever_progresso(caminho: Path, licoes: dict[str, str]) -> None:
    """Reescreve progresso.yaml preservando o cabeçalho de documentação."""
    cabecalho = _cabecalho_doc(caminho)
    partes: list[str] = []
    if cabecalho:
        partes.append(cabecalho)
        partes.append("")
    if licoes:
        partes.append("licoes:")
        for chave in sorted(licoes):
            partes.append(f'  "{chave}": {licoes[chave]}')
    else:
        partes.append("licoes: {}")
    caminho.write_text("\n".join(partes) + "\n", encoding="utf-8")


def cmd_set(trilha_dir: Path, nnn: str, estado: str) -> int:
    if estado not in ESTADOS_VALIDOS:
        print(f"ERRO: estado inválido '{estado}'. Use um de: {', '.join(ESTADOS_VALIDOS)}",
              file=sys.stderr)
        return 2
    chave = _normalizar_ordinal(nnn)
    caminho = _caminho_progresso(trilha_dir)
    doc = _carregar_doc(caminho)
    licoes = doc.get("licoes")
    if not isinstance(licoes, dict):
        licoes = {}
    licoes = {str(k): str(v) for k, v in licoes.items()}
    if estado == EstadoLicao.NAO_INICIADA.value:
        # "nao_iniciada" é o default: remover a entrada mantém o arquivo enxuto.
        licoes.pop(chave, None)
    else:
        licoes[chave] = estado
    _escrever_progresso(caminho, licoes)
    print(f"OK: lição {chave} -> {estado}")
    return 0


def cmd_get(trilha_dir: Path, nnn: str) -> int:
    chave = _normalizar_ordinal(nnn)
    progresso = ler_progresso(_caminho_progresso(trilha_dir))
    estado = progresso.get(chave, EstadoLicao.NAO_INICIADA)
    print(f"{chave}: {estado.value}")
    return 0


def cmd_retomar(trilha_dir: Path) -> int:
    licoes, _ = carregar_licoes(trilha_dir)
    progresso = ler_progresso(_caminho_progresso(trilha_dir))
    ponto = calcular_ponto_de_retomada(licoes, progresso)
    if ponto is None:
        if licoes:
            print("▶ Trilha completa — todas as lições concluídas.")
        else:
            print("▶ Nenhuma lição encontrada na Trilha.")
        return 0
    print(f"▶ Retomar em: #{ponto.ordinal:03d} — {ponto.titulo}")
    return 0


def cmd_listar(trilha_dir: Path) -> int:
    progresso = ler_progresso(_caminho_progresso(trilha_dir))
    if not progresso:
        print("Nenhum estado registrado (todas as lições: nao_iniciada).")
        return 0
    for chave in sorted(progresso):
        print(f"{chave}: {progresso[chave].value}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Helper de progresso da Trilha.")
    parser.add_argument("--trilha", default=None, type=Path,
                        help="diretório raiz da Trilha (default: detectado a partir de tools/).")
    sub = parser.add_subparsers(dest="comando", required=True)

    p_set = sub.add_parser("set", help="define o estado de uma lição.")
    p_set.add_argument("ordinal")
    p_set.add_argument("estado", choices=ESTADOS_VALIDOS)

    p_get = sub.add_parser("get", help="mostra o estado de uma lição.")
    p_get.add_argument("ordinal")

    sub.add_parser("retomar", help="mostra o ponto de retomada.")
    sub.add_parser("listar", help="lista os estados registrados.")

    args = parser.parse_args(argv)
    trilha_dir = args.trilha or _raiz_trilha()

    if args.comando == "set":
        return cmd_set(trilha_dir, args.ordinal, args.estado)
    if args.comando == "get":
        return cmd_get(trilha_dir, args.ordinal)
    if args.comando == "retomar":
        return cmd_retomar(trilha_dir)
    if args.comando == "listar":
        return cmd_listar(trilha_dir)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
