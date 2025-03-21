
from flask import Flask, render_template, request
import mysql.connector, csv, datetime, time
import datascience
import analitica, basura



app = Flask (__name__)

@app.route('/')
def principal():
        return render_template('index.html')

@app.route('/nosotros')
def nostoros():
        return render_template('nosotros.html')

@app.route('/contacto')
def contacto():
        return render_template('contacto.html')


@app.route('/persona')
def persona():
        return render_template('persona.html')


@app.route('/analitica')
def analitics():
    basura.procesar()
   # analitica.ejecutar_analitica()
    return render_template('analitica.html')


@app.route('/guardar_p', methods=['GET','POST'])
def guardar_p(): 
        resultado=''           
        accion= request.form.get('accion')
        id= request.form.get('id')
        fechanace = request.form.get('fechanace')
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        telefono = request.form.get('telefono')
        correoe = request.form.get('correoe')
        tipousuario = request.form.get('tipousuario')
        try:
                # Conexión a la base de datos
                db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pruebas"
                )
        except:
             return "No existe conección a la base de datos, verifica que el servidor esté activo y tus datos sean correctos."



            
        # Función para insertar una persona en la tabla
        def insertar_persona(id, fechanace, nombre, apellido, telefono, correoe, tipousuario):
            cursor = db.cursor()
            sql = "INSERT INTO personas (id, fechanace, nombre, apellido, telefono, correoe, tipousuario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (id, fechanace, nombre, apellido, telefono, correoe, tipousuario)
            cursor.execute(sql, val)
            db.commit()
            return "Persona insertada con éxito. ID: "+ str(cursor.lastrowid)
#            print("Persona insertada con éxito. ID: ", cursor.lastrowid)

        # Función para actualizar una persona en la tabla
        def actualizar_persona(fechanace, nombre, apellido, telefono, correoe, tipousuario, id):
            cursor = db.cursor()
            sql = "UPDATE personas SET fechanace = %s, nombre = %s, apellido = %s, telefono = %s, correoe = %s, tipousuario = %s WHERE id = %s"
            val = (fechanace, nombre, apellido, telefono, correoe, tipousuario, id)
            cursor.execute(sql, val)
            db.commit()
            return str(cursor.rowcount)+ " registros(s) actualizado(s)"
 #           print(cursor.rowcount, "registros(s) actualizado(s)")

        # Función para eliminar una persona de la tabla
        def eliminar_persona(id):
            cursor = db.cursor()
            sql = "DELETE FROM personas WHERE id = %s"
            val = (id,)
            cursor.execute(sql, val)
            db.commit()
            return str(cursor.rowcount), " registro(s) eliminado(s)"
  #          print(cursor.rowcount, "registro(s) eliminado(s)")

        # Función para obtener todas las personas de la tabla
        def obtener_personas():
            cursor = db.cursor()
            cursor.execute("SELECT * FROM personas") #WHERE id LIKE ='"+id+"';"
            personas = cursor.fetchall()  
            res = "<table style='border=1;'>"
            for x in personas:
                res += "<tr><td>"+ str(x[0])+ "</td>"
                res += "<td>"+ str(x[1])+ "</td>"
                res += "<td>"+ str(x[2])+ "</td>"
                res += "<td>"+ str(x[3])+ "</td>"
                res += "<td>"+ str(x[4])+ "</td>"
                res += "<td>"+ str(x[5])+ "</td>"
                res += "<td>"+ str(x[6])+ "</td></tr>"
            res += "</table>"  
            db.commit()
            return res
    
        # Función para exportar a un archivo de texto los datos de la tabla
        def exportarTxt(): 
            cursor = db.cursor()
            cursor.execute("SELECT * FROM personas") 
            datos = cursor.fetchall() 

            d=" ".join(str(row) for row in datos)
            f=datetime.date.today().isoformat()  
            r=time.strftime("%Y%m%d_%H%M%S")
            archivo = open("PythonLearning\WebBasic\Reports\Personas_"+"_"+r+".txt", "w")
            
            archivo.write(d)
            archivo.close()

            db.commit()
            return "Se exportaron los datos TXT a la ruta especificada.[>>Reports]"
        
        # Función para a
        def exportarCsv():
            
            cursor = db.cursor()
            cursor.execute("SELECT * FROM personas") 
            datos = cursor.fetchall() 

            d=" ".join(str(row) for row in datos)
            f=datetime.date.today().isoformat()  
            r=time.strftime("%Y%m%d_%H%M%S")
            archivo = open("PythonLearning\WebBasic\Reports\Personas_"+"_"+r+".csv", "w")
            
            archivo.write(d)
            archivo.close()

            db.commit()
            return "Se exportaron los datos CSV a la ruta especificada.[>>Reports]"
             # datascience.ExportarAcsv() 


        def exportarPdf():
            
            cursor = db.cursor()
            cursor.execute("SELECT * FROM personas") 
            datos = cursor.fetchall() 

            d=" ".join(str(row) for row in datos)
            f=datetime.date.today().isoformat()  
            r=time.strftime("%Y%m%d_%H%M%S")
            archivo = open("PythonLearning\WebBasic\Reports\Personas_"+"_"+r+".pdf", "w")
            
            archivo.write(d)
            archivo.close()

            db.commit()
            return "Se exportaron los datos PDF a la ruta especificada.[>>Reports]"
             # datascience.ExportarAPDF()
        
    ##TO DO: 

    #a partir de mgmanager.py generar las funciones para gestion de los datos. 
    # 
    # 
    # 



        if accion=='Leer':                          
            resultado= obtener_personas()
        elif accion=='Editar':
              resultado= actualizar_persona(fechanace, nombre, apellido, telefono, correoe, tipousuario, id)
        elif accion=='Borrar':
              resultado= eliminar_persona(id)              
        elif accion=='Exportartxt':                          
              resultado=  exportarTxt()                     
        elif accion=='Exportarcsv':                          
              resultado= exportarCsv                   
        elif accion=='Exportarpdf':                          
              resultado=  exportarPdf()                           
        elif accion=='Analizar':                          
              resultado = analitics()
        else:
              resultado= insertar_persona(id, fechanace, nombre, apellido, telefono, correoe, tipousuario)
        # Cierre de la conexión a la base de datos
        db.close()
        return resultado



if __name__ == '__main__':
    app.run(debug=True, port=5080)

