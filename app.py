import streamlit as st
import joblib
import numpy as np
import datetime

# Cargar el modelo
modelo = joblib.load("modelo_radiacion.pkl")

# Estilo de página
st.set_page_config(
    page_title="Predicción Solar - Coatl Energy MX",
    page_icon="☀️",
    layout="centered"
)

# Encabezado
st.title("🔆 Predicción de Radiación Solar")
st.subheader("Desarrollado por Coatl Energy MX")
st.markdown("---")

# Estilo informativo
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stApp {
        font-family: 'Arial', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Entradas del usuario
st.markdown("### 🧾 Ingresa los datos para estimar la radiación:")

año = st.slider("Año", min_value=2020, max_value=2030, value=2025)
temperatura = st.number_input("🌡️ Temperatura promedio (°C)", min_value=-10.0, max_value=60.0, value=25.0)
nubosidad = st.slider("☁️ Nivel de nubosidad (0.0 = despejado, 1.0 = muy nublado)", 0.0, 1.0, 0.3)

# Predicción
if st.button("📊 Predecir radiación"):
    entrada = np.array([[año, temperatura, nubosidad]])
    resultado = modelo.predict(entrada)[0]
    
    st.success(f"🔅 Radiación solar estimada: **{resultado:.2f} kWh/m²/día**")

    # Estimación anual
    generacion_anual = resultado * 365 * 5_000  # Ejemplo con 5000 m² de panel
    st.info(f"⚡ Generación estimada anual: **{generacion_anual:,.2f} kWh**")

# Footer
st.markdown("---")
st.caption("© 2025 Coatl Energy MX · Predicción impulsada por Machine Learning")

