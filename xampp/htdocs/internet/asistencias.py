#!C:\Python27\python
# -*- coding: utf-8 -*-
import mihtml

print("Content-Type: text/html\n")

nombres = ["Mauro Diaz", "Fredy Alvarez","Diego Cervantes"]
areas = ["Limpieza","Contabilidad","etc"]
faltas = [50,94,80]
asistencias = ["Si","No","-"]

mihtml.head("Asistencias")
mihtml.header(True)


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
for (n,a,f) in zip(nombres, areas, faltas):
    print"""
        <tr>
            <td>
            <img src = inicio/loro.jpg width=100 height = 100 alt = ""></td>
            <td>""",n,"""</td>      
            <td>""",a,"""</td>
            <td>""",f,"""</td>
            <td>/</td>
        </tr>
        """
#arriba reemplazamos n, a y f por la base de datos
print"""
    </table>
</div>
"""
mihtml.bottombar()
