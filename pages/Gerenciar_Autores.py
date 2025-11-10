import streamlit as st
import pandas as pd
from src.api.api_client import get, post, put, delete

st.set_page_config(page_title="CRUD de Livros", layout="wide")

st.title("👤 Gestão de Autores")

abas = st.tabs(["🧾 Listar", "➕ Cadastrar", "✏️ Editar", "🗑️ Remover"])

with abas[0]:
    st.subheader("🧾 Lista de Autores Cadastrados")

    if st.button("🔄 Atualizar lista"):
        autores = get("autor/all")
        st.write(autores)

with abas[1]:
    st.subheader("➕ Cadastrar Novo Autor")

    nome = st.text_input("Nome do Autor")
    data_nascimento = st.date_input("Data de Nascimento", format="DD/MM/YYYY")
    nacionalidade = st.text_input("Nacionalidade")
    biografia = st.text_area("Biografia")

    if st.button("Cadastrar Autor"):
        dados = {
            "nomeAutor": nome,
            "dataNascimento": str(data_nascimento),
            "nacionalidade": nacionalidade,
            "biografia": biografia,
        }

        resposta = post("autor", dados)
        if resposta.status_code in [200, 201]:
            st.success("Autor cadastrado com sucesso!")
        else:
            st.error("Falha no cadastro!")
            st.write(resposta.json())

with abas[2]:
    st.subheader("✏️ Editar Autor")

    autores = get("autor/all")

    if autores:
        lista_autores = {a["nomeAutor"]: a for a in autores}
        autor_nome = st.selectbox("Selecione o autor para editar", list(lista_autores.keys()))

        if "autor_selecionado" not in st.session_state :
            st.session_state["autor_selecionado"] = lista_autores[autor_nome]

        autor_selecionado = st.session_state["autor_selecionado"]

        nome = st.text_input("Nome do Autor", autor_selecionado["nomeAutor"], key="edit_nome_autor")
        data_nascimento = st.date_input("Data de Nascimento", pd.to_datetime(autor_selecionado["dataNascimento"]), format="DD/MM/YYYY", key="edit_data_nasc")
        nacionalidade = st.text_input("Nacionalidade", autor_selecionado["nacionalidade"], key="edit_nacionalidade")
        biografia = st.text_area("Biografia", autor_selecionado["biografia"], key="edit_biografia")

        if st.button("Salvar Alterações"):
            dados = {
                "idAutor": autor_selecionado["idAutor"],
                "nomeAutor": nome,
                "dataNascimento": str(data_nascimento),
                "nacionalidade": nacionalidade,
                "biografia": biografia
            }

            resposta = put("autor", dados)

            if resposta.status_code in [200, 201]:
                st.success("Autor atualizado com sucesso!")
            else:
                st.error("Falha ao atualizar autor!")
                st.write(resposta.json())
    else:
        st.warning("Nenhum autor encontrado para edição.")

with abas[3]:
    st.subheader("🗑️ Remover Autor")

    autores = get("autor/all")

    if autores:
        lista_autores = {a["nomeAutor"]: a for a in autores}
        autor_nome = st.selectbox("Selecione o autor para remover", list(lista_autores.keys()))
        autor_selecionado = lista_autores[autor_nome]

        if st.button("Remover Autor", key="botao_remover"):
            resposta = delete(f"autor/{autor_selecionado['idAutor']}")
            if resposta.status_code == 200:
                st.success("Autor removido com sucesso!")
            else:
                st.error("Falha ao remover autor!")
                st.write(resposta.json())
    else:
        st.warning("Nenhum autor encontrado para remoção.")