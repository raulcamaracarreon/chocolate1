import streamlit as st
import pandas as pd
import base64

def calculate_ingredients(manteca_de_cacao):
    cacao_en_polvo = manteca_de_cacao * 0.25
    azucar = manteca_de_cacao * 0.3
    brandy_gramos = manteca_de_cacao * 0.02 * 15 * 0.67
    vainilla_gramos = manteca_de_cacao * 0.005 * 4.2
    leche_polvo = 40.0  # Cantidad fija de leche en polvo (ajusta el valor según tus necesidades)
    lecitina_soya = manteca_de_cacao * 0.01  # Cantidad de lecitina de soya añadida (ajusta el valor según tus necesidades)
    return cacao_en_polvo, azucar, brandy_gramos, vainilla_gramos, leche_polvo, lecitina_soya

st.set_page_config(page_title="Calculadora de ingredientes para barra de chocolate amargo con brandy", page_icon=":chocolate_bar:")

st.markdown("<h1 style='text-align: center; font-weight: bold;'>Calculadora de ingredientes para barra de chocolate amargo con brandy</h1>", unsafe_allow_html=True)

manteca_de_cacao = st.number_input("Cantidad de manteca de cacao (en gramos)", min_value=0.0, step=1.0, value=150.0)

cacao_en_polvo, azucar, brandy_gramos, vainilla_gramos, leche_polvo, lecitina_soya = calculate_ingredients(manteca_de_cacao)

total = manteca_de_cacao + cacao_en_polvo + azucar + brandy_gramos + vainilla_gramos + leche_polvo + lecitina_soya

data = {
    "Ingrediente": ["Manteca de cacao", "Cacao en polvo sin azúcar", "Azúcar, jarabe o endulzante", "Brandy", "Extracto de vainilla", "Leche en polvo", "Lecitina de soya", "TOTAL"],
    "Cantidad": [manteca_de_cacao, cacao_en_polvo, azucar, brandy_gramos, vainilla_gramos, leche_polvo, lecitina_soya, total],
    "Unidad": ["gramos", "gramos", "gramos", "gramos", "gramos", "gramos", "gramos", "gramos"]
}

df = pd.DataFrame(data)

st.write(df)

csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="receta_chocolate_amargo.csv">Descargar receta</a>'
st.markdown(href, unsafe_allow_html=True)

