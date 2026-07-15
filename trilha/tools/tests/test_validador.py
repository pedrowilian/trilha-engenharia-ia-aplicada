"""Testes do validador da Trilha de Engenharia de IA Aplicada.

Inclui:
  - Testes baseados em propriedade (Hypothesis) para as 6 propriedades de
    correção do design (subtarefas 2.3, 2.5, 2.7, 2.9, 2.11, 2.13).
  - Testes unitários do validador (subtarefa 2.15).

Cada teste de propriedade está anotado com a propriedade correspondente do
design (Feature: trilha-engenharia-ia).
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest
from hypothesis import HealthCheck, assume, given, settings
from hypothesis import strategies as st

from builders import licao_obj, montar_licao_md, trilha_valida
from validar_trilha import (
    EstadoLicao,
    Licao,
    calcular_ponto_de_retomada,
    carregar_competencias,
    checar_conformidade_template,
    checar_cobertura_topicos,
    checar_dag_completo,
    checar_mapa_competencias,
    destokenizar,
    estado_da_licao,
    executar_exemplo,
    ExemploResolvido,
    ExigenciaMercado,
    ordenacao_valida,
    parse_licao_de_texto,
    parsear_json,
    ResultadoAprendizagem,
    round_trip_igual,
    serializar_json,
    tokenizar,
    TOPICOS_OBRIGATORIOS,
)

RAIZ_TRILHA = Path(__file__).resolve().parent.parent.parent


def _codigos(violacoes) -> set[str]:
    return {v.codigo for v in violacoes}


def _subcodigos(violacoes) -> set[str]:
    return {v.item_ausente for v in violacoes}


# ===========================================================================
# Property 1 — Ordenação válida sse DAG acíclico, contíguo e sem refs pendentes
# ===========================================================================


@st.composite
def _trilha_e_defeito(draw):
    """Gera uma trilha válida (ordinais 1..N, refs apenas para trás) e um defeito."""
    n = draw(st.integers(min_value=2, max_value=8))
    prereqs: dict[int, list[int]] = {}
    for ordinal in range(1, n + 1):
        anteriores = list(range(1, ordinal))
        escolhidos = draw(st.lists(st.sampled_from(anteriores) if anteriores else st.nothing(),
                                   unique=True, max_size=len(anteriores)))
        prereqs[ordinal] = escolhidos
    defeito = draw(st.sampled_from(
        ["valido", "ciclo", "pendente", "duplicado", "lacuna", "frente"]))
    return n, prereqs, defeito


# Feature: trilha-engenharia-ia, Property 1: Ordenação válida sse DAG é acíclico,
# contíguo e sem referências pendentes
@settings(max_examples=100)
@given(_trilha_e_defeito())
def test_ordenacao_topologica(dados):
    n, prereqs, defeito = dados
    licoes = trilha_valida(prereqs)

    if defeito == "valido":
        assert ordenacao_valida(licoes), \
            "uma trilha acíclica, contígua e com refs para trás deve ser válida"
        return

    if defeito == "ciclo":
        # Cria um ciclo entre as duas primeiras lições.
        licoes[0].pre_requisitos = [licoes[1].id]
        licoes[1].pre_requisitos = [licoes[0].id]
        violacoes = checar_dag_completo(licoes)
        assert not ordenacao_valida(licoes)
        assert "CICLO" in _codigos(violacoes)
    elif defeito == "pendente":
        licoes[-1].pre_requisitos = licoes[-1].pre_requisitos + ["licao-999"]
        violacoes = checar_dag_completo(licoes)
        assert not ordenacao_valida(licoes)
        assert "REF_PENDENTE" in _codigos(violacoes)
    elif defeito == "duplicado":
        licoes[1].ordinal = licoes[0].ordinal  # ordinal repetido
        violacoes = checar_dag_completo(licoes)
        assert not ordenacao_valida(licoes)
        assert "ORDINAL_NAO_CONTIGUO" in _codigos(violacoes)
    elif defeito == "lacuna":
        licoes[-1].ordinal = n + 5  # cria lacuna (ordinais não formam 1..N)
        # Limpa pré-requisitos pendurados que dependiam do ordinal antigo é desnecessário.
        violacoes = checar_dag_completo(licoes)
        assert not ordenacao_valida(licoes)
        assert "ORDINAL_NAO_CONTIGUO" in _codigos(violacoes)
    elif defeito == "frente":
        # Faz a primeira lição depender de uma de ordinal maior (aresta para frente).
        licoes[0].pre_requisitos = [licoes[1].id]
        violacoes = checar_dag_completo(licoes)
        assert not ordenacao_valida(licoes)
        # Pode ser detectado como ARESTA_FRENTE (ou CICLO se houver reciprocidade).
        assert {"ARESTA_FRENTE", "CICLO"} & _codigos(violacoes)


# ===========================================================================
# Property 2 — Conformidade de template para toda lição
# ===========================================================================

_DEFEITOS_TEMPLATE = {
    "valido": None,
    "sem_teorica": "UMA_SECAO_TEORICA",
    "sem_pratica": "UMA_SECAO_PRATICA",
    "ordem": "ORDEM_SECOES",
    "sem_motivacao": "MOTIVACAO_AUSENTE",
    "sem_principio": "PRINCIPIO_AUSENTE",
    "poucos_exemplos": "EXEMPLOS_INSUFICIENTES",
    "exemplo_sem_codigo": "EXEMPLO_SEM_CODIGO",
    "exemplo_sem_saida": "EXEMPLO_SEM_SAIDA",
    "poucos_exercicios": "EXERCICIOS_INSUFICIENTES",
    "exercicio_sem_criterio": "EXERCICIO_SEM_CRITERIO",
    "exercicio_sem_solucao": "EXERCICIO_SEM_SOLUCAO",
    "objetivos_demais": "OBJETIVOS_FORA_INTERVALO",
    "objetivos_zero": "OBJETIVOS_FORA_INTERVALO",
    "tempo_excede": "TEMPO_EXCEDE",
    "js_nao_marcado": "JS_NAO_MARCADO",
    "conceito_sem_exemplo": "CONCEITO_SEM_EXEMPLO",
}


def _montar_com_defeito(defeito: str, ordinal: int, tempo: int) -> str:
    kwargs = dict(ordinal=ordinal, tempo=min(tempo, 60))
    if defeito == "sem_teorica":
        kwargs["com_teorica"] = False
    elif defeito == "sem_pratica":
        kwargs["com_pratica"] = False
    elif defeito == "ordem":
        kwargs["pratica_antes"] = True
    elif defeito == "sem_motivacao":
        kwargs["com_motivacao"] = False
    elif defeito == "sem_principio":
        kwargs["com_principio"] = False
    elif defeito == "poucos_exemplos":
        kwargs["n_conceitos"] = 2  # 2 exemplos < 3
    elif defeito == "exemplo_sem_codigo":
        kwargs["exemplo_defeito"] = "sem_codigo"
    elif defeito == "exemplo_sem_saida":
        kwargs["exemplo_defeito"] = "sem_saida"
    elif defeito == "poucos_exercicios":
        kwargs["n_exercicios"] = 2
    elif defeito == "exercicio_sem_criterio":
        kwargs["exercicio_defeito"] = "sem_criterio"
    elif defeito == "exercicio_sem_solucao":
        kwargs["exercicio_defeito"] = "sem_solucao"
    elif defeito == "objetivos_demais":
        kwargs["objetivos"] = 6
    elif defeito == "objetivos_zero":
        kwargs["objetivos_lista"] = []
    elif defeito == "tempo_excede":
        kwargs["tempo"] = 61
    elif defeito == "js_nao_marcado":
        kwargs["js"] = "nao_marcado"
    elif defeito == "conceito_sem_exemplo":
        kwargs["conceito_sem_exemplo"] = True
    return montar_licao_md(**kwargs)


# Feature: trilha-engenharia-ia, Property 2: Conformidade de template para toda lição
@settings(max_examples=100, suppress_health_check=[HealthCheck.too_slow])
@given(
    defeito=st.sampled_from(list(_DEFEITOS_TEMPLATE.keys())),
    ordinal=st.integers(min_value=1, max_value=104),
    tempo=st.integers(min_value=5, max_value=60),
    incluir_js_marcado=st.booleans(),
)
def test_conformidade_template(defeito, ordinal, tempo, incluir_js_marcado):
    md = _montar_com_defeito(defeito, ordinal, tempo)
    licao, vs_meta = parse_licao_de_texto(md, f"gen-{ordinal}.md")
    assert not vs_meta, f"front-matter gerado deveria ser válido: {vs_meta}"
    violacoes = checar_conformidade_template(licao)
    subcodigo_esperado = _DEFEITOS_TEMPLATE[defeito]

    if subcodigo_esperado is None:
        assert violacoes == [], \
            f"lição conforme não deveria gerar violações, mas gerou: {[str(v) for v in violacoes]}"
    else:
        assert subcodigo_esperado in _subcodigos(violacoes), (
            f"defeito '{defeito}' deveria gerar subcódigo '{subcodigo_esperado}'; "
            f"obtidos: {_subcodigos(violacoes)}"
        )


# ===========================================================================
# Property 3 — Round-trip de parsing/serialização preserva a estrutura
# ===========================================================================

_json_estrategia = st.recursive(
    st.one_of(
        st.none(),
        st.booleans(),
        st.integers(min_value=-(10 ** 9), max_value=10 ** 9),
        st.text(),  # inclui Unicode/caracteres especiais
    ),
    lambda filhos: st.one_of(
        st.lists(filhos, max_size=5),
        st.dictionaries(st.text(min_size=1), filhos, max_size=5),
    ),
    max_leaves=15,
)


# Feature: trilha-engenharia-ia, Property 3: Round-trip de parsing/serialização
# preserva a estrutura (JSON de function calling / MCP-JSON-RPC)
@settings(max_examples=100)
@given(_json_estrategia)
def test_roundtrip_parsing_json(estrutura):
    assert round_trip_igual(estrutura, serializar_json, parsear_json), \
        "parse->serialize->parse deve ser igual ao primeiro parse (igualdade exata)"


# Feature: trilha-engenharia-ia, Property 3: Round-trip de parsing/serialização
# preserva a estrutura (árvores de tokens com Unicode)
@settings(max_examples=100)
@given(st.text())
def test_roundtrip_tokenizacao(texto):
    tokens = tokenizar(texto)
    # serialize = destokenizar (tokens -> str); parse = tokenizar (str -> tokens)
    assert round_trip_igual(tokens, destokenizar, tokenizar)
    # E o destokenizar reconstrói o texto original exatamente.
    assert destokenizar(tokens) == texto


# ===========================================================================
# Property 4 — Cobertura completa dos requisitos obrigatórios sem itens órfãos
# ===========================================================================


def _licao_que_cobre(termo: str, ordinal: int) -> Licao:
    return Licao(
        id=f"licao-{ordinal:03d}",
        ordinal=ordinal,
        modulo="M00",
        titulo=termo,
        objetivos_de_aprendizagem=[f"Estudar {termo}"],
    )


# Feature: trilha-engenharia-ia, Property 4: Cobertura completa dos requisitos
# obrigatórios sem itens órfãos (tópicos)
@settings(max_examples=100)
@given(st.sets(st.integers(min_value=0, max_value=len(TOPICOS_OBRIGATORIOS) - 1)))
def test_cobertura_topicos(indices_cobertos):
    licoes = []
    for k, idx in enumerate(sorted(indices_cobertos), start=1):
        termo = TOPICOS_OBRIGATORIOS[idx][2][0]  # primeiro termo do tópico
        licoes.append(_licao_que_cobre(termo, k))

    violacoes = checar_cobertura_topicos(licoes)
    ausentes_reportados = {v.item_ausente for v in violacoes}

    ids_cobertos = {TOPICOS_OBRIGATORIOS[i][0] for i in indices_cobertos}
    ids_esperados_ausentes = {tid for (tid, _r, _t) in TOPICOS_OBRIGATORIOS} - ids_cobertos

    # Todo tópico não coberto deve ser sinalizado.
    assert ids_esperados_ausentes <= ausentes_reportados
    # Nenhum tópico coberto deve ser sinalizado como ausente.
    assert ausentes_reportados.isdisjoint(ids_cobertos)


# Feature: trilha-engenharia-ia, Property 4: Cobertura completa dos requisitos
# obrigatórios sem itens órfãos (mapa de competências)
@settings(max_examples=100)
@given(
    n_exigencias=st.integers(min_value=1, max_value=6),
    # para cada resultado: índice da exigência atendida, ou None (órfão)
    resultados=st.lists(st.one_of(st.none(), st.integers(min_value=0, max_value=5)),
                        min_size=0, max_size=8),
)
def test_cobertura_competencias(n_exigencias, resultados):
    exigencias = [ExigenciaMercado(id=f"req-{i}", descricao=f"Exigência {i}",
                                   categoria="mercado-8")
                  for i in range(n_exigencias)]
    licoes = [licao_obj(1)]
    objs = []
    exigencias_atendidas = set()
    for k, escolha in enumerate(resultados):
        if escolha is None:
            objs.append(ResultadoAprendizagem(id=f"out-{k}", descricao="x",
                                              licao_id="licao-001", exigencias_mercado=[]))
        else:
            ex_id = f"req-{escolha % n_exigencias}"
            objs.append(ResultadoAprendizagem(id=f"out-{k}", descricao="x",
                                              licao_id="licao-001", exigencias_mercado=[ex_id]))
            exigencias_atendidas.add(ex_id)

    violacoes = checar_mapa_competencias(licoes, exigencias, objs)
    codigos = _codigos(violacoes)

    # Outcomes órfãos (sem exigência) devem ser sinalizados.
    tem_orfao = any(escolha is None for escolha in resultados)
    if tem_orfao:
        assert "OUTCOME_ORFAO" in codigos
    # Exigências não atendidas por nenhum resultado devem ser sinalizadas.
    exigencias_sem_resultado = {e.id for e in exigencias} - exigencias_atendidas
    if exigencias_sem_resultado:
        assert "EXIGENCIA_SEM_LICAO" in codigos
        ausentes = {v.item_ausente for v in violacoes if v.codigo == "EXIGENCIA_SEM_LICAO"}
        assert exigencias_sem_resultado <= ausentes


# ===========================================================================
# Property 5 — Ponto de retomada e consistência índice<->progresso
# ===========================================================================


# Feature: trilha-engenharia-ia, Property 5: Ponto de retomada e consistência
# índice<->progresso
@settings(max_examples=100)
@given(
    n=st.integers(min_value=1, max_value=12),
    data=st.data(),
)
def test_ponto_de_retomada(n, data):
    licoes = [licao_obj(o) for o in range(1, n + 1)]
    # Vetor de estados: alguns ordinais ausentes (=> nao_iniciada).
    progresso = {}
    estados_possiveis = ["__ausente__", "nao_iniciada", "em_andamento", "concluida"]
    estados_brutos = data.draw(st.lists(st.sampled_from(estados_possiveis),
                                        min_size=n, max_size=n))
    for ordinal, est in zip(range(1, n + 1), estados_brutos):
        if est == "__ausente__":
            continue
        if est == "nao_iniciada":
            # ausência e nao_iniciada são equivalentes; registramos explicitamente às vezes
            progresso[f"{ordinal:03d}"] = EstadoLicao.NAO_INICIADA
        else:
            progresso[f"{ordinal:03d}"] = EstadoLicao(est)

    # Cálculo de referência do ponto de retomada.
    def estado(o):
        return progresso.get(f"{o:03d}", EstadoLicao.NAO_INICIADA)

    esperado = None
    em_andamento = [o for o in range(1, n + 1) if estado(o) == EstadoLicao.EM_ANDAMENTO]
    if em_andamento:
        esperado = min(em_andamento)
    else:
        nao_iniciadas = [o for o in range(1, n + 1) if estado(o) == EstadoLicao.NAO_INICIADA]
        esperado = min(nao_iniciadas) if nao_iniciadas else None

    ponto = calcular_ponto_de_retomada(licoes, progresso)
    if esperado is None:
        assert ponto is None
    else:
        assert ponto is not None and ponto.ordinal == esperado

    # Consistência: estado exibido == estado registrado (função pura).
    for o in range(1, n + 1):
        assert estado_da_licao(o, progresso) == estado(o)


# ===========================================================================
# Property 6 — Exemplos e soluções executáveis reproduzem a saída exibida
# ===========================================================================


# Feature: trilha-engenharia-ia, Property 6: Exemplos e soluções executáveis
# reproduzem a saída exibida
@settings(max_examples=100, deadline=None,
          suppress_health_check=[HealthCheck.too_slow])
@given(
    a=st.integers(min_value=-1000, max_value=1000),
    b=st.integers(min_value=-1000, max_value=1000),
    defeito=st.sampled_from(["nenhum", "saida_divergente", "erro_execucao"]),
)
def test_exemplos_executaveis(a, b, defeito):
    codigo = f"print({a} + {b})"
    saida_correta = str(a + b)

    if defeito == "nenhum":
        ex = ExemploResolvido(codigo_python=codigo,
                              explicacoes_por_bloco=["soma"],
                              saida_esperada=saida_correta)
        assert executar_exemplo(ex) == [], "exemplo determinístico correto não deve falhar"
    elif defeito == "saida_divergente":
        ex = ExemploResolvido(codigo_python=codigo,
                              explicacoes_por_bloco=["soma"],
                              saida_esperada=str(a + b + 1))  # saída errada
        violacoes = executar_exemplo(ex)
        assert "EXEMPLO_FALHOU" in _codigos(violacoes)
    else:  # erro_execucao
        ex = ExemploResolvido(codigo_python="raise ValueError('boom')",
                              explicacoes_por_bloco=["erro"],
                              saida_esperada="")
        violacoes = executar_exemplo(ex)
        assert "EXEMPLO_FALHOU" in _codigos(violacoes)


# ===========================================================================
# 2.15 — Testes unitários do validador
# ===========================================================================


def test_template_canonico_conforme():
    """O TEMPLATE-licao.md canônico deve passar em todas as regras (Property 2)."""
    texto = (RAIZ_TRILHA / "TEMPLATE-licao.md").read_text(encoding="utf-8")
    licao, vs_meta = parse_licao_de_texto(texto, "TEMPLATE-licao.md")
    assert vs_meta == [], f"front-matter do template deveria ser válido: {vs_meta}"
    violacoes = checar_conformidade_template(licao)
    assert violacoes == [], \
        f"o template canônico deve ser conforme; violações: {[str(v) for v in violacoes]}"


def test_template_canonico_exemplos_executam():
    """Os Exemplos_Resolvidos do template executam e reproduzem a saída (Property 6)."""
    texto = (RAIZ_TRILHA / "TEMPLATE-licao.md").read_text(encoding="utf-8")
    licao, _ = parse_licao_de_texto(texto, "TEMPLATE-licao.md")
    assert len(licao.exemplos_resolvidos) >= 3
    for i, ex in enumerate(licao.exemplos_resolvidos, 1):
        violacoes = executar_exemplo(ex, f"exemplo-{i}")
        assert violacoes == [], f"Exemplo_Resolvido #{i} falhou: {[str(v) for v in violacoes]}"


def test_licao_sem_secao_pratica():
    """Uma lição sem Seção_Prática é não-conforme (UMA_SECAO_PRATICA)."""
    md = montar_licao_md(com_pratica=False)
    licao, _ = parse_licao_de_texto(md, "sem-pratica.md")
    violacoes = checar_conformidade_template(licao)
    assert "UMA_SECAO_PRATICA" in _subcodigos(violacoes)


def test_ciclo_a_b_a():
    """Um ciclo A->B->A é detectado como CICLO (R5.6)."""
    a = licao_obj(1, pre_requisitos=["licao-002"])
    b = licao_obj(2, pre_requisitos=["licao-001"])
    violacoes = checar_dag_completo([a, b])
    assert "CICLO" in _codigos(violacoes)
    assert not ordenacao_valida([a, b])


def test_front_matter_malformado():
    """Front-matter ausente vira METADADOS_INVALIDOS (R2.1)."""
    md = "# Lição sem front-matter\n\n## Seção_Teórica\nblah\n"
    licao, vs = parse_licao_de_texto(md, "ruim.md")
    assert licao is None
    assert any(v.codigo == "METADADOS_INVALIDOS" for v in vs)


def test_front_matter_yaml_invalido():
    """YAML sintaticamente inválido vira METADADOS_INVALIDOS (R2.1)."""
    md = "---\nid: [::: invalido\nordinal: 1\n---\n\n## Seção_Teórica\n"
    licao, vs = parse_licao_de_texto(md, "ruim2.md")
    assert licao is None
    assert any(v.codigo == "METADADOS_INVALIDOS" for v in vs)


def test_campos_obrigatorios_ausentes():
    """Faltar campos obrigatórios no front-matter vira METADADOS_INVALIDOS (R2.1)."""
    md = "---\ntitulo: Só título\n---\n\n## Seção_Teórica\n"
    licao, vs = parse_licao_de_texto(md, "faltando.md")
    assert licao is None
    assert any(v.codigo == "METADADOS_INVALIDOS" for v in vs)


def test_round_trip_exigido_quando_envolve_parsing():
    """Lição com envolve_parsing_serializacao=true sem exercício round-trip falha (R3.6)."""
    from validar_trilha import validar_round_trip
    md = montar_licao_md(envolve_parsing_serializacao=True,
                         incluir_exercicio_round_trip=False)
    licao, _ = parse_licao_de_texto(md, "rt.md")
    violacoes = validar_round_trip(licao)
    assert "ROUNDTRIP_DIVERGENTE" in _codigos(violacoes)

    md_ok = montar_licao_md(envolve_parsing_serializacao=True,
                            incluir_exercicio_round_trip=True)
    licao_ok, _ = parse_licao_de_texto(md_ok, "rt-ok.md")
    assert validar_round_trip(licao_ok) == []


def test_competencias_yaml_exigencias_carregadas():
    """O competencias.yaml do repositório define as 12 exigências (8 + 4)."""
    exigencias, resultados, vs = carregar_competencias(RAIZ_TRILHA / "competencias.yaml")
    assert vs == []
    categorias = {e.categoria for e in exigencias}
    assert "mercado-8" in categorias and "ml-classico-4" in categorias
    assert sum(1 for e in exigencias if e.categoria == "mercado-8") == 8
    assert sum(1 for e in exigencias if e.categoria == "ml-classico-4") == 4
