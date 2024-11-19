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
    st.write("""
   La histidina es uno de los 22 aminoácidos proteinogénicos, aquellos que codifican nuestro código genético y son utilizados para la síntesis de proteínas. Además es considerado uno de los 9 aminoácidos esenciales que requerimos consumir a través de la dieta para evitar sufrir signos de degradación proteica y malnutrición.""")
    st.image(
        "https://thumbs.dreamstime.com/b/f%C3%B3rmula-qu%C3%ADmica-de-histidina-estructura-molecular-ilustraci%C3%B3n-vectorial-aislada-en-fondo-blanco-238646983.jpg",
        caption="Estructura molecular de la histidina",
        width=300
    )
    st.write("""En la naturaleza encontramos el enantiómero levorrotarorio de la histidina, es decir, la forma L-histidina.

Es un aminoácido muy presente en gran cantidad de alimentos, tanto de origen animal como vegetal, por lo que su carencia es una condición extraña y normalmente asociada a alteraciones genéticas o malnutrición severa.""")
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
    st.video("""<div class="sketchfab-embed-wrapper"> <iframe title="Eve3D Aminoácido Histidina" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/56604a3421fd497a90e21de0ce3cd9f3/embed"> </iframe> <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"> <a href="https://sketchfab.com/3d-models/eve3d-aminoacido-histidina-56604a3421fd497a90e21de0ce3cd9f3?utm_medium=embed&utm_campaign=share-popup&utm_content=56604a3421fd497a90e21de0ce3cd9f3" target="_blank" rel="nofollow" style="font-weight: bold; color: #1CAAD9;"> Eve3D Aminoácido Histidina </a> by <a href="https://sketchfab.com/eve3d_unam?utm_medium=embed&utm_campaign=share-popup&utm_content=56604a3421fd497a90e21de0ce3cd9f3" target="_blank" rel="nofollow" style="font-weight: bold; color: #1CAAD9;"> EVE3D UNAM </a> on <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=56604a3421fd497a90e21de0ce3cd9f3" target="_blank" rel="nofollow" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a></p></div>""")

