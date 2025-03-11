'''Este archivo incluye:

    Conexión a la base de datos: Para obtener los datos de la tabla personas y las respuestas a la encuesta.
    Análisis básico de los datos: Descripción y estadísticas de los datos de los empleados.
    Gráfico Radial: Mostrar las respuestas de la rueda de la vida para cada usuario.
    Otras métricas: Por ejemplo, promedio de satisfacción de los empleados, análisis de tendencias, etc.'''

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime

# Configurar estilo de gráficos
sns.set_theme(style="whitegrid")

# Conexión a la base de datos MySQL
def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Usuario de la base de datos
        password="",  # Contraseña de la base de datos
        database="pruebas"  # Nombre de la base de datos
    )

# Función para obtener los datos de las personas
def obtener_personas():
    conn = obtener_conexion()
    query = "SELECT * FROM personas"
    df_personas = pd.read_sql(query, conn)
    conn.close()
    return df_personas

# Función para obtener las respuestas de la encuesta
def obtener_encuestas():
    conn = obtener_conexion()
    query = "SELECT * FROM encuesta"
    df_encuestas = pd.read_sql(query, conn)
    conn.close()
    return df_encuestas

# Función para realizar análisis descriptivo básico de los datos de personas
def analisis_personas(df):
    descripcion = df.describe(include="all")
    print("Descripción de los datos de personas:")
    print(descripcion)
    
# Función para realizar análisis de las respuestas de la encuesta
def analisis_encuesta(df_encuestas):
    print("\nAnálisis de las respuestas de la encuesta:")
    # Calcular estadísticas básicas
    encuesta_promedio = df_encuestas.mean(axis=1)
    print(f"Promedio de respuestas por encuesta:\n{encuesta_promedio.head()}")
    
    # Descripción de las respuestas
    encuesta_descripcion = df_encuestas.describe()
    print(f"\nDescripción de las respuestas de la encuesta:\n{encuesta_descripcion}")

# Función para graficar la satisfacción de los empleados con un gráfico radial (spider plot)
def graficar_satisfaccion(df_encuestas, id_persona):
    # Filtrar las respuestas de la persona
    respuestas = df_encuestas[df_encuestas['id_persona'] == id_persona].iloc[:, 2:].values.flatten()

    # Etiquetas de las dimensiones de la rueda de la vida (preguntas)
    dimensiones = ['Emocional', 'Físico', 'Relacional', 'Espiritual', 'Financiero', 'Familiar', 'Profesional', 'Social', 'Crecimiento', 'Diversión']

    # Configuración del gráfico radial
    num_vars = len(dimensiones)

    # Ángulos para las dimensiones
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Cerramos el gráfico
    respuestas = np.concatenate((respuestas, [respuestas[0]]))
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, respuestas, color='b', alpha=0.25)
    ax.plot(angles, respuestas, color='b', linewidth=2)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dimensiones, fontsize=10, fontweight='bold')

    plt.title(f"Satisfacción de la persona {id_persona}", size=14)
    plt.show()

# Función para obtener el promedio de las respuestas de la rueda de la vida por cada persona
def obtener_promedio_respuestas(df_encuestas):
    # Calcular el promedio de cada pregunta
    promedios = df_encuestas.iloc[:, 2:].mean()
    print("\nPromedio de las respuestas por cada dimensión de la rueda de la vida:")
    print(promedios)

# Función principal para ejecutar los análisis
def ejecutar_analitica():
    # Obtener datos
    df_personas = obtener_personas()
    df_encuestas = obtener_encuestas()

    # Análisis de los datos de personas
    analisis_personas(df_personas)

    # Análisis de las respuestas de la encuesta
    analisis_encuesta(df_encuestas)

    # Obtener el promedio de respuestas para la rueda de la vida
    obtener_promedio_respuestas(df_encuestas)

    # Graficar la satisfacción de un empleado (por ejemplo, el que tiene id_persona == 1)
    graficar_satisfaccion(df_encuestas, id_persona=1)

  
