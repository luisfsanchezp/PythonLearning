# app.py

from flask import Flask, render_template, request, redirect, url_for
from models.db import init_db, mysql
from models.personas import crear_persona, obtener_persona
from models.encuestas import crear_encuesta, obtener_encuestas, obtener_encuestas_por_dimension
from models.dimensiones import obtener_dimensiones

import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'

# Inicializar base de datos
init_db(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encuesta', methods=['GET', 'POST'])
def encuesta():
    if request.method == 'POST':
        documento = request.form['documento']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        correo = request.form['correo']

        # Crear la persona en la base de datos
        persona_id = crear_persona(documento, nombres, apellidos, correo)

        # Guardar respuestas de la encuesta
        for dimension_id in request.form.getlist('dimension_id'):
            puntuacion = request.form.get(f'puntuacion_{dimension_id}')
            crear_encuesta(persona_id, dimension_id, puntuacion)

        return redirect(url_for('index'))

    # Obtener las dimensiones
    dimensiones = obtener_dimensiones()
    return render_template('encuesta.html', dimensiones=dimensiones)



@app.route('/reporte')
def reporte():
    # Obtener las encuestas y calcular la satisfacción promedio por dimensión
    encuestas = obtener_encuestas()
    
    # Consultas para obtener las encuestas por dimensión
    resultados_por_dimension = {}
    dimensiones = obtener_dimensiones()

    for dim in dimensiones:
        dimension_id = dim[0]
        encuestas_dimension = obtener_encuestas_por_dimension(dimension_id)
        puntuacion_promedio = sum([encuesta[3] for encuesta in encuestas_dimension]) / len(encuestas_dimension) if encuestas_dimension else 0
        resultados_por_dimension[dim[1]] = puntuacion_promedio

    # Crear un gráfico interactivo con Plotly
    df = pd.DataFrame(list(resultados_por_dimension.items()), columns=['Dimensión', 'Promedio'])
    fig = px.bar(df, x='Dimensión', y='Promedio', title="Promedio de Satisfacción por Dimensión")
    graph_html = fig.to_html(full_html=False)

    # Crear un gráfico con Matplotlib y convertirlo en imagen
    fig_matplotlib = plt.figure(figsize=(8, 6))
    plt.bar(resultados_por_dimension.keys(), resultados_por_dimension.values())
    plt.xlabel('Dimensión')
    plt.ylabel('Promedio de Satisfacción')
    plt.title('Promedio de Satisfacción por Dimensión')

    # Guardamos la imagen en un buffer en memoria
    img_stream = io.BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)
    img_base64 = base64.b64encode(img_stream.getvalue()).decode('utf-8')

    
    # Crear un gráfico interactivo con Plotly
    df2 = pd.DataFrame(list(resultados_por_dimension.items()), columns=['Dimensión', 'Promedio'])
    fig2 = px.bar_polar(df2, r='Dimensión', hover_name="Promedio")
    graph_html2 = fig2.to_html(full_html=False)


    return render_template('reporte.html', resultados_por_dimension=resultados_por_dimension, graph_html=graph_html, img_base64=img_base64,graph_html2=graph_html2 )




if __name__ == '__main__':
    app.run(debug=True)
