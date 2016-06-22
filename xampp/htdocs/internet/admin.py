#!C:\Python27\python
# -*- coding: utf-8 -*-
import mihtml
import cgi
import cgitb; cgitb.enable()
import mysql.connector
import re



print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inigo')



t1 = ["Gestion de Areas","Gestion de empleados", "Cerrar Sesion"]
t2 = ["admin.py","admin2.py","inicio.py"]

mihtml.head("Admin")
mihtml.header()
mihtml.topbar()

print"""
<div class="contenido">
    <div class="subdivision">

        <div class="formulario-header">
            <p>Administrar Areas</p>
        </div>
        """
j=0
for i in t1:    
    print"""
        <p>
            <td><a href=" """,t2[j],""" " class="boton-admin">""",i,"""</a></td>
        </p>
        """
    j+=1

print"""
        </table>
    </div>
"""

print"""
    <div class="subdivision2">
        <div class="formulario-header">
            <p>Gestion de Areas</p>
        </div>
            <form action="admin.py" class="formulario-container" method="post" name="miform">
                <br>
                <p>      
                    <label class="formulario-text-grey">Usuario:</label>
                    <input class="formulario-input" type="text" name="usuario">
                </p>
                <p>      
                    <label class="formulario-text-grey">Password (Necesario letra mayuscula y dos signos):</label>
                    <input class="formulario-input" type="text" name="password">
                </p>
                <p>      
                    <label class="formulario-text-grey">Nombre de Area:</label>
                    <input class="formulario-input" style="resize:none" name="area"></input> 
                </p>
                <p>      
                    <label class="formulario-text-grey">Descripcion:</label>
                    <textarea class="formulario-input" maxlength="200" cols="20" rows="10" name="descripcion"></textarea> 
                </p>
                <p>      
                    <label class="formulario-text-grey">Jefe:</label>
                    <input class="formulario-input" style="resize:none" name="jefe"></input> 
                </p>
                <p>
                <input class="btn" type="submit" name="enviar" value="enviar">
                </p>

            </form>
"""
form = cgi.FieldStorage() 

usuario = form.getfirst('usuario', 'empty')
password = form.getfirst('password', 'empty')
area = form.getfirst('area', 'empty')
descripcion = form.getfirst('descripcion', 'empty')
jefe = form.getfirst('jefe', 'empty')

usuario = cgi.escape(usuario)
password = cgi.escape(password)
area = cgi.escape(area)
descripcion = cgi.escape(descripcion)
jefe = cgi.escape(jefe)

usuarioM = False
passwordM = False
areaM = False
descripcionM = False
jefeM = False

if( usuario != 'empty' and password != 'empty' and area != 'empty' and descripcion != 'empty' and jefe != 'empty'):
    if re.match("[A-Z]{3}-[0-9]{4}-[0-9]{2}",usuario):
        usuarioM = True

    if (re.search("[A-Z]+",password) and re.search("[\W]{2,}",password)):  
       passwordM = True

    if re.match("[a-zA-Z0-9\s]+",area):
       areaM = True  

    if re.match("[a-zA-Z0-9\s]+",descripcion):
       descripcionM = True   

    if re.match("[a-zA-Z\s]+",jefe):
       jefeM = True

    if (usuarioM and passwordM and areaM and descripcionM and jefeM):

        existe=db.cursor()
        existe.execute("SELECT * FROM `areas` WHERE `user` = '%s'" % (usuario))
        resultado = existe.fetchall()
        if(len(resultado) != 0):
            print("Ya hay un usuario registrado con el mismo ID")
        else:
            insertar=db.cursor()     
            valores = """INSERT INTO `areas` (`id`, `user`, `password`, `nombre_area`, `descripcion`, `jefe_area`) 
                        VALUES (NULL, '%s', '%s', '%s', '%s', '%s')""" % (usuario, password,area, descripcion, jefe)
            insertar.execute(valores)
            db.commit()   
            print ("ID de ultimo registro insertado: %s<br>" % insertar.lastrowid)
            insertar.close()
    else:
        if(not usuarioM):
            print "<p>Usuario Invalido</p>"
        if(not passwordM):
            print "<p>Password Invalido</p>"
        if(not areaM):
            print "<p>Area Invalido</p>"
        if(not descripcionM):
            print "<p>Descripcion Invalido</p>"
        if(not jefeM):
            print "<p>Jefe Invalido</p>"
else:
    print "<p>No ha ingresado algun campo</p>"
print"""
    </div>    
</div>
"""
mihtml.bottombar()