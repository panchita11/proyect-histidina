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

Tanto de origen animal como vegetal, por lo que su carencia es una condición extraña y normalmente asociada a alteraciones genéticas o malnutrición severa.""")
    st.write("""La histidina se obtiene por hidrólisis de numerosas sustancias proteicas.
Desde el punto de vista físico se presenta en cristales incoloros, ópticamente activos, solubles en agua, insolubles en alcohol y en éter, que por descarboxilación se transforman en histamina. Puede obtenerse por síntesis de diferentes formas. En cuanto a su valor nutricional, la histidina no se considera un aminoácido esencial para hombres adultos y adolescentes, mientras que sí lo es para la primera infancia. También es esencial para la mayoría de los mamíferos.
La histidina está contenida en proporciones relativamente altas en la hemoglobina. El grupo imidazol de la histidina constituye el sitio activo de muchas enzimas: las modificaciones químicas de residuos de histidina específicos provocan de hecho su inactivación. La principal vía del catabolismo de la histidina en mamíferos y humanos pasa por su transformación en ácido glutámico, que comienza con la degradación de la histidina a ácido urocánico por la acción de la enzima histidasa.
La deficiencia hereditaria de histidinasa (la enzima que descompone la histidina) que puede transmitirse como rasgo recesivo, conduce a la acumulación en la circulación de histidina (histidinemia) con un cuadro de retraso mental y estatutario, anemia, pigmentación deficiente de la piel; también se acompaña de un aumento de la excreción del aminoácido en la orina (histidinuria). La histidinuria elevada puede ocurrir durante el embarazo (histidinuria gravidarum) y en algunas condiciones de insuficiencia hepática funcional.""")
    st.image("https://arribasalud.com/wp-content/uploads/2018/02/histidina-665x285.jpg")
elif opcion == "Funciones biológicas":
    st.header("Funciones biológicas de la Histidina")
    st.write("""
    La histidina participa en:
    - La síntesis de proteínas: La histidina es un componente de las proteínas, incorporándose durante la traducción del ARN mensajero en los ribosomas.
    - Producción de hemoglobina:Estabilizan la unión del oxígeno a través de interacciones con el hierro del grupo hemo.
Regulan la afinidad de la hemoglobina al oxígeno en respuesta a cambios en pH (efecto Bohr), debido a la capacidad del anillo imidazol de la histidina para aceptar o donar protones.
    - Metabolismo del nitrógeno:La histidina participa en el metabolismo del nitrógeno como fuente de este elemento. Es desaminada por la enzima histidasa para formar urocanato, un paso inicial en su degradación. 
    - Como precursor de la histamina, involucrada en respuestas inmunitarias y digestivas:La enzima histidina descarboxilasa convierte la histidina en histamina, que actúa como:

Mediador inmunológico: Promueve la inflamación y la vasodilatación en respuesta a lesiones o alérgenos.
Regulador digestivo: Estimula la secreción de ácido gástrico en el estómago, facilitando la digestión.
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
   
   
