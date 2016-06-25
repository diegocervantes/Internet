#!C:\Python27\python
# -*- coding: utf-8 -*-
import cgi
import cgitb; cgitb.enable()
import mysql.connector


print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inigo')

form = cgi.FieldStorage() 

nombre = form.getfirst('nombre', 'empty')

buscar=db.cursor()   
if (nombre != 'empty'): #imprime la búsqueda
    busqueda = "SELECT * FROM `empleados` WHERE `nombre` LIKE '%s' AND `area_id` = '%s' " % ("%"+nombre+"%",0) #este 0 lo cambiamos luego por el id del área en el que esté el login
    buscar.execute(busqueda)

else: #imprime todos
    busqueda = "SELECT * FROM `empleados` WHERE  `area_id` = '%s'" % (0) #este 0 lo cambiamos luego por el id del área en el que esté el login
    buscar.execute(busqueda)

resultado = buscar.fetchall()
print (""" <table class="t01" """)
print ("<tr><th>Codigo/Usuario</th><th>Nombre</th><th>DNI</th><th>Ingreso</th><th>Email</th><th>Telefono/Celular</th></tr>")
for r in resultado:
    print '<tr><td>',r[1],'</td><td>',r[3],'</td><td>',r[6],'</td><td>',r[7],'</td><td>',r[8],'</td><td>',r[10],'</td></tr>'
print("</table>")


buscar.close()   

db.close()
