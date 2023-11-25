import streamlit as st

st.set_page_config(
    page_title="App Vendas",
    page_icon="🏠",
    layout="wide"
)

st.sidebar.markdown('Desenvolvido por [Douglas Macedo](https://www.linkedin.com/in/douglasmacedosilva/)')

st.markdown('# Bem-vindo ao Analisador de Vendas')

st.divider()

st.markdown(
    '''
    Esse projeto foi desenvolvido como aplicação prática do curso ***Full Stack - Xtreme***.

    Utilizaremos três principais bibliotecas para o seu desenvolvimento:

    - `pandas`: para manipulação de dados em tabelas
    - `plotly`: para geração de gráficos
    - `streamlit`: para criação desse webApp interativo que você se encontra nesse momento

    Os dados utilizados são ficticios e apenas para uso didático.

    Para mais informações do curso de FullStack visite nossa página [Xtreme.cx](https://xtreme.cx/).
    '''
            )


