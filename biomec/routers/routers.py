from flask import Blueprint, render_template

global_scope = Blueprint("views",__name__)


#funciones decoradas, (para que puedan ser usadas en otro archivo)
@global_scope.route('/', methods =['GET'])
def home():
    nav = [ #aqui hago una lista para navegar a otras rutas desde el home
           {"name": "Igresar","url":"/admin/login"} 
    ]

            # Aqui ponemos Titulo y descripcion 
    parametros = { "title": "Bienvenido a Biomec",
                    "description": " Tu Laboratorio clinico a tu alcanze"
    }
    return render_template("home.html", **parametros)

