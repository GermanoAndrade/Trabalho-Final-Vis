# Trabalho Final

link da aplicação: https://final-proj-vis.herokuapp.com/


### Bases

Para esse trabalho, a partir da junção de dados de queimadas, dados meteorológicos e dados de desmatamento, foi
proposto a tentativa de analisar esses dados e suas relações por meio de visualizações interativas.  

Para isso, foram escolhidas as seguintes bases:


- [`Forest Fires in Brazil`](https://www.kaggle.com/gustavomodelli/forest-fires-in-brazil) 

<div align="center">
	<img src="https://raw.githubusercontent.com/GermanoAndrade/Trabalho-Final-Vis/main/img/fire_br.png", width="400px">
</div>

- [`Climate Weather Surface of Brazil`](https://www.kaggle.com/PROPPG-PPG/hourly-weather-surface-brazil-southeast-region?select=central_west.csv)

 
<div align="center">
	<img src="https://raw.githubusercontent.com/GermanoAndrade/Trabalho-Final-Vis/main/img/weather_n.png">
</div>


- [`Desmatamento PRODES`](https://basedosdados.org/dataset/b9528c5f-3b31-4383-9e60-51e34e6b9237)

 
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

## Aplicação

A aplicação, que pode ser acessada através desse [link](https://final-proj-vis.herokuapp.com/), tem a finalidade de apresentar os resultados 
gráficos produzidos.

### Menu

Através do seu menu, é possível navegar entre as páginas disponíveis.
<div align="center">
	<img src="/img/menu_app.png" width="250px">
</div>

### Heatmap

Na página de heatmap, é possível encontrar as seguintes visualizações

<div align="center">
	<img src="/img/heatmap_queimada.png">
</div>

<div align="center">
	<img src="/img/queimadas_por_ano.png">
</div>


<div align="center">
	<img src="/img/precipitacao.png">
</div>


<div align="center">
	<img src="/img/desmatamento.png">
</div>

### Mapa

Na página mapa, é possível comparar os mapas segundo as métricas desejadas.


<div align="center">
	<img src="/img/mapas.png">
</div>









