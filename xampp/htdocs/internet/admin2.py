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
            <p>Gestion de  Empleados</p>
        </div>
            <form action="admin2.py" class="formulario-container" method="post" name="miform">
                <br>
                <p>      
                    <label class="formulario-text-grey">Usuario/Codigo:</label>
                    <input class="formulario-input" type="text" name="usuario">
                </p>
                <p>      
                    <label class="formulario-text-grey">Nombre:</label>
                    <input class="formulario-input" type="text" name="nombre">
                </p>
                <p>      
                    <label class="formulario-text-grey">Password:</label>
                    <input class="formulario-input" style="resize:none" name="password"></input> 
                </p>
                <p>      
                    <label class="formulario-text-grey">Fecha de Nacimiento:</label>
                    <input class="formulario-input" style="resize:none" name="nacimiento"></input> 
                </p>
                <p>      
                    <label class="formulario-text-grey">DNI:</label>
                    <input class="formulario-input" style="resize:none" name="dni"></input> 
                </p>
                <p>      
                    <label class="formulario-text-grey">Ingreso:</label>
                    <input class="formulario-input" style="resize:none" name="ingreso"></input> 
                </p>
                <p>      
                    <label class="formulario-text-grey">Email:</label>
                    <input class="formulario-input" style="resize:none" name="email"></input> 
                </p>
                <p>      
                    <label class="formulario-text-grey">Telefono:</label>
                    <input class="formulario-input" style="resize:none" name="telefono"></input> 
                </p>
                <p>      
                    <label class="formulario-text-grey">Celular:</label>
                    <input class="formulario-input" style="resize:none" name="celular"></input> 
                </p>
                <p>
                <input class="btn" type="submit" name="enviar" value="enviar">
                </p>

            </form>
"""
form = cgi.FieldStorage() 

usuario = form.getfirst('usuario', 'empty')
nombre = form.getfirst('nombre', 'empty')
password = form.getfirst('password', 'empty')
nacimiento = form.getfirst('nacimiento', 'empty')
dni = form.getfirst('dni', 'empty')
ingreso = form.getfirst('ingreso', 'empty')
email = form.getfirst('email', 'empty')
telefono = form.getfirst('telefono', 'empty')
celular = form.getfirst('celular', 'empty')

usuario = cgi.escape(usuario)
nombre = cgi.escape(nombre)
password = cgi.escape(password)
nacimiento = cgi.escape(nacimiento)
dni = cgi.escape(dni)
ingreso = cgi.escape(ingreso)
email = cgi.escape(email)
telefono = cgi.escape(telefono)
celular = cgi.escape(celular)

usuarioM = False
nombreM = False
passwordM = False
nacimientoM = False
dniM = False
ingresoM = False
emailM = False
telefonoM = False
celularM = False


if( usuario != 'empty' and nombre != 'empty' and password != 'empty' and nacimiento != 'empty' and dni != 'empty' 
    and ingreso != 'empty' and email != 'empty' and telefono != 'empty' and celular != 'empty'):
    if re.match("[A-Z]{3}-[0-9]{5}-[0-9]{4}-[0-9]{2}",usuario):
        usuarioM = True

    if re.match("[a-zA-Z\s]+",nombre):
        nombreM = True

    if (re.search("[A-Z]+",password) and re.search("[\W]{2,}",password)):
        passwordM = True

    if re.match("[0-9]{4}-[0-9]{2}-[0-9]{2}",nacimiento):
       nacimientoM = True  

    if re.match("[0-9]{8}",dni):
       dniM = True  

    if re.match("[0-9]{4}",ingreso):
       ingresoM = True

    if re.match(".+[\@][a-z]+[\.a-z]+",email):
       emailM = True

    if re.match("[0-9\-]{6,}",telefono):
        telefonoM = True
        ## Para convertir de numero con guiones a numero
        r = ""
        for i in telefono:
            if(i != '-'):
                r = str(r) + str(i)
        telefono = int(r)
       

    if re.match("[0-9\-]{9,}",celular):
        celularM = True 
        print"Celular: SI</br>"
        r = ""
        for i in celular:
            if(i != '-'):
                r = str(r) + str(i)
        celular = int(r)
       

    if(usuarioM and nombreM and passwordM and nacimientoM and dniM and ingresoM and emailM and telefonoM and celularM):
        existe=db.cursor()
        existe.execute("SELECT * FROM `empleados` WHERE `codigo` = '%s'" % (usuario)) #usuario = codigo
        resultado = existe.fetchall()
        if(len(resultado) != 0):
            print("Ya hay un usuario registrado con el mismo codigo")
        else:
            insertar=db.cursor()     
            valores =("""INSERT INTO `empleados` (`id`, `codigo`, `user`, `nombre`, `password`, `fecha_nacimiento`, 
                        `dni`, `ingreso`, `email`, `telefono`, `celular`) 
                        VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % 
                        (usuario, usuario, nombre, password, nacimiento, dni, ingreso, email, telefono, celular))
            insertar.execute(valores)
            db.commit()   
            print ("ID de ultimo registro insertado: %s<br>" % insertar.lastrowid)
            insertar.close()
    else:
        if(not usuarioM):
            print "<p>Usuario Invalido</p>"
        if(not nombreM):
            print "<p>Nombre Invalido</p>"
        if(not passwordM):
            print "<p>Password Invalido</p>"
        if(not nacimientoM):
            print "<p>Nacimiento Invalido</p>"
        if(not dniM):
            print "<p>DNI Invalido</p>"
        if(not ingresoM):
            print "<p>Ingreso Invalido</p>"
        if(not emailM):
            print "<p>Email Invalido</p>"
        if(not telefonoM):
            print "<p>Telefono Invalido</p>"
        if(not celularM):
            print "<p>Celular Invalido</p>"
else:
    print "<p>No ha ingresado algun campo</p>"
print"""
    </div>    
</div>
"""
mihtml.bottombar()