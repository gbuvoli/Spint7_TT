import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

#El encabezado de la pagina
st.header('Mi primer dashboard en Streamlit')


#Crea un botón que, al hacer clic en él, construya un histograma

hist_button = st.button('Construir histograma') #Aquí se crea el boton

if hist_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir dispersión') #Aquí se crea el boton

if hist_button: # al hacer clic en el botón
         
     # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

