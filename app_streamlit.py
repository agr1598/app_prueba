
import streamlit as st
import pandas as pd

# Estilo para fondo blanco
st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Cargar el archivo Excel
df = pd.read_excel("df.xlsx")

# Título de la app
st.title("Búsqueda por QName")

# Campo de búsqueda
search_input = st.text_input("Ingrese el QName a buscar:")

# Si se ingresa algún texto, se filtran los datos
if search_input:
    # Filtrar DataFrame sin distinguir mayúsculas/minúsculas
    filtered_df = df[df["QName"].str.contains(search_input, case=False, na=False)]
    st.write("Resultados de la búsqueda:")
    st.dataframe(filtered_df)
else:
    st.write("Ingrese un valor en el campo de búsqueda para ver resultados.")

