import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Carga el modelo entrenado
modelo = joblib.load('modelo_radiacion.pkl')

# Carga los datos originales
df = pd.read_csv('datos_filtrados.csv')
df.columns = df.columns.str.replace('ï»¿', '')  # Corrige nombres raros
X = df[['AÑO', 'TEMPERATURA', 'NUBOSIDAD']]
y_real = df['ALLSKY']

# Predicción
y_pred = modelo.predict(X)

# Métricas
mae = mean_absolute_error(y_real, y_pred)
rmse = np.sqrt(mean_squared_error(y_real, y_pred))
r2 = r2_score(y_real, y_pred)

print(f"\n📊 Evaluación del Modelo:")
print(f"MAE (Error Absoluto Medio): {mae:.2f}")
print(f"RMSE (Raíz del Error Cuadrático Medio): {rmse:.2f}")
print(f"R² (Coeficiente de Determinación): {r2:.2f}\n")
