import streamlit as st

def linha_divisoria():
    st.markdown(
        """
        <hr style="
            margin-top: 0.5rem;
            margin-bottom: 1rem;
            border: none;
            border-top: 1px solid rgba(0,0,0,0.15);
        ">
        """,
        unsafe_allow_html=True
    )

def rodape():
    st.markdown(
    """
    <div style='text-align: center; margin-top: 30px; color: #6b7280;'>
        📚 Sistema de Biblioteca — Desenvolvido por <b>Cauã, Luís e Cristiano</b> | © 2025 Todos os direitos reservados
    </div>
    """,
    unsafe_allow_html=True
)