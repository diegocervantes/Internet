#!C:\Users\SONY\AppData\Local\Programs\Python\Python35-32\python.exe
#!/usr/bin/python
print("Content-Type: text/html\n")
etiquetas = ["INICIO","ASISTENCIAS","ADMIN"]
enlaces = ["inicio.py","asistencias.py","admin.py"]
sns = ["sns/logo1.png","sns/logo2.png","sns/logo3.png","sns/logo4.png"]
t1 = ["Agregar Area","Quitar Area", "Editar Horarios"]
t2 = ["Agregar Empleado", "Quitar Empleado", "Ver Empleado"]

print("""
<!DOCTYPE html>
<html>
<head>
<title>iniGO - Panel de Administrador</title>
<meta http-equiv="Content-Type" content="text/html; charset= utf-8" >
<meta name="description" content="iniGO Solutions">
<meta name="keywords" content="lista, asistencia, inigo, solution">
<link href="style.css" rel="stylesheet" type="text/css" media="screen">
</head>

<body>
<header>
	<div class="logo">
		<a href="inicio.py"><img src="logo.png" alt="iniGo"></a>
	</div>
</header>
""")
print("""
	<div class="topbar">
    <div class="links-top">""")
j = 0
for i in etiquetas:
	print("""<a href=""",enlaces[j],"""  title=""",i,"""> """,i,"""</a>""")
	j = j+1
print("""

    </div>
</div>""")

print("""
<div class="contenido">
	<table class="panel-admin">
	<tr>
		<td>Administrar Áreas</td>
		<td>Administrar Empleados </td>
	</tr>
	""")
j = 0
for i in t1:
	print("""
	<tr>""")
	print("""
		<td><a href="#" class="boton-admin">""",i,"""</a></td>
		<td><a href="#" class="boton-admin">""",t2[j],"""</a></td>
		""")
	j = j+1

print("""
	</table>
</div>
""")
print("""	
</div>
<div class="bottomBar">
	<div class="redes" >
	""")
for i in sns:
	print("""<a href="#"><img src=""",i,""" " alt="sns" ></a>""")
print("""
	</div>
</div>
</body>
</html>	
"""
)
