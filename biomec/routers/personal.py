from flask import Blueprint, flash, redirect, render_template, request, session, url_for


# importamos los controladores de Usuario
from ..controller import UserController
from ..controller import PersonaController
from ..controller import LaboratoristaController
# importamos los Modelos 
from ..models.entidades.User import User 
from ..models.entidades.Persona import Persona 
from ..models.entidades.Laboratorista import Laboratorista

from ..routers.tipo import session # estoy importando la variable global donde se guarda la session del usuario que ingreso al sistema
personal_scope = Blueprint('personal',__name__)

#realizar la vista del Inicio o Home "template"
@personal_scope.route('/', methods=['GET'])
def personal():

    if session['Esta_logeado']:  # obtengo el dato de la session que se almaceno en la ruta tipo.login

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Administrador",
                        "titulo": "Registrar Personal del laboratorio",
                        "titulo_usuario":"Listado del personal de la Empresa"
                }
 
        personas_lista = PersonaController.list()    #! implementar el modelo personal
        print(personas_lista)
        return render_template("usuario/admin/personal.html", **parametros, items = personas_lista)

    return redirect(url_for('tipo.login'))
