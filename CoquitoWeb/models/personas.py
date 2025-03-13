# models/personas.py

from models.db import mysql

def crear_persona(documento, nombres, apellidos, correo):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO personas (documento, nombres, apellidos, correo_electronico)
        VALUES (%s, %s, %s, %s)
    """, (documento, nombres, apellidos, correo))
    mysql.connection.commit()
    return cursor.lastrowid

def obtener_persona(persona_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM personas WHERE id = %s", (persona_id,))
    return cursor.fetchone()

def obtener_personas():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM personas")
    return cursor.fetchall()

def actualizar_persona(persona_id, documento, nombres, apellidos, correo):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE personas
        SET documento = %s, nombres = %s, apellidos = %s, correo_electronico = %s
        WHERE id = %s
    """, (documento, nombres, apellidos, correo, persona_id))
    mysql.connection.commit()

def eliminar_persona(persona_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM personas WHERE id = %s", (persona_id,))
    mysql.connection.commit()
