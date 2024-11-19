import streamlit as st

st.title("HISTIDINA")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
pip install dash pandas plotly
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Datos de ejemplo sobre la histidina
histidina_data = {
    "Propiedad": ["Masa molecular", "Fórmula química", "pKa1 (α-COOH)", "pKa2 (α-NH3+)", "pKa3 (cadena lateral)"],
    "Valor": ["155.15 g/mol", "C6H9N3O2", 1.8, 9.3, 6.0],
}

df = pd.DataFrame(histidina_data)

# Datos de pKa en diferentes entornos (valores simulados)
pka_data = {
    "Entorno": ["Solución acuosa", "Ambiente ácido", "Ambiente alcalino", "Proteínas"],
    "pKa1 (α-COOH)": [1.8, 2.0, 1.7, 1.9],
    "pKa2 (α-NH3+)": [9.3, 9.1, 9.5, 9.4],
    "pKa3 (cadena lateral)": [6.0, 5.8, 6.2, 6.1],
}

pka_df = pd.DataFrame(pka_data)

# Inicialización de la aplicación Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Interactivo: Histidina", style={"textAlign": "center"}),
    
    html.Div([
        html.H3("Propiedades Generales de la Histidina"),
        html.Table([
            html.Thead(
                html.Tr([html.Th(col) for col in df.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(df.iloc[i][col]) for col in df.columns
                ]) for i in range(len(df))
            ])
        ], style={"width": "50%", "margin": "auto", "border": "1px solid black"}),
    ], style={"marginBottom": "30px"}),
    
    html.Div([
        html.H3("Gráfico Interactivo de pKa"),
        dcc.Dropdown(
            id="entorno-dropdown",
            options=[{"label": ent, "value": ent} for ent in pka_df["Entorno"]],
            value="Solución acuosa",
            style={"width": "50%", "margin": "auto"}
        ),
        dcc.Graph(id="pka-graph"),
    ]),
    
    html.Div([
        html.H3("Descripción de la Histidina"),
        html.P("""
        La histidina es un aminoácido esencial que desempeña un papel fundamental en la bioquímica humana.
        Posee un grupo imidazol en su cadena lateral, lo que le otorga propiedades únicas como la capacidad de
        actuar como un amortiguador en soluciones biológicas.
        """)
    ], style={"padding": "20px", "textAlign": "justify"}),
])

# Callback para actualizar el gráfico de pKa
@app.callback(
    Output("pka-graph", "figure"),
    Input("entorno-dropdown", "value")
)
def update_graph(selected_entorno):
    entorno_data = pka_df[pka_df["Entorno"] == selected_entorno]
    fig = px.bar(
        entorno_data.melt(id_vars=["Entorno"], var_name="Propiedad", value_name="Valor"),
        x="Propiedad",
        y="Valor",
        title=f"Valores de pKa en el entorno: {selected_entorno}",
        labels={"Valor": "pKa"},
        text="Valor"
    )
    fig.update_traces(textposition="outside")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)

