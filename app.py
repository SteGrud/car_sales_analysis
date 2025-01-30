import streamlit as st
import pandas as pd
import plotly.express as px

# Ler o arquivo CSV
car_data = pd.read_csv('data/vehicles.csv')

# Cabeçalho do aplicativo
st.header('Dashboard de Análise de Vendas de Carros')

# Botão para criar o histograma
if st.button('Criar Histograma'):
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros...')
    fig = px.histogram(car_data, x="odometer", title="Histograma de Quilometragem")
    st.plotly_chart(fig, use_container_width=True, key="histogram_chart")

# Botão para criar o gráfico de dispersão
if st.button('Criar Gráfico de Dispersão'):
    st.write('Criando um gráfico de dispersão...')
    fig = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersão: Quilometragem vs Preço")
    st.plotly_chart(fig, use_container_width=True, key="scatter_chart")
