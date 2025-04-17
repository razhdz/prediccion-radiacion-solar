import streamlit as st
import pandas as pd
import joblib
import numpy as np
import plotly.express as px
# Cargar el modelo guardado
modelo = joblib.load('modelo_radiacion.pkl')
# Título de la app
st.title("Predicción de Radiación Solar para Coatl Energy MX")
# Descripción breve de la app
st.markdown("""
Esta aplicación predice la radiación solar diaria promedio en función de la temperatura, nubosidad y año. 
Utiliza un modelo entrenado basado en datos históricos de radiación solar.
""")
# Formulario interactivo para ingresar datos
st.sidebar.header("Parámetros de entrada")
# Entradas del usuario
anio = st.sidebar.number_input("Año", min_value=2020, max_value=2027, value=2023)
temperatura = st.sidebar.slider("Temperatura Promedio (°C)", min_value=-10, max_value=40, value=20)
nubosidad = st.sidebar.slider("Porcentaje de Nubosidad", min_value=0, max_value=100, value=50)
# Preparar los datos de entrada para el modelo
entrada = np.array([anio, temperatura, nubosidad]).reshape(1, -1)
# Botón para hacer la predicción
if st.sidebar.button("Predecir Radiación Solar"):
    # Hacer la predicción
    prediccion = modelo.predict(entrada)  
    # Mostrar el resultado de la predicción
    st.subheader(f"Radiación solar predicha para el año {anio}:")
    st.write(f"{prediccion[0]:.2f} kWh/m²/día")
    # Crear un gráfico de la predicción usando Plotly
    fig = px.bar(x=[anio], y=[prediccion[0]], labels={'x': 'Año', 'y': 'Radiación (kWh/m²/día)'},
                 title="Predicción de Radiación Solar")
    st.plotly_chart(fig)
# Agregar una recomendación o análisis adicional si se desea
st.markdown("""
Basado en los resultados de la predicción, se pueden tomar decisiones informadas sobre la planificación de la 
instalación de sistemas solares o la optimización de la energía renovable para el año especificado.
""")
#agregar app.py
