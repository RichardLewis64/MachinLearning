from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_model(data):
    X = data[['caracteristica1', 'caracteristica2']]  # Reemplazar con las columnas reales
    y = data['ventas']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    
    return model, mse

def predict_sales(model, data):
    X = data[['caracteristica1', 'caracteristica2']]  # Ajustar según tus datos
    predictions = model.predict(X)
    return predictions
