import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl as op

st.set_page_config(page_title="Prova", layout="wide")

@st.cache_data
def carregar_dados(caminho_arquivo):
    xls = pd.ExcelFile(caminho_arquivo)

    abas_acidentes = [sheet for sheet in xls.sheet_names]

    #dados_totais = []

    

    return abas_acidentes

caminho_arquivo = r"H:\ProvaPython_41\acidentes.xlsx"

df = carregar_dados(caminho_arquivo)

st.title("Painel acidentes")
st.header("prova maria cecilia")

st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])

if opcao == "Tabela":
    st.header("Tabela")
    st.text("nao consegui carregar o xlsx de jeito nenhum considera oq deu certo pfv")
    st.dataframe(df, use_container_width=True, hide_index=True)
    

elif opcao == "Gráficos":
    st.header("Gráficos")
    st.subheader("Gráfico de Barras")
    st.text("nao funcionou pq nn tem nada no df mas olha o codigo pra ver se da pra considerar algm coisa pfv")
    #fig_barras = px.bar(
        #df,
        #x="dia_da_semana",
        #y="acidentes_do_dia",
        #color="NOMEUP",
        #barmode="group",
        #title="Acidentes por dia da semana",
        #color_discrete_map={"segunda-feira": "#FF6B6B", "terça-feira": "#00F5D4", "quarta-feira": "#F005D4", "quinta-feira": "#FFF5D4", "sexta-feira": "#00F5D4", "sábado":"#0000", "domingo":"#FFFFF"}
        #template="plotly_dark"
    #)
    #fig_barras.update_xaxes(type="category")
    #fig_barras.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    #st.plotly_chart(fig_barras, use_container_width=True)



st.markdown("---")
st.caption("Fonte: https://basedosdados.org/")

#python -m streamlit run app.py