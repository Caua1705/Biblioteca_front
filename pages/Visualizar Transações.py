import streamlit as st
import pandas as pd
from src.api.api_client import get  

st.set_page_config(page_title="Visualizar Transações por Usuário", layout="wide")
st.title("📚 Visualizar Transações por Usuário")

opcao = st.radio(
    "Escolha o que deseja visualizar:",
    ("Acessos", "Downloads", "Valor Gasto")
)

transacoes = get("transacao/all")

df = pd.DataFrame(transacoes)
st.divider()

if opcao == "Acessos":
    agrupado_acessos = df[df["tipo"] == "ACESSO"].groupby('nomeUsuario').size().reset_index(name="acessos")
    st.subheader("Acessos por Usuário")
    st.dataframe(agrupado_acessos)

elif opcao == "Downloads":
    agrupado_downloads = df[df["tipo"] == "DOWNLOAD"].groupby('nomeUsuario').size().reset_index(name="downloads")
    st.subheader("Downloads por Usuário")
    st.dataframe(agrupado_downloads)

elif opcao == "Valor Gasto":
    agrupado_valor = df.groupby('nomeUsuario').agg(
        total_gasto=('valor', 'sum')
    ).reset_index()
    st.subheader("Total Gasto por Usuário")
    st.dataframe(agrupado_valor)
