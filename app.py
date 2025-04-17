import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

# Cargar el modelo
modelo = joblib.load('modelo_radiacion.pkl')

# Título de la app
st.title("Predicción de Radiación Solar - Coatl Energy MX")

# Entrada de año
año = st.slider("Selecciona el Año para la Predicción:", min_value=2025, max_value=2030, value=2025)

# Simulamos un dataframe para entrada
X_input = pd.DataFrame({
    'AÑO': [año],
    'TEMPERATURA': [23.0],  # Ajusta según sea necesario
    'NUBOSIDAD': [60.0]     # Ajusta según sea necesario
})

# Predicción
prediccion = modelo.predict(X_input)[0]
st.write(f"Predicción de radiación para el año {año}: {prediccion:.2f} kWh/m²/día")

# Datos históricos (simulados)
historicos = {
    'Año': [2020, 2021, 2022, 2023],
    'Radiación (kWh/m²/día)': [5.8, 5.6, 5.7, 5.69]  # Simulación de datos históricos
}
df_hist = pd.DataFrame(historicos)

# Gráfico de barras con predicción
fig = px.bar(df_hist, x='Año', y='Radiación (kWh/m²/día)', 
             title="Radiación Solar: Predicción vs Históricos", 
             labels={'Radiación (kWh/m²/día)': 'Radiación (kWh/m²/día)'})
fig.add_bar(x=[año], y=[prediccion], name=f'Predicción {año}', marker_color='red')
st.plotly_chart(fig)

# Gráfico de tendencia
fig_trend = px.line(df_hist, x='Año', y='Radiación (kWh/m²/día)', 
                    title="Tendencia de Radiación Solar en los Últimos Años")
st.plotly_chart(fig_trend)

# Estimación de energía generada
eficiencia = 0.15
potencia_instalada = 1  # en MW
energia_generada = prediccion * potencia_instalada * eficiencia * 365  # energía anual estimada
st.write(f"Estimación de energía generada para el año {año}: {energia_generada:.2f} kWh/anual")
#agregar app.py
