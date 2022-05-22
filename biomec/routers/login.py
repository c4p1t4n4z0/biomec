from flask import Blueprint, flash, redirect, render_template, request, url_for
from sqlalchemy import true

# importamos los controladores de Usuario
from ..controller import UserController

# importamos los Modelos de usuario
from ..models.entidades.User import User 

login_scope = Blueprint('admin',__name__)


@login_scope.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        data = request.form     # guardo todos los datos ingresados por formulario de la vista
        print(data)        
        print(data['username'])
        print(data['password'])
        #existe_el_usuario = UserController.existe('Nombre',data['username']) 
        print('------datos ingresados por formulario-------')
        usuario = User(0,data['username'],data['password'],0,0)  # capturo los datos del formulario y mando al modelo User
                                                                 # los 0 son nulos porque no metemos desde formulario
        logged_user = UserController.login(usuario)
        if logged_user != None:         # Controlador de Usuario, si tienen datos
            if logged_user.password:    #si la contraseña coincide con el de la base de datos
                return redirect(url_for('views.home')) # se dirigue a una "Dashborad", falta crearla
            else:
                flash("Contraseña invalida")           # Contraseña invalida
                return render_template('auth/login.html')
        else:
            flash("Usuario no Encontrado")             # Usuario no encontrado
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')
        


@login_scope.route('/signup')
def signup():
    return 'Signup'


@login_scope.route('/logout')
def logout():
    return 'Logout'