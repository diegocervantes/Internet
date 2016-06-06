#!C:\Python27\python
#!/usr/bin/python

import mihtml
print("Content-Type: text/html\n")

imagenes = ["inicio/imagen3.png","inicio/imagen4.jpg","inicio/imagen5.png"]

subs = ["We strive to provide best-in-class advice and execution excellence on the most complex transactions across products in order to help our clients grow.",
 		"We are focused on being a significant financier and provider of capital-raising services, which, in turn, enables our clients to achieve their strategic goals.",
 		"Our Technology, Media and Telecommunications group provides insights and services covering a wide range of industries from electronics to software	to Internet to wireless and cable companies."]

mihtml.head("Inicio")
mihtml.header()
mihtml.topbar()

print"""
<div class="contenido">
	<div class="inicio-central">
		<div class="img-central"><img src ="inicio/imagen.jpg" alt="imagen"></div>
		<p>Inigo Solutions is a leading global investment banking, securities and investment management firm that provides a wide range of financial services 
        to a substantial and diversified client base that includes corporations, financial institutions, governments and individuals. Founded in 1869, the firm is 
        headquartered in Arequipa and maintains offices in all major financial centers around the world.
        Open source solutions have changed the way people are thinking about software and hardware alike.Inigo Solutions joined the open source community, the 
        Eclipse Foundation. As a solutions member, we will migrate our open source Java library, GS Collections, which will be renamed Eclipse Collections. The 
        migration will allow the open source community to contribute to and benefit from our work. The new foundation will work to drive forward collaboration and 
        standards on common container technologies among the developer community in deploying cloud native applications.</p>
	</div>"""

j =0 
for p in imagenes:
	print"""
	<div class="inicio-sub">
		<div class="sub-img"><img src=""",p,""" alt="imagen" ></div>
		<p >""", subs[j] ,"""</p>
	</div>
	"""
	j = j+1
print"""
</div>
"""
mihtml.bottombar()