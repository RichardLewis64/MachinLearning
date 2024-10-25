import streamlit as st
import pandas as pd
import plotly.express as px

def pagina_principal():
    st.title("Sistema de Predicción de Ventas")
    st.write("Bienbenido al sistema de predicción de ventas")
    st.write("Use el menu de la izquierda para seleccionar una de las opciones")
def visualizacion_datos():
    st.subheader("Visualizacion de datos")
    st.write("Cargue el archivo de ventas que desea usar")
    uploaded_file=st.file_uploader("Cargar archivo de ventas",type="csv,xlsx,xls")
    if uploaded_file is not None:
        data=pd.read_csv and pd.read_excel(uploaded_file)
        st.write(data)
        st.write("estadisticas descriptivas")
    else:
        st.write("No se ha cargado ningun archivo")
def Graficos():
    st.title("Graficos Descriptivos")
    st.write("Cargue el archivo de ventas que desea usar")
    archivo_cargado=st.file_uploader("Cargar archivo de ventas",type=["csv","xlsx"],key="2")
    if archivo_cargado is not None:
     data=pd.read_csv and pd.read_excel(archivo_cargado)
     st.write("Elije una columna para el eje x: ")
     eje_x=st.selectbox("Eje X",data.columns)
     st.write("Elije una columna para el eje y: ")
     eje_y=st.selectbox("Eje y",data.columns)
     st.write("Elije una columna para el color: ")
     color=st.selectbox("Color",data.columns)

     if st.button("Graficar"):
         fig=px.scatter(data,x=eje_x,y=eje_y,color=color,title="{eje_y} por {eje_x}")
         st.plotly_chart(fig)
         #fig = px.bar(data,x=eje_x,y=eje_y,color=color, title= "{eje_y} por {eje_x")
         #st.plotly_chart(fig)
        


st.sidebar.title("Menu de navegacion")
pagina=st.sidebar.selectbox("Seleccione una opcion",["Pagina Principal","visualizacion de datos","Graficos"])

if pagina=="Pagina Principal":
    pagina_principal()
elif pagina=="visualizacion de datos":
    visualizacion_datos()
elif pagina=="Graficos":
    Graficos()

