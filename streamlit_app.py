import streamlit as st

st.title("HISTIDINA")
st.sidebar.title("Menú de navegación")
st.sidebar.header("Secciones disponibles")

# Opciones en la barra lateral
opcion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["Información básica", "Funciones biológicas", "Propiedades químicas"]
)
# Contenido dinámico basado en la selección
if opcion == "Información básica":
    st.header("Información básica sobre la Histidina")
    st.write("""
    La histidina es un aminoácido esencial que desempeña un papel crucial en 
    varias funciones biológicas. Su fórmula química es **C₆H₉N₃O₂** y es conocida 
    por ser precursora de la histamina.
    """)
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/94/Histidine_skeletal.svg",
        caption="Estructura molecular de la histidina",
        width=300
    )
elif opcion == "Funciones biológicas":
    st.header("Funciones biológicas de la Histidina")
    st.write("""
    La histidina participa en:
    - La síntesis de proteínas.
    - Producción de hemoglobina.
    - Metabolismo del nitrógeno.
    - Como precursor de la histamina, involucrada en respuestas inmunitarias y digestivas.
    """)
elif opcion == "Propiedades químicas":
    st.header("Propiedades químicas de la Histidina")
    st.write("""
    Algunas propiedades clave:
    - **pKa** del grupo imidazol: ~6.0.
    - **Solubilidad:** Alta en agua.
    - **Peso molecular:** 155.15 g/mol.
    - **Clasificación:** Aminoácido esencial.
    """)

