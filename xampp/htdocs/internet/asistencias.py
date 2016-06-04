#!C:\Users\SONY\AppData\Local\Programs\Python\Python35-32\python.exe
#!/usr/bin/python
print("Content-Type: text/html\n")

etiquetas = ["INICIO","ASISTENCIAS","ADMIN"]
enlaces = ["inicio.py","asistencias.py","admin.py"]
sns = ["sns/logo1.png","sns/logo2.png","sns/logo3.png","sns/logo4.png"]
nombres = ["Mauro Diaz", "Fredy Alvarez","Diego Cervantes"]
areas = ["Limpieza","Contabilidad","etc"]
faltas = [50,94,80]
asistencias = ["Si","No","-"]
print("""
<!DOCTYPE html>
<html>
<head>
<title>iniGO - Asistencias</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" >
<meta name="description" content="iniGO Solutions">
<meta name="keywords" content="lista, asistencia, inigo, solution">
<link href="style.css" rel="stylesheet" type="text/css" media="screen">
</head>

<body>
<header>
	<div class="logo">
		<a href="inicio.py"><img src="logo.png" alt="iniGo"></a>
	</div>
</header>""")

print("""
	<div class="topbar">
    <div class="links-top">""")
j = 0
for i in etiquetas:
	print("""<a href=""",enlaces[j],"""  title=""",i,"""> """,i,"""</a>""")
	j = j+1
print("""
    </div>
</div>

<div class="contenido">
	<table class="t01">
  		<tr>
  			
  			<th>Foto</th>
		    <th>Nombres y Apellidos</th>
		    <th>Area</th>
		    <th>Faltas</th>
		    <th>Asistio</th>
  		</tr>
  		""")
j = 0
for i in nombres:
	print("""
  		<tr>""")
	print("""
  			<td>
  			<img src = inicio/loro.jpg width=100 height = 100 alt = ""></td>
  		    <td>""",i,"""</td>		
		    <td>""",areas[j],"""</td>
		    <td>""",faltas[j],"""</td>
		    <td>/</td>
		</tr>
		""")
	j = j+1
print("""
	</table>
</div>
<div class="bottomBar">
	<div class="redes" >""")
for i in sns:
	print("""<a href="#"><img src=""",i,""" " alt="sns" ></a>""")
print("""
	</div>
</div>
</body>
</html>	
"""
)