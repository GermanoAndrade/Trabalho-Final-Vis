import streamlit as st
from pages import sobre, heatmaps, maps

st.set_page_config(page_title= 'Final Vis | EMAp - FGV', 
                   page_icon="https://raw.githubusercontent.com/GermanoAndrade/AED-Listas/main/Lista%203/Quest%C3%B5es/Cap%C3%ADtulo%204/FGV-EMAp.png", 
                   layout="wide",# 'centered' or 'wide'
                   initial_sidebar_state="collapsed",# 'auto', 'expanded' or 'collapsed'
                   )

#st.markdown(""" <style>
#MainMenu {visibility: hidden;}
#</style> """, unsafe_allow_html=True)

st.markdown(""" <style>
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


PAGES = {'Sobre': sobre,
         'Heatmap': heatmaps,
         'Mapa': maps}

st.sidebar.image("img/FGV-EMAp.png", width=250,output_format='png')
st.sidebar.header("Queimadas, Precipitação e Desmatamento")
st.sidebar.markdown("Visualização da Informação - 2021.2 | EMAp - FGV")
st.write('<style>div.row-widget.stRadio > div{flex-direction:column;}</style>', unsafe_allow_html=True)
option = st.sidebar.radio('Ir para:', options=list(PAGES.keys()), index=1)
page = PAGES[option]
st.sidebar.markdown("""
---

Germano Andrade | Dezembro, 2021  
[<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg" width="30px"> Github](https://github.com/GermanoAndrade/)

""", unsafe_allow_html=True)
page.app()

