from altair.vegalite.v4.schema.channels import StrokeWidth, Tooltip
import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
from math import ceil
import requests

def app():

    # Título da página
    st.title('Heatmap')
    st.markdown("---")


    #fire = pd.read_csv('amazon.csv', encoding="ISO-8859-1", dtype={'number':str})
    #fire['number'] = fire['number'].apply(lambda x: x.replace(".", "")).astype(int)
    finished = pd.read_csv('./data/finished.csv')
    #est_abb = pd.read_csv('./data/cod_abb_estado.CSV', sep=';', encoding="ISO-8859-1")

    #estado_cod = {est_abb['Estado'][i]: est_abb['Código da UF'][i] for i in range(len(est_abb))}
    #estado_cod
    #finished['codigo'] = finished['estado'].apply(lambda x: str(estado_cod[x]))
    #cols = list(finished.columns)
    #finished = finished[cols[:2] + [cols[-1]] + cols[2:-1]].copy()

    #brasil_link = "https://raw.githubusercontent.com/fititnt/gis-dataset-brasil/master/uf/geojson/uf.json"
    #data_geojson_remote = alt.Data(url=brasil_link, format=alt.DataFormat(property='features',type='json'))

    #st.write(finished['incremento'][2556])
    #finished['incremento'][2556] = finished['incremento'][2556]/10
    #st.write(finished['incremento'][2556])

    metrics = { 'Queimada': ['n_incendios'], 
                'Precipitação': ['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)', 'Temperatura Média (°C)'], 
                'Desmatamento': ['desmatado']}
    #st.write(list(metrics.keys())[0])

    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    metric_option = st.radio("Selecione a métrica", list(metrics.keys()))

    with st.expander('Dataframe'):
        filtered_dataframe = finished[pd.notnull(finished[metrics[metric_option][0]])]
        chosen_state = st.selectbox("Selecione um estado", ['-', *filtered_dataframe['estado'].unique()])
        st.dataframe(filtered_dataframe[filtered_dataframe['estado'] == chosen_state ] if chosen_state != '-' else filtered_dataframe)
    

    #if metric_option == list(metrics.keys())[0]:


    #fire = finished[pd.notnull(finished['n_incendios'])]
    fire = finished[pd.notnull(finished[metrics[metric_option][0]])]
    #st.write(metrics[metric_option][1])
    #st.write(metric_option)
    if metric_option == "Precipitação":
        fire = fire[fire[metrics[metric_option][1]] >= 0]

    min_year = int(fire['ano'].min())
    max_year = int(fire['ano'].max())

    #st.markdown(f"min = {min_year}\nmax = {max_year}")                   

    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 
            'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    if metric_option == list(metrics.keys())[0]:
        mid = ceil((min_year+max_year)/2)
        value = st.slider("Selecione o intervalo de anos", min_year, max_year, value = (mid-2, mid+2),step=1)
    elif metric_option != list(metrics.keys())[2]:
        value = st.slider("Selecione o ano", min_year, max_year, value = ceil((min_year+max_year)/2),step=1)
        #st.write(value)

    def classes(x, max):
        if x <= (1/5)*max:
            return '1'
        elif x <= (2/5)*max:
            return '2'
        elif x <= (3/5)*max:
            return '3'
        elif x <= (4/5)*max:
            return '4'
        elif x <= max+1:
            return '5'

    if metric_option == list(metrics.keys())[1]:
        #precip_option = st.radio("Selecione a métrica", fire[])
        #st.write(fire.columns)
        col1, col2 = st.columns(2)
        with col1:

            plot = alt.Chart(fire[fire['ano'] == value], title=f"Precipitação - Ano de {value}").mark_rect().encode(
                    x=alt.X('mes:N', title='Mês', sort=[i.capitalize() for i in meses]),
                    y=alt.Y('estado:N', title="Estado"),
                    color=alt.Color(f'{metrics[metric_option][0]}:Q', legend=alt.Legend(title = "Precipitação Total (mm)", orient='top')),
                    #color='n_incendios:Q',
                tooltip=[alt.Tooltip(metrics[metric_option][1], title=metric_option), alt.Tooltip('estado', title='Estado'), alt.Tooltip('mes', title='Mês')]
                #tooltip=[alt.Tooltip('n_incendios', title='Queimadas'), alt.Tooltip('estado', title='Estado'), alt.Tooltip('mes', title='Mês')]
                ).properties(
                width=550,
                height=500
            )
            st.altair_chart(plot)
        with col2:

            plot = alt.Chart(fire[fire['ano'] == value], title=f"Temperatura Média - Ano de {value}").mark_rect().encode(
                    x=alt.X('mes:N', title='Mês', sort=[i.capitalize() for i in meses]),
                    y=alt.Y('estado:N', title="Estado"),
                    color=alt.Color(f'{metrics[metric_option][1]}:Q', legend=alt.Legend(orient='top'), sort='descending'),
                    #color='n_incendios:Q',
                tooltip=[alt.Tooltip(metrics[metric_option][1], title=metrics[metric_option][1]), alt.Tooltip('estado', title='Estado'), alt.Tooltip('mes', title='Mês')]
                #tooltip=[alt.Tooltip('n_incendios', title='Queimadas'), alt.Tooltip('estado', title='Estado'), alt.Tooltip('mes', title='Mês')]
                ).properties(
                width=550,
                height=500
            )
            st.altair_chart(plot)
    elif metric_option == list(metrics.keys())[2]:

        add_or_remove = st.radio("Selecione uma opção", ["Adicionar", "Remover"])
        a_r_dict = {"Adicionar": "Todos", "Remover": "Nenhum"}
        #cll1, cll2 = st.columns((3,2))  
        #with cll1:
        multiselect = st.multiselect(f"Selecione os estados para {add_or_remove.lower()}", options=[a_r_dict[add_or_remove], *fire['estado'].unique()], default=a_r_dict[add_or_remove])
        #with cll2:
           # multiselect_estado = st.multiselect(f"Selecione as regiões para {add_or_remove.lower()}", options=[a_r_dict[add_or_remove], *fire['region'].unique()], default=a_r_dict[add_or_remove])
        #st.write(multiselect)
        
        #state = st.selectbox("Selecione o Estado", ["-", *fire['estado'].unique()])
        #fire[fire['estado'] == state]
        #filter_fire = fire[fire['estado'] == state] if state != '-' else fire

        filter_option = fire['estado'].isin(multiselect) if add_or_remove == "Adicionar" else ~fire['estado'].isin(multiselect)

        filter_fire = fire[filter_option] if a_r_dict[add_or_remove] not in multiselect else fire
        selection = alt.selection_single()
        plot = alt.Chart(filter_fire).mark_line().encode(
            x=alt.X('ano:N', title='Mês'),
            y=alt.Y('incremento:Q', title="Desmatado"),
            color=alt.condition(selection, 'region:N', alt.value('grey')),
            strokeDash='estado',
            strokeWidth=alt.value(4),
            tooltip = [alt.Tooltip('incremento'), alt.Tooltip('ano'), alt.Tooltip('estado')]
        ).properties(
            width=1000,
            height=500
        ).add_selection(selection)
        st.altair_chart(plot)
    else:
        cll1, cll2, cll3 =  st.columns((0.5,5,1))
        with cll2:
            filteredd = fire[fire['ano'].isin(value)]
            filteredd['classes'] =filteredd['n_incendios'].apply(lambda x: classes(x, filteredd['n_incendios'].max()))
            #st.write(fire)
            plot = alt.Chart(filteredd, title=f"Anos de {value[0]} a {value[1]}").mark_rect().encode(
                    x=alt.X('mes:N', title='Mês', sort=[i.capitalize() for i in meses]),
                    y=alt.Y('estado:N', title="Estado"),
                    #color=alt.Color(f'{metrics[metric_option][0]}:Q', title='Quantidade de Incêndios',
                    color=alt.Color(f'classes:N', title='Quantidade de Incêndios', legend=alt.Legend(),
                    #legend=alt.Legend()
                    scale=alt.Scale(scheme='category10')),
                    #color='n_incendios:Q',
                tooltip=[alt.Tooltip(metrics[metric_option][0], title=metric_option), alt.Tooltip('estado', title='Estado'), 
                        alt.Tooltip('mes', title='Mês'), alt.Tooltip('classes', title='Classe')]
                #tooltip=[alt.Tooltip('n_incendios', title='Queimadas'), alt.Tooltip('estado', title='Estado'), alt.Tooltip('mes', title='Mês')]
                ).properties(
                width=900,
                height=600
            )
            st.altair_chart(plot)
        with cll3:
            st.info("Info")
            st.markdown(f"classe 1: $\leq$ {(1/5)*filteredd['n_incendios'].max()}")
            st.markdown(f"classe 2: $\leq$ {(2/5)*filteredd['n_incendios'].max()}")
            st.markdown(f"classe 3: $\leq$ {(3/5)*filteredd['n_incendios'].max()}")
            st.markdown(f"classe 4: $\leq$ {(4/5)*filteredd['n_incendios'].max()}")
            st.markdown(f"classe 5: $\leq$ {(5/5)*filteredd['n_incendios'].max()}")

            
        #st.write(fire)
        st.markdown("""
        ---

        ## Queimadas por ano""")
        plot = alt.Chart(fire, title="Queimadas por ano").mark_rect().encode(
                x=alt.X('mes:N', title='Mês', sort=[i.capitalize() for i in meses]),
                y=alt.Y('estado:N', title="Estado"),
                #color=alt.Color(f'{metrics[metric_option][0]}:Q', title='Quantidade de Incêndios',
                color=alt.Color(f'n_incendios:Q', title='Quantidade de Incêndios', legend=alt.Legend(),
                #legend=alt.Legend()
                #scale=alt.Scale(scheme='category10')),
                ),
                #color='n_incendios:Q',
            #tooltip=[alt.Tooltip(metrics[metric_option][0], title=metric_option), alt.Tooltip('estado', title='Estado'), 
                    # alt.Tooltip('mes', title='Mês'), alt.Tooltip('classes:N', title='Classe')]
            tooltip=[alt.Tooltip('n_incendios', title='Queimadas'), alt.Tooltip('estado', title='Estado'), alt.Tooltip('ano', title="Ano"), alt.Tooltip('mes', title='Mês')]
            ).properties(
                width=200,
                height=200).facet(
            facet=alt.Facet('ano:N', title="Queimadas por ano"),
            columns=4,
            #column = alt.Column("ano:N", title="None")
                #row = alt.Row("ano:N", title=None)
                ).configure_title(fontSize=24)
        st.altair_chart(plot)
        '''
        elif metric_option == list(metrics.keys())[1]:
            pass
        else:
            pass'''

        #"""
        #https://developer.nytimes.com/docs/articlesearch-product/1/overview
        API_KEY = 'jKimF0TPY7CbbKf1PxoIu6R3JB096zgj'
        #link = F'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=wildfires+maranhao&api-key={API_KEY}'
        #TODO: http://noticias.gov.br/noticias-api/documentacao.xhtml
        '''H = 0
        link = f'http://noticias.gov.br/noticias-api/noticias/busca?b=titulo:incendio%20titulo:maranhao&h={H}&wt=json'
        H_list = [["", ""],["<strong>", "</strong>"], ["<span style='background:yellow;'>", "</span>"]]
        request = requests.get(link)
        if request.json()["resultado"]["numeroNoticias"]:
            for i in request.json()["resultado"]["noticias"]["noticia"]:
                st.write(i.values())'''
                #with st.expander(i['titulo'].replace(2*H_list[H][0], "").replace(2*H_list[H][1], "").replace(H_list[H][0], "").replace(H_list[H][1], "")):
                   # st.markdown(f"[link]({i['link']})")
                    #st.image(i['link'])
                    #st.markdown(i["descricao"].replace(2*H_list[H][0], H_list[H][0]).replace(2*H_list[H][1], H_list[H][1]), unsafe_allow_html=True)
        #for i in request.content["resultado"]["noticias"]["noticia"]:
        #    st.markdown("---")
        #    st.write(i)
        #    st.markdown("---")
        #st.write(request.content)
        
        #"""

        print(fire.head())

    '''st.markdown("### Mapas")
    min_year = int(fire['ano'].min())
    max_year = int(fire['ano'].max())
    if metric_option != list(metrics.keys())[2]:
        value = st.slider("selecione o ano", min_year, max_year, value = ceil((min_year+max_year)/2),step=1)
        #st.write(value)'''

    