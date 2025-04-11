import streamlit as st
import numpy as np
import joblib

# Cargar el modelo previamente entrenado
modelo = joblib.load('modelo_radiacion.pkl')

# Título de la app
st.title('☀️ Predicción de Radiación Solar')
st.subheader('by Coatl Energy MX')

st.markdown("""
Esta aplicación predice la **radiación solar promedio diaria (kWh/m²/día)** 
usando como entrada el año, la temperatura promedio y la nubosidad.
""")

# Entradas del usuario
año = st.number_input('Año', min_value=2020, max_value=2100, value=2025, step=1)
temperatura = st.number_input('Temperatura promedio (°C)', value=25.0)
nubosidad = st.number_input('Nubosidad promedio (0 a 1)', min_value=0.0, max_value=1.0, value=0.2)

# Crear un arreglo con los datos ingresados
input_data = np.array([[año, temperatura, nubosidad]])

# Botón para predecir
if st.button('Predecir Radiación Solar'):
    prediccion = modelo.predict(input_data)
    st.success(f'🌞 Radiación solar estimada: {prediccion[0]:.2f} kWh/m²/día')
#Agregar app.py
