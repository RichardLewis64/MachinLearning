import streamlit as st
##import pandas as pd
from data_loader import load_data
from model import train_model, predict_sales
from utils.visualization import plot_data

st.title("Sistema de Predicción de Ventas")

# Subir archivo
uploaded_file = st.file_uploader("Sube el archivo de ventas")
if uploaded_file:
    data = load_data(uploaded_file)  # Cargar datos
    st.write(data)

    # Visualización de los datos
    st.subheader("Visualización de los datos")
    plot_data(data)

    # Entrenar y hacer predicciones
    if st.button("Entrenar modelo y predecir"):
        model, mse = train_model(data)
        st.write(f"Error cuadrático medio: {mse}")

        # Realizar predicciones
        predictions = predict_sales(model, data)
        st.write("Predicción de ventas:", predictions)