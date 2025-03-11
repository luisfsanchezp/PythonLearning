import mysql.connector, csv, datetime, time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from fpdf import FPDF 



def OpenCnn():
     # Conexión a la base de datos MySQL
    cnn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pruebas"
    )
    return cnn

def CloseCnn(cnn):    
    # Cerrar la conexión
    cnn.close()
    
def ExportarAcsv():
    # Conexión a la base de datos MySQL
    db_connection = OpenCnn()

    # Obtener los datos de la persona
    query = "SELECT * FROM `personas` "
    df = pd.read_sql(query, db_connection)

    # Ver los primeros registros para asegurarnos de que todo esté bien
    print(df.head())

    # Análisis básico: contar los tipos de usuario
    '''
    id = df['id'].value_counts()
    fecnace = df['fechanace'].value_counts()
    nomre = df['nombre'].value_counts()
    apell = df['apellido'].value_counts()
    tel = df['telefono'].value_counts()
    correo = df['correoe'].value_counts()
    '''
    tiposusuario = df['tipousuario'].value_counts()


    # Mostrar los resultados de las respuestas

    print("Tipos de usuario:")
    print(tiposusuario)
    ''''
    # Visualizar los tipos de usuario
    plt.figure(figsize=(10, 6))

    # Respuestas pregunta 1
    plt.subplot(1, 3, 1)
    sns.barplot(x=tiposusuario.index, y=tiposusuario.values)
    plt.title("Cantidad por tipo de usuario")

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()
    '''

    # Exportar los resultados a un archivo CSV
    r=time.strftime("%Y%m%d_%H%M%S")
    df.to_csv("PythonLearning\WebBasic\Reports\Personas_"+"_"+r+".csv", index=False)
    
    # Cerrar la conexión
    CloseCnn(db_connection)

def ExportarAPDF():
     # Conexión a la base de datos MySQL
    db_connection = OpenCnn()

    # Obtener los datos de la persona
    query = "SELECT * FROM `personas` "
    df = pd.read_sql(query, db_connection)

    # Ver los primeros registros para asegurarnos de que todo esté bien
    print(df.head())

    # Análisis básico: contar los tipos de usuario
    tiposusuario = df['tipousuario'].value_counts()
    '''
    # Crear gráficos
    plt.figure(figsize=(10, 6))

    # Respuestas pregunta 1
    plt.subplot(1, 3, 1)
    sns.barplot(x=tiposusuario.index, y=tiposusuario.values)
    plt.title("Cantidad x Tipos de usuario")


    # Guardar los gráficos como imágenes
    plt.tight_layout()
    plt.savefig('.pdf', format='pdf')
    '''
    # Exportar PDF con texto (opcional)
    pdf = FPDF()
    pdf.add_page()

    # Título del reporte
    pdf.set_font("Arial", size=16, style='B')
    pdf.cell(200, 10, txt="Análisis de Datos de Empleados", ln=True, align='C')

    # Contar respuestas de las preguntas
    pdf.ln(10)  # Línea de separación
    pdf.set_font("Arial", size=12)

    # Agregar estadísticas de las personas por tipo
    pdf.cell(200, 10, txt=f"Tipos: {tiposusuario.to_dict()}", ln=True)

    # Guardar el archivo PDF
    r=time.strftime("%Y%m%d_%H%M%S")
    pdf.output("PythonLearning\WebBasic\Reports\Personas_"+"_"+r+".pdf")
  
    # Confirmación
    print("Los resultados han sido exportados a 'resultados_personas.pdf' y 'Personas_"+"_"+r+".pdf'")

    
    # Cerrar la conexión
    CloseCnn(db_connection)

