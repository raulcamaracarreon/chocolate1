import streamlit as st
import pandas as pd
import base64



def calculate_ingredients(manteca_de_cacao):
    cacao_en_polvo = manteca_de_cacao * 0.25
    azucar = manteca_de_cacao * 0.3
    brandy_gramos = manteca_de_cacao * 0.02 * 15 * 0.9  # Convertir cucharadas a gramos (1 cucharada = 15 ml, densidad de brandy = 0.9 g/ml)
    vainilla_gramos = manteca_de_cacao * 0.005 * 4.2  # Convertir cucharaditas a gramos (1 cucharadita = 4.2 gramos)
    return cacao_en_polvo, azucar, brandy_gramos, vainilla_gramos

st.set_page_config(page_title="Calculadora de ingredientes para barra de chocolate amargo con brandy", page_icon=":chocolate_bar:")

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

st.write("Instrucciones:")

st.write("1. Derrite la manteca de cacao en un baño María. Para hacer esto, coloca la manteca de cacao en un recipiente resistente al calor y colócalo sobre una olla con agua hirviendo. Revuelve la manteca de cacao hasta que se derrita completamente.")

st.write("2. Una vez que la manteca de cacao se haya derretido, agrega el cacao en polvo, el azúcar de coco o de caña y la pizca de sal. Revuelve hasta que los ingredientes se hayan mezclado completamente.")

st.write("3. Agrega el brandy y el extracto de vainilla a la mezcla de chocolate. Revuelve hasta que estén bien incorporados.")

st.write("4. Vierte la mezcla de chocolate en un molde para barras de chocolate. Si no tienes un molde para barras, puedes usar un molde de pan forrado con papel encerado.")

st.write("5. Refrigera la barra de chocolate durante al menos 30 minutos, o hasta que se haya endurecido por completo.")

st.write("6. Desmolda la barra de chocolate y córtala en porciones individuales. Sirve y disfruta de tu deliciosa barra de chocolate amargo con brandy.")





