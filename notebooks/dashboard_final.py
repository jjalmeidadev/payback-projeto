import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Final", layout="wide")

# ========================
# CSS do layout
# ========================
st.markdown("""
<style>
.section-card { border-radius:10px; padding:6px; margin:6px 0; }
.section-red  { background: linear-gradient(135deg, #7D1E2F, #3C0D14); }
.section-blue { background: linear-gradient(135deg, #144272, #0A2647); }
.metric-card { background-color:rgba(255,255,255,0.08); border-radius:6px; padding:4px; margin:2px; text-align:center; height:46px; }
.metric-title { font-weight:600; font-size:0.65rem; margin-bottom:2px; }
.metric-value { font-size:0.85rem; font-weight:700; }
</style>
""", unsafe_allow_html=True)

# ========================
# Carregar dados JSON
# ========================
with open("resultados.json", "r", encoding="utf-8") as f:
    resultados = json.load(f)

col_esq, col_dir = st.columns([1, 1])
ALTURA_GRAFICO = 250

# ==========================================================
# Função auxiliar
# ==========================================================
def exibir_grafico_barras(df):
    if "status_do_pagamento" in df.columns:
        contagem = df["status_do_pagamento"].value_counts()
        st.bar_chart(contagem, use_container_width=True, height=ALTURA_GRAFICO)

# ==========================================================
# Seções 4.2 – 4.4 (Tendência de Pagamento)
# ==========================================================
for sec_id, cor in zip(["4.2", "4.3", "4.4"], ["section-blue", "section-red", "section-blue"]):
    with col_esq:
        sec = resultados.get(sec_id, {})
        c = sec.get("classificacao", {})
        st.markdown(f"<div class='section-card {cor}'>", unsafe_allow_html=True)
        st.markdown(f"### {sec.get('titulo', f'Seção {sec_id}')}", unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Acurácia</div><div class='metric-value'>{c.get('acc','—')}</div></div>", unsafe_allow_html=True)
        with m2:
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Precisão</div><div class='metric-value'>{c.get('prec','—')}</div></div>", unsafe_allow_html=True)
        with m3:
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Recall</div><div class='metric-value'>{c.get('rec','—')}</div></div>", unsafe_allow_html=True)
        with m4:
            st.markdown(f"<div class='metric-card'><div class='metric-title'>F1</div><div class='metric-value'>{c.get('f1','—')}</div></div>", unsafe_allow_html=True)

        if c.get("tabela"):
            df = pd.DataFrame(c["tabela"])
            if {"pagador_hash", "status_do_pagamento"}.issubset(df.columns):
                st.dataframe(df[["pagador_hash", "status_do_pagamento"]].head(10),
                             use_container_width=True, height=160)
                exibir_grafico_barras(df)
        else:
            if c.get("y_test") and c.get("y_pred"):
                df = pd.DataFrame({
                    "pagador_hash": list(range(len(c["y_test"]))),
                    "vl_reais": c["y_test"],
                    "previsões": c["y_pred"]
                })
                st.dataframe(df.head(10), use_container_width=True, height=160)
                exibir_grafico_barras(df.rename(columns={"previsões": "status_do_pagamento"}))

        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# Seções 4.6 – 4.8 (Tendência de Valor de Pagamento)
# ==========================================================
for sec_id, cor in zip(["4.6", "4.7", "4.8"],
                       ["section-blue", "section-red", "section-blue"]):
    with col_dir:
        sec = resultados.get(sec_id, {})
        r = sec.get("rf", {})
        st.markdown(f"<div class='section-card {cor}'>", unsafe_allow_html=True)
        st.markdown(f"### {sec.get('titulo', f'Seção {sec_id}')}", unsafe_allow_html=True)

        mae = r.get("mae", "—")
        rmse = r.get("rmse", "—")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                f"<div class='metric-card'><div class='metric-title'>MAE</div><div class='metric-value'>{mae}</div></div>",
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                f"<div class='metric-card'><div class='metric-title'>RMSE</div><div class='metric-value'>{rmse}</div></div>",
                unsafe_allow_html=True,
            )

        df = pd.DataFrame()
        if r.get("detalhes_hash"):
            df = pd.json_normalize(r["detalhes_hash"])
        elif r.get("detalhes_grupo"):
            df = pd.json_normalize(r["detalhes_grupo"])

        if not df.empty:
            # Normaliza nomes e renomeia variações
            df.columns = df.columns.str.strip().str.lower()
            df = df.rename(columns={
                "pagador_inscricao_hash": "pagador_hash",
                "pagamento_total": "valor_boleto_total",
                "valor_boleto": "valor_boleto_total",
                "pagamento_total_previsto": "valor_previsto",
                "valor_previsto_total": "valor_previsto",
                "previsto": "valor_previsto"
            })

            # Garante que existam as colunas necessárias
            for col in ["valor_boleto_total", "valor_previsto"]:
                if col not in df.columns:
                    df[col] = None

            if "pagador_hash" not in df.columns:
                df["pagador_hash"] = range(1, len(df) + 1)

            colunas_final = [c for c in ["pagador_hash", "valor_boleto_total", "valor_previsto"] if c in df.columns]
            st.dataframe(df[colunas_final].head(10),
                         use_container_width=True, height=160)
        else:
            st.warning("Nenhum dado disponível para esta seção.")

        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# Score Final (gráfico de linha)
# ==========================================================
st.markdown("<div class='section-card section-red'>", unsafe_allow_html=True)
st.markdown(f"### {resultados.get('final_score', {}).get('titulo', 'Score Final de Inadimplência')}",
            unsafe_allow_html=True)

score = resultados.get("final_score", {})

if score.get("detalhamento_por_pagador"):
    df_pagador = pd.DataFrame(score["detalhamento_por_pagador"])
    st.markdown("#### Score Médio por Pagador", unsafe_allow_html=True)
    st.dataframe(df_pagador.head(20), use_container_width=True, height=250)

    if {"pagador_inscricao_hash", "score_boleto_media"}.issubset(df_pagador.columns):
        df_plot = df_pagador.sort_values("score_boleto_media").reset_index(drop=True)
        df_plot.index.name = "Pagadores"
        st.line_chart(df_plot["score_boleto_media"], use_container_width=True, height=300)

st.markdown("</div>", unsafe_allow_html=True)
