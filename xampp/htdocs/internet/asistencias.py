#!C:\Python27\python
# -*- coding: utf-8 -*-
import mihtml

print("Content-Type: text/html\n")

nombres = ["Mauro Diaz", "Fredy Alvarez","Diego Cervantes"]
areas = ["Limpieza","Contabilidad","etc"]
faltas = [50,94,80]
asistencias = ["Si","No","-"]

mihtml.head("Asistencias")
mihtml.header()
mihtml.topbar()

print"""
<div class="contenido">
    <table class="t01">
        <tr>
            
            <th>Foto</th>
            <th>Nombres y Apellidos</th>
            <th>Area</th>
            <th>Faltas</th>
            <th>Asistio</th>
        </tr>
        """
j = 0
for i in nombres:
    print"""
        <tr>"""
    print"""
            <td>
            <img src = inicio/loro.jpg width=100 height = 100 alt = ""></td>
            <td>""",i,"""</td>      
            <td>""",areas[j],"""</td>
            <td>""",faltas[j],"""</td>
            <td>/</td>
        </tr>
        """
    j = j+1
print"""
    </table>
</div>
"""
mihtml.bottombar()