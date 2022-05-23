from flask import Blueprint, flash, redirect, render_template, request, session, url_for

# importamos los controladores de Usuario
from ..controller import UserController

# importamos los Modelos de usuario
from ..models.entidades.User import User 

global_scope = Blueprint("views",__name__)

#----------------------HOME------------------------------
#funciones decoradas, (para que puedan ser usadas en otro archivo)
@global_scope.route('/', methods =['GET'])
def home():
    #if 'Esta_logeado' in session:

            # Aqui ponemos Titulo y descripcion 
    parametros = { "title": "Bienvenido a Biomec ",
                  "description": " Tu Laboratorio clinico a tu alcanze"
    }
    return render_template("home.html", **parametros)

    #return redirect(url_for('tipo.login'))



        