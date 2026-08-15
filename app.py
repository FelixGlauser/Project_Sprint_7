import pandas as pd
import plotly.express as px
import streamlit as st
df = pd.read_csv("vehicles_us.csv")
st.header("Análisis de anuncios de vehículos")
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Distribución del kilometraje de los vehículos")

    fig = px.histogram(
        df,
        x="odometer",
        title="Distribución del kilometraje",
        labels={
            "odometer": "Kilometraje"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Construir gráfico de dispersión")
if scatter_button:
    st.write("Precio en función del kilometraje")

    fig = px.scatter(
        df,
        x="odometer",
        y="price",
        title="Precio en función del kilometraje",
        labels={
            "odometer": "Kilometraje",
            "price": "Precio"
        }
    )

    st.plotly_chart(fig, use_container_width=True)