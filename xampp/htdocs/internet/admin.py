#!C:\Python27\python
#!/usr/bin/python

import mihtml
import cgi
import cgitb; cgitb.enable()
import mysql.connector
import re


print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inigo')



t1 = ["Agregar Area","Quitar Area", "Cerrar Sesion"]
t2 = ["Agregar Empleado", "Quitar Empleado", "Ver Empleado"]
t3 = ["Area","Id","Encargado"]

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
for i in t1:
    print"""
        <p>
            <td><a href="#" class="boton-admin">""",i,"""</a></td>
        </p>
        """
print"""
        </table>
    </div>
"""

print"""
    <div class="subdivision2">
        <div class="formulario-header">
            <p>Input Form</p>
        </div>
            <form class="formulario-container">
                <br>
                <p>      
                    <label class="formulario-text-grey">Nombre:</label>
                    <input class="formulario-input" type="text" required="">
                </p>
                <p>      
                    <label class="formulario-text-grey">Contrasena (Necesario letra mayuscula y dos signos):</label>
                    <input class="formulario-input" type="text" required="">
                </p>
                <p>      
                    <label class="formulario-text-grey">Fecha de Nacimineto (yyyy-mm-dd):</label>
                    <input class="formulario-input" style="resize:none"></input> 
                </p>
                <p>
                <button class="btn" type="button">Enviar</button>
                </p>

            </form>
    </div>    
</div>
""" #si quieres poner textarea solo lo reemplazas por el input osea <textarea>balblaablab</textarea>
mihtml.bottombar()