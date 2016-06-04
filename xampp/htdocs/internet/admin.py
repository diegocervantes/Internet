#!C:\Python27\python
#!/usr/bin/python

import mihtml

print("Content-Type: text/html\n")

t1 = ["Agregar Area","Quitar Area", "Editar Horarios"]
t2 = ["Agregar Empleado", "Quitar Empleado", "Ver Empleado"]

mihtml.head("Admin")
mihtml.header()
mihtml.topbar()

print"""
<div class="contenido">
    <table class="panel-admin">
    <tr>
        <td>Administrar Areas</td>
        <td>Administrar Empleados </td>
    </tr>
    """

j = 0
for i in t1:
    print"""
        <tr>
            <td><a href="#" class="boton-admin">""",i,"""</a></td>
            <td><a href="#" class="boton-admin">""",t2[j],"""</a></td>
        </tr>
        """
    j = j+1

print"""
    </table>
</div>
"""
mihtml.bottombar()