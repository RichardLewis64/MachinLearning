import pandas as pd

def load_data(file):
    # Cargar datos desde un archivo CSV
    data = pd.read_csv(file)
    
    # Realizar algún preprocesamiento necesario (opcional)
    # data.fillna(0, inplace=True)  # Ejemplo de preprocesamiento
    
    return data