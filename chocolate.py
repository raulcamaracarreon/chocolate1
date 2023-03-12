import streamlit as st
import pandas as pd
import base64



def calculate_ingredients(manteca_de_cacao):
    cacao_en_polvo = manteca_de_cacao * 0.25
    azucar = manteca_de_cacao * 0.3
    brandy_gramos = manteca_de_cacao * 0.02 * 15 * 0.9  # Convertir cucharadas a gramos (1 cucharada = 15 ml, densidad de brandy = 0.9 g/ml)
    vainilla_gramos = manteca_de_cacao * 0.005 * 4.2  # Convertir cucharaditas a gramos (1 cucharadita = 4.2 gramos)
    return cacao_en_polvo, azucar, brandy_gramos, vainilla_gramos

st.set_page_config(page_title="Calculadora de ingredientes para barra de chocolate amargo con brandy wawinense", page_icon=":chocolate_bar:")

st.title("Calculadora de ingredientes para barra de chocolate amargo con brandy")

manteca_de_cacao = st.number_input("Cantidad de manteca de cacao (en gramos)", min_value=0.0, step=1.0, value=150.0)

cacao_en_polvo, azucar, brandy_gramos, vainilla_gramos = calculate_ingredients(manteca_de_cacao)

data = {
    "Ingrediente": ["Manteca de cacao", "Cacao en polvo sin azúcar", "Azúcar de coco o de caña", "Brandy", "Extracto de vainilla"],
    "Cantidad": [manteca_de_cacao, cacao_en_polvo, azucar, brandy_gramos, vainilla_gramos],
    "Unidad": ["gramos", "gramos", "gramos", "gramos", "gramos"]
}

df = pd.DataFrame(data)

st.write(df)

csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="receta_chocolate_amargo.csv">Descargar receta</a>'
st.markdown(href, unsafe_allow_html=True)






