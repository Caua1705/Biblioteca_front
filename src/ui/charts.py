import streamlit as st
import plotly.express as px
from config.ui_config import CORES_GRAFICO_BARRAS

def grafico_livros_por_categoria(df_livros):
    fig = px.bar(
    df_livros,
    x="Categoria",
    y="Quantidade",
    text="Quantidade",
    title="Quantidade de Livros por Categoria",
        color="Categoria",  
        color_discrete_map = CORES_GRAFICO_BARRAS
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        title_font_size=18,
        xaxis_tickangle=0,
        font=dict(color="#111827", size=13),
        margin=dict(l=20, r=20, t=40, b=40)
    )

    st.plotly_chart(fig, use_container_width=True)


def grafico_evolucao_transacoes(df_transacoes):
    fig = px.line(
        df_transacoes, "Data", "count",
        line_shape="spline", markers=True
    )
    fig.update_traces(line=dict(width=2, color="green"))  

    fig.update_layout(
        title={'text': "Quantidade de Transações por Dia (Últimos 15 Dias)", 'x': 0.0, 'xanchor': 'left'},
        xaxis_title="Data", yaxis_title="Quantidade",
        plot_bgcolor="white",
        xaxis=dict(showgrid=True, gridcolor="#E5E7EB", dtick="D1",
                   tickformat="%d/%m", tickangle=-45),
        yaxis=dict(showgrid=True, gridcolor="#E5E7EB"),
        font=dict(color="#111827")
    )

    st.plotly_chart(fig, use_container_width=True)