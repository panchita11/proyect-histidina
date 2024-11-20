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
    
    - Producción de hemoglobina:Estabilizan la unión del oxígeno a través de interacciones con el hierro del grupo hemo.Regulan la afinidad de la hemoglobina al oxígeno en respuesta a cambios en pH (efecto Bohr), debido a la capacidad del anillo imidazol de la histidina para aceptar o donar protones.

    - Metabolismo del nitrógeno:La histidina participa en el metabolismo del nitrógeno como fuente de este elemento. Es desaminada por la enzima histidasa para formar urocanato, un paso inicial en su degradación. 
    
    - Precursor de la histamina, involucrada en respuestas inmunitarias y digestivas:La enzima histidina descarboxilasa convierte la histidina en histamina, que actúa como mediador inmunológico, promueve la inflamación y la vasodilatación en respuesta a lesiones o alérgenos y regulador digestivo estimula la secreción de ácido gástrico en el estómago, facilitando la digestión.
    """)
elif opcion == "Propiedades químicas":
    st.header("Propiedades químicas de la Histidina")
    st.write(""" 
    -pKa del grupo imidazol: ~6.0.
    
    -Solubilidad: Alta en agua.
    
    -Peso molecular: 155.15 g/mol.
    
    -Clasificación: Aminoácido esencial.
    
    Comparación del pH Isoeléctrico (pI) de la Histidina y otras Proteínas""")
   
import streamlit as st
import plotly.graph_objects as go
import py3Dmol
# Función para renderizar el modelo 3D de la histidina
def render_modelo_3d():
    histidina_pdb = """
HETATM    1  N   HIS A   1      -1.204   0.689   0.000  1.00  0.00           N  
HETATM    2  CA  HIS A   1      -0.012   0.000   0.000  1.00  0.00           C  
HETATM    3  C   HIS A   1       1.264   0.763   0.000  1.00  0.00           C  
HETATM    4  O   HIS A   1       1.304   2.000   0.000  1.00  0.00           O  
HETATM    5  CB  HIS A   1      -0.312  -1.523   0.000  1.00  0.00           C  
HETATM    6  CG  HIS A   1      -0.890  -2.089   1.222  1.00  0.00           C  
HETATM    7  ND1 HIS A   1      -1.812  -1.241   2.035  1.00  0.00           N  
HETATM    8  CD2 HIS A   1      -0.768  -3.366   1.799  1.00  0.00           C  
HETATM    9  CE1 HIS A   1      -2.209  -1.921   3.126  1.00  0.00           C  
HETATM   10  NE2 HIS A   1      -1.516  -3.110   2.963  1.00  0.00           N  
HETATM   11  H   HIS A   1      -1.204   1.677   0.000  1.00  0.00           H  
HETATM   12  HA  HIS A   1      -0.001  -0.024   0.987  1.00  0.00           H  
HETATM   13  HB2 HIS A   1       0.012  -1.877   0.000  1.00  0.00           H  
HETATM   14  HB3 HIS A   1      -0.898  -1.853  -0.863  1.00  0.00           H  
"""
    viewer = py3Dmol.view(width=600, height=400)
    viewer.addModel(histidina_pdb, 'pdb')
    viewer.setStyle({'stick': {}})
    viewer.zoomTo()
    return viewer

# Configuración del dashboard
st.set_page_config(page_title="Dashboard de Histidina", layout="wide")

# Título principal
st.title("Dashboard Interactivo: Histidina")

# Descripción general
st.markdown("""
La **histidina** es un aminoácido esencial involucrado en múltiples procesos biológicos. 
Este dashboard interactivo te permitirá explorar sus propiedades, compararla con otras moléculas y visualizar su estructura en 3D.
""")

# Sidebar con opciones
st.sidebar.title("Opciones")
mostrar_info = st.sidebar.checkbox("Mostrar información general", value=True)
mostrar_grafica = st.sidebar.checkbox("Mostrar gráfica comparativa", value=True)
mostrar_modelo = st.sidebar.checkbox("Mostrar modelo 3D", value=True)

# Información general
if mostrar_info:
    st.subheader("Información General")
    st.markdown("""
    - **Fórmula molecular**: C₆H₉N₃O₂  
    - **Masa molecular**: 155.15 g/mol  
    - **pH isoeléctrico (pI)**: 7.59  
    - **Clasificación**: Aminoácido esencial.  
    - **Funciones**:
        - Precursor de histamina.
        - Participa en la regulación del pH.
        - Componente clave en sitios activos de enzimas.  
    """)

# Gráfica comparativa
if mostrar_grafica:
    st.subheader("Comparación del pH Isoeléctrico (pI)")
    proteinas = ['Histidina', 'Albumina', 'Hemoglobina', 'Mioglobina', 'Caseína']
    pi_valores = [7.59, 4.9, 6.8, 7.0, 4.6]

    fig = go.Figure(data=[go.Bar(
        x=proteinas,
        y=pi_valores,
        text=pi_valores,
        textposition='auto',
        marker_color=['blue', 'green', 'red', 'purple', 'orange']
    )])
    fig.update_layout(
        title="pH Isoeléctrico de la Histidina comparado con otras moléculas",
        xaxis_title="Moléculas",
        yaxis_title="pI",
        template="plotly_white"
    )
    st.plotly_chart(fig)

# Modelo 3D
if mostrar_modelo:
    st.subheader("Modelo 3D de la Histidina")
    streamlit run dashboard_histidina.py
    modelo_3d = render_modelo_3d()
    modelo_html = modelo_3d._make_html()
    st.components.v1.html(modelo_html, width=600, height=400)

