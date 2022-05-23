from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import login_required

# importamos los controladores de Usuario
from ..controller import UserController,PersonaController

# importamos los Modelos de usuario
from ..models.entidades.User import User 


tipo_scope = Blueprint('tipo',__name__)


@tipo_scope.route('/', methods=['GET'])

def roles():
    if 'Esta_logeado' in session:

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Bienvenido(a) Admin: " + session['username'] +" seleccione un Rol",
                        "description": " Tu Laboratorio clinico a tu alcanze"
        }
        return render_template("usuario/tipo.html", **parametros)

    return redirect(url_for('tipo.login'))

#----------------------LOGIN------------------------------
#mejorar esta parte darle otra vista
@tipo_scope.route('/login', methods=['GET', 'POST'])
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
            print(str(logged_user.id_persona )+ ' id del usuario')
            if logged_user.password:    #si la contraseña coincide con el de la base de datos
                #return redirect(url_for('views.home')) # se dirigue a una "Dashborad", falta crearla
                session['Esta_logeado'] = True
                session['id_persona'] = logged_user.id_persona # id_persona del usuario                
                datos_de_persona = PersonaController.get_persona('CI',session['id_persona']) #para obtener su nombre completo
                #---concateno el nobre compleo despues de haber sacado los datos con el controlador de Persona
                session['username'] =  str(datos_de_persona.nombre) +" " +str(datos_de_persona.apellido_paterno)+" " +str(datos_de_persona.apellido_materno)
                print('------datos de session para todos-------')
                print(session['username'])


                # agregar aqui los numeros de roles para redirigir a su respectivo lugar
                lista_id_rol =[1,2,3]
                lista_tipo = ['tipo.roles','tipo.personal','tipo.tecnico'] 
                for id_rol in range(len(lista_id_rol)):
                        if logged_user.id_rol == lista_id_rol[id_rol]:
                                print(logged_user.id_rol)
                                print(lista_id_rol[id_rol])        
                                return redirect(url_for(lista_tipo[id_rol] )) #redirige dashboard que corresponde

            else:
                flash("Contraseña invalida")           # Contraseña invalida
                return render_template('auth/login.html')
        else:
            flash("Usuario no Encontrado")             # Usuario no encontrado
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


#----------------------ADMIN------------------------------
@tipo_scope.route('/admin', methods=['GET'])

def admin():
    if 'Esta_logeado' in session:

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Bienvenido(a) "+ session['username']+ " al Dasboard de Administrador" ,
                        "description": " Tu Laboratorio clinico a tu alcanze"
        }
        return render_template("usuario/admin/dashboard_admin.html", **parametros)

    return redirect(url_for('tipo.login'))
    
#----------------------ADMIN - REGISTRO - USUARIO------------------------------
@tipo_scope.route('/registro/usuario',methods=['GET', 'POST'])
def registro_user():
    parametros = {  "title": "Bienvenido(a) "+ session['username']+ " al Dasboard de Administrador" ,
                        "description": "Comenzemos la administracion"}
    #return render_template("auth/registro.html", **parametros)  
    return render_template("auth/registro.html", **parametros)



#----------------------TECNICO------------------------------
@tipo_scope.route('/tecnico', methods=['GET', 'POST'])

def tecnico():
    if 'Esta_logeado' in session:

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Bienvenido: "+ session['username'] +" al Dasboard de tecnico en laboratorio clinico",
                        "description": " Tu Laboratorio clinico a tu alcanze"
        }
        return render_template("usuario/personal/dashboard_tecnico.html", **parametros)

    return redirect(url_for('tipo.login'))





#----------------------PERSONAL------------------------------
@tipo_scope.route('/personal', methods=['GET', 'POST'])

def personal():
    if 'Esta_logeado' in session:   

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Bienvenido(a): "+ session['username'] +" al Dasboard de Personal",
                        "description": " Tu Laboratorio clinico a tu alcanze"
        }
        return render_template("usuario/personal/dashboard_personal.html", **parametros)

    return redirect(url_for('tipo.login'))







@tipo_scope.route('/logout')
def logout():
    if 'Esta_logeado' in session:  
        session.pop('Esta_logeado',None)
        session.pop('username',None)
        return redirect(url_for('views.home'))
    return redirect(url_for('tipo.login'))