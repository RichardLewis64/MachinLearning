import matplotlib.pyplot as plt
import streamlit as st

def plot_data(data):
    fig, ax = plt.subplots()
    ax.plot(data['fecha'], data['ventas'], label='Ventas')  # Ajustar según tus datos
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Ventas')
    ax.set_title('Ventas a lo largo del tiempo')
    
    st.pyplot(fig)