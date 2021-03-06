import streamlit as st


def app():
    col1, col2 = st.columns((4,1.5))
    with col1:
        st.title('Sobre')
        st.markdown("---")
    with col2:
        st.image("https://raw.githubusercontent.com/GermanoAndrade/AED-Listas/main/Lista%203/Quest%C3%B5es/Cap%C3%ADtulo%204/FGV-EMAp.png")


    st.markdown("""[<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg" width="30px"> Repositório](https://github.com/GermanoAndrade/Trabalho-Final-Vis)"""
    ,unsafe_allow_html=True)


    with open('README.md', 'r', encoding='utf-8') as md:
        readme = md.read()

    st.markdown("\n")
    st.markdown(readme[16:], unsafe_allow_html=True)
    st.markdown("""
    ### Bases

Para esse trabalho, a partir da junção de dados de queimadas, dados meteorológicos e dados de desmatamento, foi
proposto a tentativa de analisar esses dados e suas relações por meio de visualizações interativas.  

Para isso, foram escolhidas as seguintes bases:

- [Forest Fires in Brazil](https://www.kaggle.com/gustavomodelli/forest-fires-in-brazil) 

<div align="center">
	<img src="https://raw.githubusercontent.com/GermanoAndrade/Trabalho-Final-Vis/main/img/fire_br.png", width="400px">
</div>

- [Climate Weather Surface of Brazil](https://www.kaggle.com/PROPPG-PPG/hourly-weather-surface-brazil-southeast-region?select=central_west.csv)

 
<div align="center">
	<img src="https://raw.githubusercontent.com/GermanoAndrade/Trabalho-Final-Vis/main/img/weather_n.png">
</div>


- [Desmatamento PRODES](https://basedosdados.org/dataset/b9528c5f-3b31-4383-9e60-51e34e6b9237)

 
<div align="center">
	<img src="https://raw.githubusercontent.com/GermanoAndrade/Trabalho-Final-Vis/main/img/desmatamento_br.png">
</div><br>


### Join das bases

Apesar de que todas as bases não contêm os dados de todos os estados para todos os meses dos mesmos anos,
foi possível juntar todas as bases aproveitando o máximo de dados que era possível manter em cada uma.

Após juntar todas as bases, o dataframe completo ficou com essa cara:

<div align="center">
	<img src="https://raw.githubusercontent.com/GermanoAndrade/Trabalho-Final-Vis/main/img/finished.png" width="1150px">
</div><br> 

### Ideias

A partir daí, com base na estrutura e nos dados do dataframe completo, a ideia foi construir visualizações de Heatmap e de Mapas também.  
<span style="font-size:16pt;font-variant-caps: petite-caps;"> Heatmaps </span>

<div align="center">
	<img src="https://raw.githubusercontent.com/GermanoAndrade/Trabalho-Final-Vis/main/img/Fernando_Hannaka_2020.png">
	<figcaption>Fernando Hannaka (2020)</figcaption>
</div>

<span style="font-size:16pt;font-variant-caps: petite-caps;"> Mapas </span>

<div align="center">
	<img src="https://raw.githubusercontent.com/GermanoAndrade/Trabalho-Final-Vis/main/img/exemplo_mapa.png" width="600px">
	<figcaption>Análise Geoespacial	</figcaption>
</div>




    """, unsafe_allow_html=True)