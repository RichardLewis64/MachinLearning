import streamlit as st
import pandas as pd
from data_loader import load_data
from model import train_model, train_clustering, train_logistic_regression
from utils.visualization import plot_data

st.title("Sistema de Predicción de Ventas")

# Controles en el sidebar
st.sidebar.header("Opciones de datos y modelo")

# Elegir entre cargar archivo o usar dataset interno en el sidebar
data_option = st.sidebar.radio("Selecciona el origen de los datos:", ("Cargar archivo", "Usar dataset interno"))

if data_option == "Cargar archivo":
    uploaded_file = st.sidebar.file_uploader("Sube el archivo de ventas")
    if uploaded_file:
        data = load_data(uploaded_file)
else:
    data = load_data(use_internal=True)

# Mostrar los datos si están cargados
if data is not None:
    st.write(data)

    # Visualización de los datos
    st.subheader("Visualización de los datos")
    plot_data(data)

    # Selección de modelo en el sidebar
    model_option = st.sidebar.selectbox("Selecciona el modelo de predicción", 
                                        ["Regresión Lineal", "Clustering", "Regresión Logística"])

    if model_option == "Regresión Lineal":
        if st.sidebar.button("Entrenar modelo de regresión lineal y predecir"):
            model, mse = train_model(data)
            st.write(f"Error cuadrático medio: {mse}")
            predictions =(model, data)
            st.write("Predicción de ventas:", predictions)

    elif model_option == "Clustering":
        if st.sidebar.button("Aplicar clustering"):
            labels = train_clustering(data)
            st.write("Etiquetas de clusters:", labels)

    elif model_option == "Regresión Logística":
        if st.sidebar.button("Entrenar modelo de regresión logística y predecir"):
            model, accuracy = train_logistic_regression(data)
            st.write(f"Precisión del modelo: {accuracy}")
            predictions =(model, data)
            st.write("Predicción de ventas:", predictions)