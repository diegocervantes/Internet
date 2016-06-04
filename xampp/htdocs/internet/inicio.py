#!C:\Users\SONY\AppData\Local\Programs\Python\Python35-32\python.exe
#!/usr/bin/python
print("Content-Type: text/html\n")

etiquetas = ["INICIO","ASISTENCIAS","ADMIN"]
enlaces = ["inicio.py","asistencias.py","admin.py"]
sns = ["sns/logo1.png","sns/logo2.png","sns/logo3.png","sns/logo4.png"]
imagenes = ["inicio/imagen3.png","inicio/imagen4.jpg","inicio/imagen5.jpg"]

descripcion = """Inigo Solutions is a leading global investment banking, securities and investment management firm that provides a wide range of financial services 
		to a substantial and diversified client base that includes corporations, financial institutions, governments and individuals. Founded in 1869, the firm is 
		headquartered in Arequipa and maintains offices in all major financial centers around the world.
		Open source solutions have changed the way people are thinking about software and hardware alike.Inigo Solutions joined the open source community, the 
		Eclipse Foundation. As a solutions member, we will migrate our open source Java library, GS Collections, which will be renamed Eclipse Collections. The 
		migration will allow the open source community to contribute to and benefit from our work. The new foundation will work to drive forward collaboration and 
		standards on common container technologies among the developer community in deploying cloud native applications."""

subs = ["""We strive to provide best-in-class advice and execution excellence on the most complex transactions across products in order to help our clients grow.""",
 		"""We are focused on being a significant financier and provider of capital-raising services, which, in turn, enables our clients to achieve their st
		rategic goals.""",
 		"""Our Technology, Media and Telecommunications group provides insights and services covering a wide range of industries from electronics to software 
		to Internet to wireless and cable companies."""]


print ("""
<!DOCTYPE html>
<html>
<head>
<title>iniGO - Inicio</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" >
<meta name="description" content="iniGO Solutions">
<meta name="keywords" content="lista, asistencia, inigo, solution">
<link href="style.css" rel="stylesheet" type="text/css" media="screen">
</head>
""")

print("""
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
</div>

<div class="contenido">
	
	<div class="inicio-central">
		<div class="img-central">
			<img src ="inicio/imagen.jpg" alt="imagen">	
		</div>
		<p>
		""", descripcion, """</p>
		
	</div>""")

j =0 
for p in imagenes:
	print("""
	<div class="inicio-sub">
		<div class="sub-img">
			<img src=""",p,""" alt="imagen" >
		</div>
		<p >""", subs[j] ,"""</p>
	</div>
	""")
	j = j+1

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