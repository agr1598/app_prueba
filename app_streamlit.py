import streamlit as st
import pandas as pd

# Estilo visual general
st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
        padding: 2rem;
    }
    h1 {
        text-align: center;
        color: #1a237e;
    }
    .big-input input {
        font-size: 18px !important;
        padding: 10px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Cargar el archivo Excel
df = pd.read_excel("df.xlsx")

# Título
st.markdown("<h1>🔍 Búsqueda por QName</h1>", unsafe_allow_html=True)

# Contenedor centrado para la búsqueda
with st.container():
    st.markdown("### Ingrese el QName a buscar:")
    search_input = st.text_input("", key="search", placeholder="Escriba aquí...", label_visibility="collapsed")

    # Botón para limpiar búsqueda
    if st.button("🔄 Limpiar búsqueda"):
        st.experimental_rerun()

    # Filtrado y resultados
    if search_input:
        filtered_df = df[df["QName"].str.contains(search_input, case=False, na=False)]
        st.markdown(f"#### Resultados encontrados: {len(filtered_df)}")

        if filtered_df.empty:
            st.warning("⚠️ No se encontraron coincidencias.")
        else:
            st.dataframe(filtered_df, use_container_width=True)
    else:
        st.info("ℹ️ Ingrese un valor en el campo de búsqueda para ver resultados.")
