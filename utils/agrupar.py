import pandas as pd

def livros_por_categoria(livros):
    df_livros = pd.DataFrame(livros)
    df_livros["categoria_nome"] = df_livros["categoria"].apply(lambda x: x["nomeCategoria"])
    df_livros = df_livros[["nomeLivro", "categoria_nome"]]

    df_agrupado = df_livros["categoria_nome"].value_counts().reset_index()
    df_agrupado = df_agrupado.rename(columns={"categoria_nome":"Categoria","count":"Quantidade"})
    return df_agrupado

def agrupar_por_transacoes(transacoes, limite):
    df_transacoes = pd.DataFrame(transacoes)

    df_transacoes["dataHora"] = pd.to_datetime(df_transacoes["dataHora"])
    df_transacoes["Data"] = df_transacoes["dataHora"].dt.date

    data_minima = df_transacoes["Data"].min()
    data_maxima = df_transacoes["Data"].max()

    df_transacoes_por_data = df_transacoes["Data"].value_counts().reset_index()

    df_intervalo_datas = pd.DataFrame({
    "Data": pd.date_range(data_minima, data_maxima, freq="D").date
})
    
    df_concatenado = (
        pd.merge(df_intervalo_datas, df_transacoes_por_data, on="Data", how="left")
        .fillna(0)
        .sort_values(by="Data")
    )
    return df_concatenado.tail(limite)
