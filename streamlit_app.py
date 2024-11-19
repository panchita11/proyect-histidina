import streamlit as st

st.title("HISTIDINA")
pip install dash
import dash
from dash import dcc, html

# Inicializar la app de Dash
app = dash.Dash(__name__)

# Contenido de la página
app.layout = html.Div(
    style={'fontFamily': 'Arial, sans-serif', 'margin': '20px'},
    children=[
        html.H1("Información básica sobre la Histidina", style={'textAlign': 'center', 'color': '#2C3E50'}),
        html.Div(
            style={'marginTop': '20px'},
            children=[
                html.H2("Descripción general"),
                html.P(
                    "La histidina es un aminoácido esencial, especialmente importante en el desarrollo infantil. "
                    "Tiene un papel crucial en la síntesis de proteínas y como precursor de la histamina, un "
                    "compuesto vital en las respuestas inmunitarias, digestivas y neurológicas."
                ),
                html.H2("Propiedades químicas"),
                html.Ul([
                    html.Li("Fórmula química: C₆H₉N₃O₂"),
                    html.Li("Peso molecular: 155.15 g/mol"),
                    html.Li("Clasificación: Aminoácido esencial"),
                    html.Li("pKa del grupo imidazol: ~6.0"),
                ]),
                html.H2("Estructura molecular"),
                html.P(
                    "La histidina contiene un grupo imidazol que le confiere propiedades únicas, "
                    "permitiendo actuar como un donador o receptor de protones en reacciones bioquímicas."
                ),
                html.Div(
                    style={'textAlign': 'center', 'marginTop': '20px'},
                    children=[
                        html.Img(
                            src="https://upload.wikimedia.org/wikipedia/commons/9/94/Histidine_skeletal.svg",
                            style={'width': '300px', 'height': 'auto'},
                            alt="Estructura molecular de la histidina"
                        ),
                        html.P("Figura: Estructura molecular de la histidina", style={'fontSize': '12px'}),
                    ]
                ),
            ]
        ),
        html.Div(
            style={'marginTop': '40px'},
            children=[
                html.H2("Importancia biológica"),
                html.P(
                    "La histidina es esencial en la producción de hemoglobina y en el mantenimiento del equilibrio ácido-base "
                    "del cuerpo. También participa en el metabolismo del nitrógeno y actúa como un precursor de importantes "
                    "compuestos bioquímicos."
                )
            ]
        ),
    ]
)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)


