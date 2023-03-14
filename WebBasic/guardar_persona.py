
import mysql.connector
from flask import Flask, render_template, request

accion= request.form.get('accion')
print('Se recibe solicitud a la pagina guardar para: %s' % accion)
id= request.form.get('id')
fechanace = request.form.get('fechanace')
nombre = request.form.get('nombre')
apellido = request.form.get('apellido')
telefono = request.form.get('telefono')
correoe = request.form.get('correoe')
tipousuario = request.form.get('tipousuario')


# Conexión a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

    
# Función para insertar una persona en la tabla
def insertar_persona(id, fechanace, nombre, apellido, telefono, correoe, tipousuario):
    cursor = db.cursor()
    sql = "INSERT INTO personas (id, fechanace, nombre, apellido, telefono, correoe, tipousuario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (id, fechanace, nombre, apellido, telefono, correoe, tipousuario)
    cursor.execute(sql, val)
    db.commit()
    print("Persona insertada con éxito. ID: ", cursor.lastrowid)

# Función para actualizar una persona en la tabla
def actualizar_persona(id, fechanace, nombre, apellido, telefono, correoe, tipousuario):
    cursor = db.cursor()
    sql = "UPDATE personas SET fechanace = %s, nombre = %s, apellido = %s, telefono = %s, correoe = %s, tipousuario = %s WHERE id = %s"
    val = (fechanace, nombre, apellido, telefono, correoe, tipousuario, id)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "registros(s) actualizado(s)")

# Función para eliminar una persona de la tabla
def eliminar_persona(id):
    cursor = db.cursor()
    sql = "DELETE FROM personas WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "registro(s) eliminado(s)")

# Función para obtener todas las personas de la tabla
def obtener_personas():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM personas")
    personas = cursor.fetchall()
    return personas


if accion=='leer':
    print(obtener_personas())
elif accion=='actualizar':
    actualizar_persona(id, fechanace, nombre, apellido, telefono, correoe, tipousuario)
elif accion=='borrar':
    eliminar_persona(id)
else:
    insertar_persona(id, fechanace, nombre, apellido, telefono, correoe, tipousuario)

# Cierre de la conexión a la base de datos
db.close()

 

