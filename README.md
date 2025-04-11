# prediccion-radiacion-solar
IA al servicio de la sostenibilidad 🌞. Coatl Energy MX presenta una app que predice radiación solar para impulsar tus proyectos de energía limpia.
# ☀️ Predicción de Radiación Solar con IA

Una aplicación desarrollada por **Coatl Energy MX** que utiliza técnicas de *Machine Learning* para predecir la radiación solar diaria (kWh/m²/día), basada en variables como el año, temperatura y nubosidad. 

Esta herramienta puede ser útil para:

- El dimensionamiento preliminar de sistemas fotovoltaicos.
- Estudios de potencial solar a largo plazo.
- Evaluación de impacto climático sobre generación solar.

---

## 🚀 ¿Cómo funciona?

El modelo fue entrenado con datos históricos usando un **Random Forest Regressor**. Luego, se integró en una aplicación interactiva con **Streamlit**, permitiendo:

- Ingresar tus propios valores (año, temperatura, nubosidad).
- Obtener predicciones de radiación solar.
- Visualizar resultados en una interfaz simple.

---

## 📦 Requisitos

Instala las dependencias con:

```bash
pip install -r requirements.txt
