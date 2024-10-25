import streamlit as st
from data_loader import load_data
from model import train_model, train_clustering, train_logistic_regression
from utils.visualization import plot_data
from Loging import authenticate_user  # Importar la función de autenticación

# Autenticación del usuario
if authenticate_user():
    st.sidebar.title("Navegación")
    # Barra de navegación
    page = st.sidebar.selectbox("Selecciona una página", ["Inicio", "Regresión Lineal", "Clustering", "Regresión Logística"])

    # Cargar los datos
    data_option = st.sidebar.radio("Selecciona el origen de los datos:", ("Cargar archivo", "Usar dataset interno"))
    data = None
    if data_option == "Cargar archivo":
        uploaded_file = st.sidebar.file_uploader("Sube el archivo de ventas")
        if uploaded_file:
            data = load_data(uploaded_file)
    else:
        data = load_data(use_internal=True)
    
    if data is not None:
        st.write(data)
        st.subheader("Visualización de los datos")
        plot_data(data)

        if page == "Regresión Lineal":
            st.header("Regresión Lineal")
            if st.button("Entrenar modelo de regresión lineal"):
                model, mse = train_model(data)
                st.write(f"Error cuadrático medio: {mse}")

        elif page == "Clustering":
            st.header("Clustering")
            if st.button("Aplicar clustering"):
                labels = train_clustering(data)
                st.write("Etiquetas de clusters:", labels)

        elif page == "Regresión Logística":
            st.header("Regresión Logística")
            if st.button("Entrenar modelo de regresión logística"):
                model, accuracy = train_logistic_regression(data)
                st.write(f"Precisión del modelo: {accuracy}")

else:
    st.warning("Por favor, inicia sesión para acceder a la aplicación.")
