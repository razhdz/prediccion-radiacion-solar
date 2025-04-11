import streamlit as st
import pandas as pd
import joblib

# Cargar modelo
modelo = joblib.load('modelo_radiacion.pkl')

# Título y descripción
st.title("🔆 Predicción de Radiación Solar")
st.write("""
Esta aplicación utiliza inteligencia artificial para predecir la radiación solar en kWh/m²/día 
a partir del año, temperatura promedio y nubosidad. Ideal para proyectos de energía renovable ☀️⚡
""")

# Entradas del usuario
año = st.number_input("Año", min_value=2024, max_value=2100, value=2025)
temperatura = st.number_input("Temperatura promedio (°C)", value=15.0)
nubosidad = st.number_input("Nubosidad promedio (de 0 a 1)", min_value=0.0, max_value=1.0, value=0.2)

# Botón para predecir
if st.button("Predecir"):
    entrada = pd.DataFrame([[año, temperatura, nubosidad]], columns=["AÑO", "TEMPERATURA", "NUBOSIDAD"])
    resultado = modelo.predict(entrada)[0]
    st.success(f"🌞 Radiación solar estimada: **{resultado:.2f} kWh/m²/día**")
#Agregar app.py
