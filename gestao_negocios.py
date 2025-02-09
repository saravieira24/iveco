# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st

# Título do aplicativo
st.title("Gestão de Negócios de Vendas de Camiões")

# Criar estrutura do DataFrame com os campos fornecidos
colunas = [
    "VENDEDOR", "CLIENTE", "ESTADO", "OBSERVAÇÕES", "PREVISÃO", "MODELO", "NE", "COR", "UND", "STOCK", "VP",
    "VAN", "CMR OU EXG", "ESTADO NEGÓCIO", "FINANCIAMENTO", "RETOMA", "SINAL", "CARROÇARIA", "MATRICULA",
    "PDI", "GARANTIA", "TCO", "ENTREGA"
]

df = pd.DataFrame(columns=colunas)

# Criar uma tabela editável para entrada de dados
st.subheader("Registro de Novos Negócios")
new_data = {}
for col in colunas:
    new_data[col] = st.text_input(f"{col}")

if st.button("Adicionar Negócio"):
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    st.success("Negócio adicionado com sucesso!")

# Exibir a tabela com os negócios cadastrados
st.subheader("Negócios Registrados")
st.dataframe(df)

# Criar um dashboard simples
st.subheader("Dashboard de Vendas")
num_vendas = len(df)
st.metric(label="Total de Negócios Registrados", value=num_vendas)

# Filtros para análise
st.subheader("Filtrar por Vendedor")
vendedor_filtro = st.selectbox("Escolha um vendedor", ["Todos"] + list(df["VENDEDOR"].unique()))

if vendedor_filtro != "Todos":
    df_filtrado = df[df["VENDEDOR"] == vendedor_filtro]
else:
    df_filtrado = df

st.dataframe(df_filtrado)

