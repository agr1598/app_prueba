import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# ─── CONFIGURACIÓN DE PÁGINA ──────────────────────────────────────
st.set_page_config(
    page_title="Búsqueda por QName",
    layout="wide"
)

# ─── CARGA DE DATOS ────────────────────────────────────────────────
df = pd.read_excel("df.xlsx")

# ─── INTERFAZ ─────────────────────────────────────────────────────
st.title("Búsqueda por QName")
search_input = st.text_input("Ingrese el QName a buscar:")

if search_input:
    # Filtrado de coincidencia exacta (sin distinguir mayúsc./minúsc.)
    filtered_df = df[df["QName"].str.fullmatch(search_input, case=False, na=False)]

    st.write("Resultados de la búsqueda:")

    # ─── CONFIGURAR AGGRID ─────────────────────────────────────────
    gb = GridOptionsBuilder.from_dataframe(filtered_df)
    gb.configure_default_column(
        resizable=True,
        sortable=True,
        filter=True
    )
    # Ajustar todas las columnas al ancho del grid al cargar
    grid_options = gb.build()

    # Mostrar AgGrid
    AgGrid(
        filtered_df,
        gridOptions=grid_options,
        fit_columns_on_grid_load=True,
        height=600,
        width="100%"
    )

else:
    st.write("Ingrese un valor en el campo de búsqueda para ver resultados.")
