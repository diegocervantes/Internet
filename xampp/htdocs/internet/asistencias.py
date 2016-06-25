#!C:\Python27\python
# -*- coding: utf-8 -*-
import mihtml
import cgi
import cgitb; cgitb.enable()
import mysql.connector
import re

print("Content-Type: text/html\n")

db = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inigo')

mihtml.head("Asistencias")
mihtml.header(True)


form = cgi.FieldStorage() 

nombre = form.getfirst('nombre', 'empty')

print ("""
    <TITLE>CGI script ! Python</TITLE>
    <script type="text/javascript" src="jquery.min.js"></script> 
    <script type="text/javascript"> 

    function getData(){
            var parametros = {
                    "nombre" : document.getElementById('nombre').value,
            };
            $.ajax({
                    data:  parametros,
                    url:   'buscarAjax.py',
                    type:  'get',
                    beforeSend: function () {
                            $("#contenido").html("Procesando, espere por favor...");
                    },
                    success:  function (response) {
                            $("#contenido").html(response);
                    }
            });
    }
    </script> 
    <body>
"""
)




print"""
<div class="contenido">
    <form action="" class="formulario-container" method="post" name="miform">
        <br>     
            <label class="formulario-text-grey">Busqueda:</label>
        <input  type="text" maxlength="10" size="10" name="nombre" id=nombre>
        <input type="button" name="Buscar" value="Buscar" onClick="getData();">
        </br>
        <div id="contenido"></div>
        </br> 
    </form>
"""
#arriba reemplazamos n, a y f por la base de datos
print"""

</div>
"""
mihtml.bottombar()