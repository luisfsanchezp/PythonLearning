# models/encuestas.py

from models.db import mysql

def crear_encuesta(persona_id, dimension_id, puntuacion):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO encuestas (persona_id, dimension_id, puntuacion)
        VALUES (%s, %s, %s)
    """, (persona_id, dimension_id, puntuacion))
    mysql.connection.commit()

def obtener_encuestas():
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT e.id, p.nombres, p.apellidos, d.nombre, e.puntuacion
        FROM encuestas e
        JOIN personas p ON e.persona_id = p.id
        JOIN dimensiones d ON e.dimension_id = d.id
    """)
    return cursor.fetchall()

def obtener_encuestas_por_persona(persona_id):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT e.id, d.nombre, e.puntuacion
        FROM encuestas e
        JOIN dimensiones d ON e.dimension_id = d.id
        WHERE e.persona_id = %s
    """, (persona_id,))
    return cursor.fetchall()

def obtener_encuestas_por_dimension(dimension_id):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT e.id, p.nombres, p.apellidos, e.puntuacion
        FROM encuestas e
        JOIN personas p ON e.persona_id = p.id
        WHERE e.dimension_id = %s
    """, (dimension_id,))
    return cursor.fetchall()
