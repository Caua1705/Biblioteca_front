import streamlit as st

def aplicar_estilo_metricas():
    st.markdown("""
    <style>
        .stMetric {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 12px;
            box-shadow: 0 0 5px rgba(0,0,0,0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            color: #111827;
        }

        .stMetric:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        [data-testid="stColumn"]:nth-of-type(1) .stMetric {
            border-left: 6px solid #2563eb;  /* Azul */
        }
        [data-testid="stColumn"]:nth-of-type(2) .stMetric {
            border-left: 6px solid #16a34a;  /* Verde */
        }
        [data-testid="stColumn"]:nth-of-type(3) .stMetric {
            border-left: 6px solid #f59e0b;  /* Amarelo */
        }
        [data-testid="stColumn"]:nth-of-type(4) .stMetric {
            border-left: 6px solid #dc2626;  /* Vermelho */
        }
    </style>
    """, unsafe_allow_html=True)
    

def show_metrics(livros, autores, categorias, transacoes):
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📚 Livros", len(livros))
    c2.metric("✍️ Autores", len(autores))
    c3.metric("🏷️ Categorias", len(categorias))
    c4.metric("🔄 Transações", len(transacoes))
