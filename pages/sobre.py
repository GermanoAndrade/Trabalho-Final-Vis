import streamlit as st


def app():
    col1, col2 = st.columns((4,1.5))
    with col1:
        st.title('Sobre')
        st.markdown("---")
    with col2:
        st.image("https://raw.githubusercontent.com/GermanoAndrade/AED-Listas/main/Lista%203/Quest%C3%B5es/Cap%C3%ADtulo%204/FGV-EMAp.png")

    st.markdown("""
    Breve descrição do trabalho
    """)

    st.markdown("[Repositório](https://github.com/GermanoAndrade/Visualizacao_da_Informacao/tree/main/Trabalho%204)")