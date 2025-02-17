from datetime import date
import streamlit as st
import pandas as pd
from data_loader import load_data
from model import train_model, train_clustering, train_logistic_regression
from utils.visualization import plot_data
from Login import authenticate_user

st.title("Sistema de Predicción de Ventas")

# Autenticación de usuario
if authenticate_user():
    # Barra de navegación
    menu = ["Inicio", "Cargar Datos", "Modelos de ML"]
    choice = st.sidebar.selectbox("Menú", menu)

    if choice == "Inicio":
        st.subheader("Bienvenido al Sistema de Predicción de Ventas")

    elif choice == "Cargar Datos":
        st.subheader("Cargar Datos")
        data_option = st.radio("Selecciona el origen de los datos:", ("Cargar archivo", "Usar dataset interno"))

        if data_option == "Cargar archivo":
            uploaded_file = st.file_uploader("Sube el archivo de ventas")
            if uploaded_file:
                data = load_data(uploaded_file)
        else:
            data = load_data(use_internal=True)

        if data is not None:
            st.write(data)
            st.subheader("Visualización de los datos")
            plot_data(data)

    elif choice == "Modelos de ML":
        st.subheader("Modelos de Machine Learning")
        model_option = st.selectbox("Selecciona el modelo de predicción", 
                                    ["Regresión Lineal", "Clustering", "Regresión Logística"])

        if model_option == "Regresión Lineal":
            if st.button("Entrenar modelo de regresión lineal y predecir"):
                model, mse = train_model(data)
                st.write(f"Error cuadrático medio: {mse}")
                predictions = model.predict(data[['Capacidad_litros', 'Tipo_Plastico']])
                st.write("Predicción de ventas:", predictions)

        elif model_option == "Clustering":
            if st.button("Aplicar clustering"):
                labels = train_clustering(data)
                st.write("Etiquetas de clusters:", labels)

        elif model_option == "Regresión Logística":
            if st.button("Entrenar modelo de regresión logística y predecir"):
                model, accuracy = train_logistic_regression(data)
                st.write(f"Precisión del modelo: {accuracy}")
                predictions = model.predict(data[['Capacidad_litros', 'Tipo_Plastico']])
                st.write("Predicción de ventas:", predictions)
else:
    st.warning("Por favor, introduce tus credenciales")
