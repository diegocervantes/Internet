etiquetas = ["INICIO","ASISTENCIAS","ADMIN"]
enlaces = ["inicio.py","asistencias.py","admin.py"]
sns = ["sns/logo1.png","sns/logo2.png","sns/logo3.png","sns/logo4.png"]

def head(nombre):
    print"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>iniGO - """,nombre,"""</title>
    <script type="text/javascript" src="jquery.min.js"></script> 
    <script type="text/javascript"> 
    function getData(){
            var parametros = {
                    "usuario" : document.getElementById('usuario').value,
                    "password" : document.getElementById('password').value,
            };
            $.ajax({
                    data:  parametros,
                    url:   'insertar.py',
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
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" >
    <meta name="description" content="iniGO Solutions">
    <meta name="keywords" content="lista, asistencia, inigo, solution">
    <link href="style.css" rel="stylesheet" type="text/css" media="screen">
    </head>
    """

def login():
	print	"""
	<div class = "login">
		<form action="" method="post" name="miform">
    	Usuario:
    	<input type="text" maxlength="11" size="10" name="usuario" id=usuario></br>
    	Password:
    	<input type="password" maxlength="20" size="10" name="password" id=password></br>
    	<input type="button" name="enviar" value="enviar" onClick="getData();">
    	<div id="contenido"></div>
	</form>
	</div>
"""	

    # <div class="login">
    #     Usuario: 
    #     <input type="text" maxlength="10" size="10" name="usuario"></br>
    #     Contrasena:
    #     <input type="password" maxlength="10" size="10" name="password"></br>
    #     <input type="submit" name="enviar" value="Ingresar">
    # </div>

def header(valor):
    print"""
    <body>
    <header>
        <div class="logo">
            <a href="inicio.py"><img src="logo.png" alt="iniGo"></a>
        </div>
    """
    if (valor == False):
        login()
    else:
        print  """
    <div class=login>
    <form action="inicio.py">
        <input type="submit" value="Cerrar Sesion">
    </form>
    </div>
""" 

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
