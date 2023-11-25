import streamlit as st
import pandas as pd
from utilidades import leitura_de_dados
from datetime import datetime
import plotly.express as px 

st.set_page_config(page_title="Produtos", page_icon="🎁", layout="wide")


# Leitura dos dados de utilidades
leitura_de_dados()

# Carregar DataFrames da sessão
df_vendas = st.session_state['dados']['df_vendas']
df_lojas = st.session_state['dados']['df_lojas']

df_data = pd.merge(df_vendas, df_lojas, on= "ID Loja", how= "left")
df_data = df_data.reset_index()


# Selecionar as colunas relevantes e formorta coluna de data
df_data = df_data[['Data','Produto', 'Quantidade', 'Valor Unitário', 'Valor Final', 'Loja']]

df_data ['Data'] = df_data['Data'].dt.strftime('%d/%m/%y')

st.markdown('# Detalhamento dos Produtos')

produtos = df_data['Produto'].unique()
produto = st.sidebar.selectbox("Produtos", produtos)

st.divider()

# Converte e formata dados temporais para criar um g´rafico de linhas
df_data['Data'] = pd.to_datetime(df_data['Data'], format='%d/%m/%y')
df_data['Mês/Ano'] = df_data['Data'].dt.to_period('M')
df_data['Mês/Ano'] = df_data['Mês/Ano'].dt.strftime('%Y-%m')

df_data = df_data.drop(columns=['Data', 'Valor Unitário'], axis=1)
df_data_agrupado = df_data.groupby(['Mês/Ano', 'Loja', 'Produto',])[['Quantidade','Valor Final']].sum().reset_index()
df_data.set_index('Mês/Ano')
df_data_agrupado['Ticket_Medio'] = df_data_agrupado["Valor Final"] / df_data_agrupado['Quantidade']

df_data

#Econtre o Produto com o maior ticker médio
produto_maior_ticket_medio = df_data_agrupado.loc[df_data_agrupado['Ticket_Medio'].idxmax()]['Produto']
maior_tkt = df_data_agrupado.loc[df_data_agrupado['Ticket_Medio'].idxmax()]['Ticket_Medio']

st.markdown(f"### o Produto com o Maior tkt é o/a: {produto_maior_ticket_medio} no valor de R$: {maior_tkt}")

st.divider()

df_data_agrupado = df_data_agrupado[df_data_agrupado['Produto'] == produto]

st.dataframe(df_data_agrupado)