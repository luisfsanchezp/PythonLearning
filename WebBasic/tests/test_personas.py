''''
    Vamos a probar las siguientes funciones:

    Conexión a la base de datos MySQL.
    Insertar datos en la base de datos.
    Realizar análisis estadísticos básicos sobre los datos.
    Comprobar la exportación de los resultados a CSV.'
    
'''
import pytest
import mysql.connector, time
import pandas as pd
import os
from io import StringIO

# Función de conexión a la base de datos
def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Usuario de la base de datos
        password="",  # Contraseña de la base de datos
        database="pruebas"  # Nombre de la base de datos
    )

# Función para insertar un registro en la base de datos
def insertar_persona(id, fechanace, nombre, apellido, telefono, correoe, tipousuario):
    conn = obtener_conexion()
    cursor = conn.cursor()
    query = "INSERT INTO personas (id, fechanace, nombre, apellido, telefono, correoe, tipousuario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (id, fechanace, nombre, apellido, telefono, correoe, tipousuario))
    conn.commit()
    cursor.close()
    conn.close()

# Función para leer los resultados de la base de datos
def obtener_resultados():
    conn = obtener_conexion()
    query = "SELECT * FROM personas"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Función para realizar un análisis básico
def obtener_descripcion(df):
    return df.describe()

# Pruebas

def test_conexion_db():
    """Test para comprobar la conexión a la base de datos."""
    try:
        conn = obtener_conexion()
        assert conn.is_connected()  # Si la conexión es exitosa
    except mysql.connector.Error as err:
        pytest.fail(f"Error de conexión: {err}")
    finally:
        conn.close()

def test_insertar_persona():
    """Test para comprobar la inserción de datos en la base de datos."""
    id = "90909090"
    fechanace="20/10/2003"
    nombre = "Juan"
    apellido = "Pérez"
    telefono ="300546467"
    correoe = "juan@example.com"
    tipousuario=2

    # Insertamos los datos
    insertar_persona(id, fechanace, nombre, apellido, telefono, correoe, tipousuario)

    # Comprobamos si los datos se insertaron correctamente
    df = obtener_resultados()
    assert df.shape[0] > 0  # Aseguramos que hay al menos una fila en los resultados
    assert any(df["id"] == id)  # Verificamos que el documento se insertó

def test_analisis_estadistico():
    """Test para verificar el análisis estadístico."""
    df = obtener_resultados()
    
    # Aseguramos que el análisis de la descripción funcione
    descripcion = obtener_descripcion(df)
    assert descripcion is not None
    assert "id" in descripcion.columns  # Verificamos que la columna 'id' esté en la descripción
    assert "fechanace" in descripcion.columns  # Verificamos que la columna 'fechanace' esté en la descripción
    assert "nombre" in descripcion.columns  # Verificamos que la columna 'nombre' esté en la descripción
    assert "apellido" in descripcion.columns  # Verificamos que la columna 'apellido' esté en la descripción
    assert "telefono" in descripcion.columns  # Verificamos que la columna 'telefono' esté en la descripción
    assert "correoe" in descripcion.columns  # Verificamos que la columna 'correoe' esté en la descripción
    assert "tipousuario" in descripcion.columns  # Verificamos que la columna 'tipousuario' esté en la descripción

def test_exportar_a_csv():
    """Test para verificar la exportación de los resultados a CSV."""
    df = obtener_resultados()
    
    # Guardamos el DataFrame en un archivo CSV temporal
    r=time.strftime("%Y%m%d_%H%M%S")
    archivo_csv = "resultados_personas_test_"+"_"+r+".csv"
    df.to_csv(archivo_csv, index=False)
    
    # Verificamos si el archivo CSV fue creado
    assert os.path.exists(archivo_csv)
    
    # Limpiamos el archivo después de la prueba
    os.remove(archivo_csv)

# Ejecutar las pruebas
if __name__ == "__main__":
    pytest.main()
