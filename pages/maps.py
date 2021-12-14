from altair.vegalite.v4.schema.channels import StrokeWidth, Tooltip
import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
from math import ceil
import requests


def app():
# Título da página
    st.title('Mapas')
    st.markdown("---")


    #fire = pd.read_csv('amazon.csv', encoding="ISO-8859-1", dtype={'number':str})
    #fire['number'] = fire['number'].apply(lambda x: x.replace(".", "")).astype(int)
    finished = pd.read_csv('./data/finished.csv')
    est_abb = pd.read_csv('./data/cod_abb_estado.CSV', sep=';', encoding="ISO-8859-1")

    estado_cod = {est_abb['Estado'][i]: est_abb['Código da UF'][i] for i in range(len(est_abb))}
    estado_cod
    finished['codigo'] = finished['estado'].apply(lambda x: str(estado_cod[x]))
    cols = list(finished.columns)
    finished = finished[cols[:2] + [cols[-1]] + cols[2:-1]].copy()

    brasil_link = "https://raw.githubusercontent.com/fititnt/gis-dataset-brasil/master/uf/geojson/uf.json"
    data_geojson_remote = alt.Data(url=brasil_link, format=alt.DataFormat(property='features',type='json'))

    metrics = { 'Queimada': ['n_incendios'], 
                'Precipitação': ['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)', 'Temperatura Média (°C)'], 
                'Desmatamento': ['desmatado']}
    #st.write(list(metrics.keys())[0])

    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    #metric_option = st.radio("Selecione a métrica", list(metrics.keys()))

    
    #st.write(metrics[metric_option][1])
    #st.write(metric_option)
    
    #if metric_option == "Precipitação":
        #fire = fire[fire[metrics[metric_option][1]] >= 0]

    

    #st.markdown(f"min = {min_year}\nmax = {max_year}")                   

    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 
            'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    #if metric_option != list(metrics.keys())[2]:
    
        #st.write(value)
    
    cols1, cols2 = st.columns(2)
    with cols1:
        first_map = st.radio("Primeiro mapa", list(metrics.keys()))
        fire = finished[pd.notnull(finished[metrics[first_map][0]])]
        #st.write(list(filter(lambda x: x != first_map, list(metrics.keys()))))

        with st.expander('Dataframe'):
            filtered_dataframe = finished[pd.notnull(finished[metrics[first_map][0]])]
            chosen_state = st.selectbox("Selecione um estado", ['-', *filtered_dataframe['estado'].unique()])
            st.dataframe(filtered_dataframe[filtered_dataframe['estado'] == chosen_state ] if chosen_state != '-' else filtered_dataframe)
    with cols2:
        second_map = st.radio("Segundo mapa", list(filter(lambda x: x != first_map, list(metrics.keys()))))
        fire1 = finished[pd.notnull(finished[metrics[second_map][0]])]

        with st.expander('Dataframe'):
            filtered_dataframe = finished[pd.notnull(finished[metrics[second_map][0]])]
            chosen_state = st.selectbox("Selecione um estado", ['-', *filtered_dataframe['estado'].unique()])
            st.dataframe(filtered_dataframe[filtered_dataframe['estado'] == chosen_state ] if chosen_state != '-' else filtered_dataframe)
    

    #if metric_option == list(metrics.keys())[0]:


    #fire = finished[pd.notnull(finished['n_incendios'])]
    

    min_year = int(fire['ano'].min())
    max_year = int(fire['ano'].max())
    cl1, cl2, cl3 = st.columns((0.5,5,0.5))
    with cl2:
        value = st.slider("Selecione o ano", min_year, max_year, value = ceil((min_year+max_year)/2),step=1)
    #st.write(second_map)

    filtered = lambda df, x: df[df['ano'] == value].groupby(['estado', 'codigo'], as_index=False)[x].sum()

    wildfires = fire[fire['ano'] == value].groupby(['estado', 'codigo'], as_index=False)['n_incendios'].sum()
    rain = fire[fire['ano'] == value].groupby(['estado', 'codigo'], as_index=False)['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'].sum()
    deforestation = fire[fire['ano'] == value].groupby(['estado', 'codigo'], as_index=False)['incremento'].sum()
    #TODO: adicionar subtipos quando escolher precipitação ou desmatamento (precipitação, temp. média, etc)
    chosen_df = {"Queimada": wildfires,
                 "Precipitação": rain,
                 "Desmatamento": deforestation}

    '''if metric_option == list(metrics.keys())[1]:
        pass
    elif metric_option == list(metrics.keys())[2]:
        pass
    else:'''
    col1, col2 = st.columns(2)
    with col1:
        
        plot = alt.Chart(data_geojson_remote, title=f"{first_map} no ano de {value}").mark_geoshape(
            stroke='lightgray'
        ).encode(
            color=alt.Color(f'{metrics[first_map][0]}:Q', title=f'Quantidade de {first_map}', 
            scale=alt.Scale(scheme='redblue', reverse=(first_map != "Precipitação")),
            legend=alt.Legend(orient='top')),
            tooltip = [alt.Tooltip("estado:N"), alt.Tooltip(f'{metrics[first_map][0]}:Q')]
        ).transform_lookup(
            lookup="properties.GEOCODIGO",
            from_=alt.LookupData(data=filtered(fire, metrics[first_map][0]), key="codigo", fields=['estado', metrics[first_map][0]])
        ).properties(
            width=500,
            height=500
        ).configure_view(
            strokeWidth=0
        )
        st.altair_chart(plot)

    with col2:
        #st.write(metrics[second_map][0])
        #st.write(chosen_df[second_map])
        plot2 = alt.Chart(data_geojson_remote, title=f"{second_map} no ano de {value}").mark_geoshape(
            stroke='lightgray'
        ).encode(
            color=alt.Color(f'{metrics[second_map][0]}:Q', title=f'Quantidade de {second_map}', 
            scale=alt.Scale(scheme='redblue', reverse=second_map != "Precipitação"),
            legend=alt.Legend(orient='top')),
            tooltip = [alt.Tooltip("estado:N"), alt.Tooltip(f'{metrics[second_map][0]}:Q')]
        ).transform_lookup(
            lookup="properties.GEOCODIGO",
            from_=alt.LookupData(data=filtered(fire1, metrics[second_map][0]), key="codigo", fields=['estado', metrics[second_map][0]])
        ).properties(
            width=500,
            height=500
        ).configure_view(
            strokeWidth=0
        )
        st.altair_chart(plot2)