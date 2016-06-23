etiquetas = ["INICIO","ASISTENCIAS","ADMIN"]
enlaces = ["inicio.py","asistencias.py","admin.py"]
sns = ["sns/logo1.png","sns/logo2.png","sns/logo3.png","sns/logo4.png"]

def head(nombre):
    print"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>iniGO - """,nombre,"""</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" >
    <meta name="description" content="iniGO Solutions">
    <meta name="keywords" content="lista, asistencia, inigo, solution">
    <link href="style.css" rel="stylesheet" type="text/css" media="screen">
    </head>
    """

def login():
    print """
    <div class="login">
        <input type="submit" name="Iniciar sesion" value="Iniciar Sesion">
    </div>
    """

    # <div class="login">
    #     Usuario: 
    #     <input type="text" maxlength="10" size="10" name="usuario"></br>
    #     Contrasena:
    #     <input type="password" maxlength="10" size="10" name="password"></br>
    #     <input type="submit" name="enviar" value="Ingresar">
    # </div>

def header():
    print"""
    <body>
    <header>
        <div class="logo">
            <a href="inicio.py"><img src="logo.png" alt="iniGo"></a>
        </div>
    """
    login()
    print """
    </header>
    """

    
def topbar():
    print"""
        <div class="topbar">
        <div class="links-top">
        """

    for (i,j) in zip(etiquetas, enlaces):
        print"<a href=",j,"  title=",i,"> ",i,"</a>"

    print """ 
        </div>
        </div>
         """

def bottombar():
    print"""    
    <div class="bottomBar">
        <div class="redes" >
        """
    for i in sns:
        print"""<a href="#"><img src=""",i,""" " alt="sns" ></a>"""
    print"""
        </div>
    </div>
    </body>
    </html> 
    """