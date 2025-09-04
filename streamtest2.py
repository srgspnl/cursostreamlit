# app_educacional.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- Configuração da Página ---
st.set_page_config(
    page_title="App Educacional com Streamlit",
    layout="wide"
)

# Título principal da aplicação
st.title("👨‍🏫 Aplicação Educacional de Demonstração")
st.markdown("---")

# =========================================================================
# 1. Barra de Slider e o número aparecendo
# =========================================================================
st.header("1. Barra de Slider")
st.write("Mova o controle deslizante para ver o número correspondente.")

# Cria um slider com um valor padrão, mínimo e máximo
valor_slider = st.slider(
    "Escolha um número",
    min_value=0,
    max_value=100,
    value=50,
    step=1
)

# Exibe o valor selecionado pelo usuário
st.info(f"O número selecionado é: **{valor_slider}**")
st.markdown("---")

# =========================================================================
# 2. Entrada de dados e gráficos de frutas
# =========================================================================
st.header("2. Entrada de Dados e Gráficos de Frutas")
st.write("Insira a quantidade de cada fruta para gerar gráficos dinâmicos.")

# Lista de frutas para entrada de dados
frutas = [
    "Maçã", "Banana", "Laranja", "Uva", "Morango",
    "Abacaxi", "Manga", "Pera", "Limão", "Melancia"
]

# Usa colunas para uma entrada de dados mais organizada
col1, col2 = st.columns(2)
quantidades = {}

with col1:
    st.subheader("Quantidades")
    for i in range(len(frutas)):
        quantidades[frutas[i]] = st.number_input(
            f"Quantidade de {frutas[i]}",
            min_value=0,
            value=0,
            key=f"fruta_{i}"
        )

# Converte o dicionário em um DataFrame do Pandas para os gráficos
df_frutas = pd.DataFrame(quantidades.items(), columns=["Fruta", "Quantidade"])
# Exclui frutas com quantidade zero para não poluir o gráfico
df_frutas = df_frutas[df_frutas["Quantidade"] > 0]

with col2:
    if not df_frutas.empty:
        st.subheader("Gráficos Gerados")
        # Gráfico de Barras
        fig_bar = go.Figure(data=go.Bar(x=df_frutas["Fruta"], y=df_frutas["Quantidade"]))
        fig_bar.update_layout(title_text="Gráfico de Barras - Quantidade de Frutas")
        st.plotly_chart(fig_bar, use_container_width=True)

        # Gráfico de Pizza
        fig_pie = go.Figure(data=go.Pie(labels=df_frutas["Fruta"], values=df_frutas["Quantidade"]))
        fig_pie.update_layout(title_text="Gráfico de Pizza - Proporção de Frutas")
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.warning("Insira a quantidade de pelo menos uma fruta para gerar os gráficos.")

st.markdown("---")

# =========================================================================
# 3. Contador de palavras
# =========================================================================
st.header("3. Contador de Palavras")
st.write("Digite um texto para contar o número de palavras (limite de 50 palavras).")

# Cria uma caixa de texto para o usuário digitar
texto = st.text_area("Digite seu texto aqui:", height=150)

# Processa o texto e conta as palavras
if texto:
    palavras = texto.split()
    numero_palavras = len(palavras)

    # Exibe a contagem de palavras
    st.success(f"O seu texto tem **{numero_palavras}** palavras.")

    # Verifica se o texto excede o limite de 50 palavras
    if numero_palavras > 50:
        st.warning("⚠️ O seu texto excedeu o limite de 50 palavras.")

# --- Instruções de Execução ---
st.markdown("---")
st.subheader("Instruções para Execução")
st.info("""
Para executar este programa, salve o código em um arquivo `app_educacional.py`.
Certifique-se de ter as bibliotecas `streamlit`, `pandas` e `plotly` instaladas. Se não as tiver, use o seguinte comando no seu terminal:

`pip install streamlit pandas plotly`

Em seguida, execute a aplicação com o seguinte comando:

`streamlit run app_educacional.py`
""")
