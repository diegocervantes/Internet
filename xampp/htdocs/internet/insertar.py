#!C:\Python27\python

import cgi
import cgitb; cgitb.enable()
import mysql.connector

print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inigo')

form = cgi.FieldStorage() 

usuario = form.getfirst('usuario', 'empty')
password = form.getfirst('password', 'empty')
existe=db.cursor()

existe.execute("SELECT * FROM `admin` WHERE `user` = '%s'" % (usuario))
resultado = existe.fetchall()
existe.execute("SELECT * FROM `admin` WHERE `password` = '%s'" % (password))
resultado2 = existe.fetchall()


if(len(resultado) != 0 and len(resultado2) != 0):
  print ("Login ADMIN")
  print ("""<meta http-equiv="refresh" content="0;url=http://localhost/internet/admin.py">""")
else:
	existe.execute("SELECT * FROM `areas` WHERE `user` = '%s'" % (usuario))
	resultado = existe.fetchall()
	existe.execute("SELECT * FROM `areas` WHERE `password` = '%s'" % (password))
	resultado2 = existe.fetchall()
	if(len(resultado) != 0 and len(resultado2) != 0):
		print resultado[0][0]
		print ("Login JEFE DE AREA")
		print ("""<meta http-equiv="refresh" content="0;url=http://localhost/internet/asistencias.py">""")
	else:
		existe.execute("SELECT * FROM `empleados` WHERE `user` = '%s'" % (usuario))
		resultado = existe.fetchall()
		existe.execute("SELECT * FROM `empleados` WHERE `password` = '%s'" % (password))
		resultado2 = existe.fetchall()
		if(len(resultado) != 0 and len(resultado2) != 0):
			print ("Login EMPLEADO")
			print ("""<meta http-equiv="refresh" content="0;url=http://localhost/internet/inicio.py">""")
		else:
			print ("Datos incorrectos")
existe.close()
