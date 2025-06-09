import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

#El encabezado de la pagina
st.header('Mi primer dashboard en Streamlit')

#Crea un botón que, al hacer clic en él, construya un histograma

hist_checkbox = st.checkbox('Construir histograma', value=False, label_visibility='visible', help='Despliega de manera general la cantidad de kilómetros recorridos de nuestros vehículos') #Aquí se crea el boton

if hist_checkbox: # al hacer clic en el botón
        
         # crear un histograma
         fig = px.histogram(car_data, x="odometer")

         fig.update_layout(title= "Distribución de Km recorridos por los vehículos disponibles",
                  xaxis_title="Kilómetros recorridos",
                  yaxis_title= "Cantidad/frecuencia")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir dispersión', help='Muestra la relación entre los kilómetros recorridos y el precio del vehículo') #Aquí se crea el boton

if scatter_button: # al hacer clic en el botón

    st.markdown("💡 **Tip:** puedes hacer *doble clic* en una categoría de la leyenda para enfocarte solo en esa.")
         
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price",
                     color= "condition" ,hover_name='model',
                     hover_data=["model_year", "transmission", "fuel"],
                     opacity=0.5)# crear un gráfico de dispersión
    fig.update_layout(
    xaxis=dict(range=[0, 500000]),  # Zoom fijo en el eje X
    yaxis=dict(range=[0, 90000]),    # Zoom fijo en el eje Y
    legend_itemclick="toggle",
    legend_itemdoubleclick="toggleothers"
    )

     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
