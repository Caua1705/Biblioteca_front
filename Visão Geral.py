import streamlit as st
from src.api.api_client import get
from src.ui.charts import grafico_livros_por_categoria, grafico_evolucao_transacoes
from src.ui.metrics import aplicar_estilo_metricas, show_metrics
from utils.agrupar import livros_por_categoria, agrupar_por_transacoes
from utils.style_utils import linha_divisoria, rodape


st.set_page_config(page_title="Dashboard Biblioteca", page_icon="📚", layout="wide")
aplicar_estilo_metricas()
st.title("📈 Visão Geral da Biblioteca")


@st.cache_data(ttl=300)
def get_cached(endpoint):
    return get(endpoint)


livros = get_cached("livro/all")
autores = get_cached("autor/all")
categorias = get_cached("categoria/all")
transacoes = get_cached("transacao/all") 


show_metrics(livros, autores, categorias, transacoes)
linha_divisoria()


df_livros = livros_por_categoria(livros)
df_transacoes = agrupar_por_transacoes(transacoes, 15)


col1, col2 = st.columns(2)
with col1:
    st.markdown("### Evolução de Transações")
    grafico_evolucao_transacoes(df_transacoes)

with col2:
    st.markdown("### Livros por Categoria")
    grafico_livros_por_categoria(df_livros)

rodape()
