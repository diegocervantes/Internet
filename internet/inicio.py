#!C:\Users\SONY\AppData\Local\Programs\Python\Python35-32\python.exe
#!/usr/bin/python
print("Content-Type: text/html\n")

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

<div class="topbar">
    <div class="links-top">
		<a href="inicio.html"  title="Inicio"> INICIO</a>
		<a href="asistencias.py"  title="Asistencias"> ASISTENCIAS</a>
		<a href="admin.py"  title="Administración"> ADMIN</a>
    </div>
</div>

<div class="contenido">
	
	<div class="inicio-central">
		<div class="img-central">
			<img src ="inicio/imagen.jpg" alt="imagen">	
		</div>
		<p>Inigo Solutions is a leading global investment banking, securities and investment management firm that provides a wide range of financial services 
		to a substantial and diversified client base that includes corporations, financial institutions, governments and individuals. Founded in 1869, the firm is 
		headquartered in Arequipa and maintains offices in all major financial centers around the world.
		Open source solutions have changed the way people are thinking about software and hardware alike.Inigo Solutions joined the open source community, the 
		Eclipse Foundation. As a solutions member, we will migrate our open source Java library, GS Collections, which will be renamed Eclipse Collections. The 
		migration will allow the open source community to contribute to—and benefit from—our work. The new foundation will work to drive forward collaboration and 
		standards on common container technologies among the developer community in deploying cloud native applications.</p>
		
	</div>

	<div class="inicio-sub">
		<div class="sub-img">
			<img src="inicio/imagen3.png" alt="imagen" >
		</div>
		<p >We strive to provide best-in-class advice and execution excellence on the most complex transactions across products in order to help our clients grow.</p>
	</div>

	<div class="inicio-sub">
		<div class="sub-img">
			<img src="inicio/imagen4.jpg" alt="imagen" >
		</div>
		<p>We are focused on being a significant financier and provider of capital-raising services, which, in turn, enables our clients to achieve their st
		rategic goals.</p>
	</div>

	<div class="inicio-sub">
		<div class="sub-img">
			<img src="inicio/imagen5.jpg" alt="imagen" >
		</div>
		<p>Our Technology, Media and Telecommunications group provides insights and services covering a wide range of industries—from electronics to software 
		to Internet to wireless and cable companies.
	</div>
	
</div>
<div class="bottomBar">
	<div class="redes" >
		<a href="#"><img src="sns/logo1.png" alt="sns" ></a>
		<a href="#"><img src="sns/logo2.png" alt="sns" ></a>
		<a href="#"><img src="sns/logo3.png" alt="sns" ></a>
		<a href="#"><img src="sns/logo4.png" alt="sns" ></a>
	</div>
</div>
</body>
</html>	
"""
)