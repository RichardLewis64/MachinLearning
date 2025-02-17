import pandas as pd
import streamlit as st

def load_data(file=None, use_internal=False):
    if use_internal:
        data = pd.read_csv('data/tanques_productos_plasticos.csv')
        st.success("Datos internos cargados exitosamente")
    elif file is not None:
        data = pd.read_csv(file)
        st.success("Archivo subido cargado exitosamente")
    else:
        data = None
        st.warning("No se ha cargado ningún archivo o dataset")
    
    return data
