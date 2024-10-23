import streamlit as st
import pandas as pd
from data_loader import load_data
from model import train_model, predict_sales, train_clustering, train_logistic_regression
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

    # Selección de modelo
    model_option = st.selectbox("Selecciona el modelo de predicción", 
                                ["Regresión Lineal", "Clustering", "Regresión Logística"])

    if model_option == "Regresión Lineal":
        if st.button("Entrenar modelo de regresión lineal y predecir"):
            model, mse = train_model(data)
            st.write(f"Error cuadrático medio: {mse}")
            predictions = predict_sales(model, data)
            st.write("Predicción de ventas:", predictions)

    elif model_option == "Clustering":
        if st.button("Aplicar clustering"):
            labels = train_clustering(data)
            st.write("Etiquetas de clusters:", labels)

    elif model_option == "Regresión Logística":
        if st.button("Entrenar modelo de regresión logística y predecir"):
            model, accuracy = train_logistic_regression(data)
            st.write(f"Precisión del modelo: {accuracy}")
            predictions = predict_sales(model, data)
            st.write("Predicción de ventas:", predictions)