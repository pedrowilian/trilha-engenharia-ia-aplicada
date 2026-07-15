"""Construtores de artefatos sintéticos para os testes do validador.

Geram lições (objetos `Licao` e texto Markdown) e trilhas, com a capacidade
de injetar defeitos controlados — usados pelos testes baseados em propriedade.
"""
from __future__ import annotations

import yaml

from validar_trilha import Licao


# ---------------------------------------------------------------------------
# Lições como objetos (para checagens de DAG/ordenação — Property 1)
# ---------------------------------------------------------------------------


def licao_obj(ordinal: int, pre_requisitos=None, modulo="M00-fundamentos") -> Licao:
    return Licao(
        id=f"licao-{ordinal:03d}",
        ordinal=ordinal,
        modulo=modulo,
        titulo=f"Lição {ordinal}",
        pre_requisitos=list(pre_requisitos or []),
        objetivos_de_aprendizagem=[f"Objetivo {ordinal}"],
        tempo_estimado_min=30,
        artefato=f"modulos/{modulo}/{ordinal:03d}-licao.md",
    )


def trilha_valida(prereqs_por_ordinal: dict[int, list[int]]) -> list[Licao]:
    """Constrói uma trilha a partir de um mapa ordinal -> lista de ordinais pré-req."""
    licoes = []
    for ordinal in sorted(prereqs_por_ordinal):
        prereqs = [f"licao-{p:03d}" for p in prereqs_por_ordinal[ordinal]]
        licoes.append(licao_obj(ordinal, prereqs))
    return licoes


# ---------------------------------------------------------------------------
# Lições como Markdown (para conformidade de template — Property 2)
# ---------------------------------------------------------------------------


def _bloco_exemplo(numero: str, conceito_idx: int, com_codigo=True,
                   com_explicacao=True, com_saida=True) -> str:
    partes = [f"#### Exemplo_Resolvido {numero}", ""]
    if com_codigo:
        partes += ["```python", f"x = {conceito_idx}", "print(x)", "```", ""]
    else:
        partes += ["(sem bloco de código)", ""]
    if com_explicacao:
        partes += ["**Explicação passo a passo:**",
                   "- **Bloco 1:** define e imprime x.", ""]
    if com_saida:
        partes += ["**Saída esperada:**", "```", str(conceito_idx), "```", ""]
    return "\n".join(partes)


def _bloco_exercicio(n: int, slug: str, com_criterio=True, com_solucao=True,
                     com_saida=True, com_setup=True, round_trip=False) -> str:
    titulo = f"### Exercício {n} — Tarefa {n}"
    if round_trip:
        titulo += " (ida-e-volta)"
    linhas = [titulo]
    if com_setup:
        linhas.append(f"- **Entrada inicial / setup:** dados iniciais do exercício {n}.")
        linhas.append("- **Passos de execução:** rode o script e compare a saída.")
    if com_criterio:
        linhas.append("- **Critério de conclusão (binário):** a saída é exatamente `ok`.")
    if com_solucao:
        linhas.append(f"- **Solução de referência:** `trilha/solucoes/{slug}/solucao_{n}.py`")
    if com_saida:
        linhas.append(f"- **Saída esperada:** `trilha/solucoes/{slug}/solucao_{n}.saida.txt`")
    return "\n".join(linhas) + "\n"


def montar_licao_md(
    *,
    ordinal: int = 13,
    titulo: str = "Tópico de Teste",
    slug: str = "topico-teste",
    pre_requisitos=None,
    objetivos: int = 3,
    tempo: int = 50,
    n_conceitos: int = 3,
    exemplos_por_conceito: int = 1,
    n_exercicios: int = 3,
    com_motivacao: bool = True,
    com_principio: bool = True,
    com_teorica: bool = True,
    com_pratica: bool = True,
    pratica_antes: bool = False,
    exemplo_defeito: str | None = None,   # 'sem_codigo' | 'sem_explicacao' | 'sem_saida'
    exercicio_defeito: str | None = None,  # 'sem_criterio'|'sem_solucao'|'sem_saida'|'sem_setup'
    conceito_sem_exemplo: bool = False,
    js: str | None = None,                 # 'marcado' | 'nao_marcado'
    envolve_parsing_serializacao: bool = False,
    incluir_exercicio_round_trip: bool = True,
    objetivos_lista=None,
) -> str:
    """Monta o Markdown completo de uma lição, com defeitos opcionais."""
    if pre_requisitos is None:
        pre_requisitos = []
    if objetivos_lista is None:
        objetivos_lista = [f"Objetivo observável {i+1}" for i in range(objetivos)]
    conceitos = [f"conceito-{i+1}" for i in range(n_conceitos)]

    front = {
        "id": f"licao-{ordinal:03d}-{slug}",
        "ordinal": ordinal,
        "modulo": "M01-fundamentos-de-ml",
        "titulo": titulo,
        "slug": slug,
        "pre_requisitos": list(pre_requisitos),
        "tempo_estimado_min": tempo,
        "objetivos_de_aprendizagem": objetivos_lista,
        "competencias": [],
        "classificacao_ementa": "complemento de aprofundamento à ementa",
        "conceitos_centrais": conceitos,
        "envolve_parsing_serializacao": envolve_parsing_serializacao,
    }
    fm = "---\n" + yaml.safe_dump(front, allow_unicode=True, sort_keys=False) + "---\n"

    # Monta a Seção_Teórica
    teorica = ["## Seção_Teórica", ""]
    if com_motivacao:
        teorica += ["### Motivação", "Por que este tópico importa.", ""]
    if com_principio:
        teorica += ["### Princípio de funcionamento", "Como o tópico funciona.", ""]

    contador_ex = 0
    for ci in range(n_conceitos):
        teorica += [f"### Conceito central {ci+1} — {conceitos[ci]}",
                    "Explicação do conceito.", ""]
        # Se conceito_sem_exemplo, o último conceito não recebe exemplo.
        if conceito_sem_exemplo and ci == n_conceitos - 1:
            continue
        for e in range(exemplos_por_conceito):
            contador_ex += 1
            defe = exemplo_defeito if contador_ex == 1 else None
            teorica.append(_bloco_exemplo(
                f"{ci+1}.{e+1}", contador_ex,
                com_codigo=(defe != "sem_codigo"),
                com_explicacao=(defe != "sem_explicacao"),
                com_saida=(defe != "sem_saida"),
            ))

    # Monta a Seção_Prática
    pratica = ["## Seção_Prática", "",
               "> **Como reproduzir:** rode cada solução de referência.", ""]
    for n in range(1, n_exercicios + 1):
        defx = exercicio_defeito if n == 1 else None
        rt = incluir_exercicio_round_trip and envolve_parsing_serializacao and n == 1
        pratica.append(_bloco_exercicio(
            n, slug,
            com_criterio=(defx != "sem_criterio"),
            com_solucao=(defx != "sem_solucao"),
            com_saida=(defx != "sem_saida"),
            com_setup=(defx != "sem_setup"),
            round_trip=rt,
        ))

    if js == "marcado":
        pratica += ["", "> ⚠️ **Complemento opcional (JavaScript)** — secundário ao Python.",
                    "```js", "console.log('oi');", "```", ""]
    elif js == "nao_marcado":
        pratica += ["", "Veja também:", "```js", "console.log('oi');", "```", ""]

    corpo_secoes = []
    if com_teorica:
        corpo_secoes.append("\n".join(teorica))
    if com_pratica:
        corpo_secoes.append("\n".join(pratica))
    if pratica_antes:
        corpo_secoes.reverse()

    corpo = f"# Lição {ordinal:03d} — {titulo}\n\n" + "\n\n".join(corpo_secoes) + "\n"
    return fm + "\n" + corpo
