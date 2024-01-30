from flask import Flask

import mysql.connector 


# db = list()
db = mysql.connector.connect( # LLAMAMOS AL FUNCION CONNECT PARA CONECTARNOS
    host ='informatica.iesquevedo.es',
    port = 3333,
    user ='root', #USUARIO QUE USAMOS NOSOTROS
    password ='1asir', #CONTRASEÑA CON LA QUE NOS CONECTAMOS
    database='laura_fernandez'
) 



def create_app():
    app = Flask(__name__)
    app.debug = True
    

    

    from .routes import routes
    from .routes import routes_lenguajes

    
    app.register_blueprint(routes.rutas_juegos)
    app.register_blueprint(routes_lenguajes.rutas_lenguajes)
    return app