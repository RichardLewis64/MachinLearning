import matplotlib.pyplot as plt
import streamlit as st

def plot_data(data, labels=None):
    fig, ax = plt.subplots()
    ax.plot(data['fecha'], data['ventas'], label='Ventas')
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Ventas')
    ax.set_title('Ventas a lo largo del tiempo')
    
    if labels is not None:
        ax.scatter(data['caracteristica1'], data['caracteristica2'], c=labels, cmap='viridis', label='Clusters')
    
    st.pyplot(fig)
