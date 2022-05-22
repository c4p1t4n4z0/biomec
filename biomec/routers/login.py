from flask import Blueprint, flash, redirect, render_template, request, url_for
#Models
#from models.ModelUser import ModelUser
#Entidades
#from models.entidades.User import User

#Controllers
from ..controller import UserController

#Models
from ..models.entidades import User

login_scope = Blueprint('admin',__name__)



@login_scope.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        #print(request.form['username'])
        #print(request.form['password'])
        data = request.form
        print(data)        
        print(data['username'])
        print(data['password'])
        #print(UserController.login(user))
        logged_user =  UserController.existe('Nombre',data['username']) #usuario logeado
        print(logged_user)
        if logged_user != None: # existen valores 
            if logged_user.password:  #el password conincide ? TRUE o FALSE
                return redirect(url_for('views.home')) #Si la cotraselea es corecta se dirigue a una Dashborad
            else:
                flash("Contraseña invalida") # Contraseña invalida
                return render_template('auth/login.html')
        else:
            flash("Usuario no Encontrado") # Usuario no encontrado
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')
    #return 'login'


@login_scope.route('/signup')
def signup():
    return 'Signup'


@login_scope.route('/logout')
def logout():
    return 'Logout'