# models/dimensiones.py

from models.db import mysql

def obtener_dimensiones():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM dimensiones")
    return cursor.fetchall()

def obtener_dimension(dimension_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM dimensiones WHERE id = %s", (dimension_id,))
    return cursor.fetchone()

def crear_dimension(nombre, descripcion):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO dimensiones (nombre, descripcion)
        VALUES (%s, %s)
    """, (nombre, descripcion))
    mysql.connection.commit()
    return cursor.lastrowid
