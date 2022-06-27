from flask import Blueprint, flash, redirect, render_template, request, session, url_for


# importamos los controladores de Usuario
from ..controller import UserController
from ..controller import PersonaController
from ..controller import LaboratoristaController
# importamos los Modelos 
from ..models.entidades.User import User 
from ..models.entidades.Persona import Persona 
from ..models.entidades.Laboratorista import Laboratorista
tipo_scope = Blueprint('tipo',__name__)

#realizar la vista del Inicio o Home "template"
@tipo_scope.route('/', methods=['GET'])
def roles():
    if 'Esta_logeado' in session:

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Administrador",
                        "titulo": "Visualizar Usuarios",
                        "titulo_usuario":"Listados de los Usuarios que interactuan con el Sistema"
                }
        return render_template("usuario/tipo.html", **parametros)

    return redirect(url_for('tipo.login'))


#----------------------LOGIN------------------------------
@tipo_scope.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        data = request.form     #guardo todos los datos ingresados por formulario de la vista
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
                session['id_rol'] = logged_user.id_rol #para comprobar su rol en las demas funciones               
                datos_de_persona = PersonaController.get_persona('CI',session['id_persona']) #para obtener su nombre completo
                #---concateno el nobre compleo despues de haber sacado los datos con el controlador de Persona
                session['username'] =  str(datos_de_persona.nombre) +" " +str(datos_de_persona.apellido_paterno)+" " +str(datos_de_persona.apellido_materno)



                # agregar aqui los numeros de roles para redirigir a su respectivo lugar
                lista_id_rol =[1,2,3]
                lista_tipo = ['tipo.roles','tipo.personal','tipo.tecnico'] 
                for id_rol in range(len(lista_id_rol)):
                        if logged_user.id_rol == lista_id_rol[id_rol]:
                                print('------datos de session para todos-------')
                                print("Usuario: " + session['username'] + " Tipo: " + str(session['id_rol']) )  
                                return redirect(url_for(lista_tipo[id_rol] )) #redirige dashboard que corresponde

            else:
                flash("Usuario o Contraseña invalida")           # Contraseña invalida
                return render_template('auth/login.html')
        else:
            flash("Usuario o Contraseña invalida")             # Usuario no encontrado
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


#----------------------ADMIN------------------------------
@tipo_scope.route('/admin', methods=['GET'])

def admin():
    if 'Esta_logeado' in session:

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Administrador"
        }

        usuarios_lista = UserController.list()

        #return render_template("usuario/admin/dashboard_admin.html", **parametros, items = usuarios_lista)
        #return render_template("base/navbar.html")
        return render_template("usuario/admin/dashboard_admin.html",**parametros)
    return redirect(url_for('tipo.login'))

@tipo_scope.route('/usuario', methods=['GET']) 
def usuario():

    # Aqui ponemos Titulo y descripcion 
    parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Administrador",
                        "titulo": "Visualizar Usuarios",
                        "titulo_usuario":"Listados de los Usuarios que interactuan con el Sistema"
                }

    usuarios_lista = UserController.list()

    return render_template("usuario/admin/usuario.html", **parametros, items = usuarios_lista)

        
#----------------------ADMIN - REGISTRO - USUARIO------------------------------


#* Para registrar nueva persona
@tipo_scope.route('/registro',methods=['GET', 'POST'])
def registro_persona():
    parametros = {  "title": "Bienvenido(a) "+ session['username'],
                        "description": "Registro de paciente"}    
    if request.method == "POST":
        data = request.form
        print(data)
        id_ultimo_persona = PersonaController.sacar_ultimo_id_persona()
        print('------datos ingresados por formulario-------')
        id_pesona = id_ultimo_persona + 1
        print(id_pesona)
        usuario = Persona(data['ci'],data['name'], data['apellidoP'],data['apellidoM'],data['telefono'],data['email'],data['fecha_nacimiento'])  # capturo los datos del formulario y mando al modelo User
                                                                 # los 0 son nulos porque no metemos desde formulario

        PersonaController.create(usuario)

        session['ci'] = usuario.ci #
        session['nombre'] = usuario.nombre #  
        #4569123


        return redirect(url_for('tipo.registro_user_paciente')) # solo puede registrar paciente

    return render_template('auth/registro_persona.html')


@tipo_scope.route('/registro/persona')
def registro_user_paciente():
    paciente = User(session['ci'], session['nombre'], session['ci'],4,session['ci'])  # capturo los datos del formulario y mando al modelo User
    
    print("registrando paciente--------------")                                      # los 0 son nulos porque no metemos desde formulario
    print (str(paciente) ) 
    UserController.create(paciente)
    return redirect(url_for('tipo.personal'))



#----------------------TECNICO------------------------------
@tipo_scope.route('/tecnico', methods=['GET', 'POST'])

def tecnico():
    if 'Esta_logeado' in session:

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Bienvenido: "+ session['username'] +" al Dasboard de tecnico en laboratorio clinico",
                        "description": " Tu Laboratorio clinico a tu alcanze"
        }
        personas_lista = PersonaController.list()        
        return render_template("usuario/personal/dashboard_personal.html", **parametros, items = personas_lista)

    return redirect(url_for('tipo.login'))





#----------------------Recepcionista------------------------------
@tipo_scope.route('/recepcionista', methods=['GET', 'POST'])
def recepcionista():
    if 'Esta_logeado' in session:   
        # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Bienvenido(a): "+ session['username'] +" al Dasboard de Personal",
                        "description": " Tu Laboratorio clinico a tu alcanze"
        }

        personas_lista = PersonaController.list()
        return render_template("usuario/personal/dashboard_recepcionista.html", **parametros, items = personas_lista)

    return redirect(url_for('tipo.login'))



#----------------------Laboratorista------------------------------
@tipo_scope.route('/bioquimico', methods=['GET'])

def bioquimico():
    if 'Esta_logeado' in session:

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Administrador"
        }
        return render_template("usuario/Laboratorista/dashboard_laboratorista.html",**parametros)
    return redirect(url_for('tipo.login'))


#----------------------Paciente------------------------------
@tipo_scope.route('/paciente', methods=['GET'])

def paciente():
    if 'Esta_logeado' in session:

                # Aqui ponemos Titulo y descripcion 
        parametros = { "title": "Biomec virtual",
                        "description": "Bienvenido(a) "+ session['username'],
                        "Nombre": session['username'],
                        "tipo": "Administrador"
        }
        return render_template("usuario/paciente/dashboard_paciente.html",**parametros)
    return redirect(url_for('tipo.login'))


#----------------------Registro Laboratorista/ Admin-----------------


@tipo_scope.route('/registro_laboratorista',methods=['GET', 'POST'])
def registro_laboratorista():
    parametros = {  "title": "Bienvenido(a) "+ session['username'],
                        "description": "Registro de paciente"}    
    if request.method == "POST":
        data = request.form
        print(data)
        print('------datos ingresados por formulario-------')
        persona = Persona(data['ci']  ,data['name'], data['apellidoP'],data['apellidoM'],data['telefono'],data['email'],data['fecha_nacimiento'])  # capturo los datos del formulario y mando al modelo User
        laboratorista = Laboratorista(data['ci'],data['especialidad'])                                                       # los 0 son nulos porque no metemos desde formulario

        PersonaController.create(persona)
        LaboratoristaController.create(laboratorista)

        flash('Se Registro Exitosamente')

        return redirect(url_for('tipo.admin')) # solo puede registrar paciente

    return render_template('auth/registro_persona.html')




@tipo_scope.route('/logout')
def logout():
    if 'Esta_logeado' in session:  
        session.pop('Esta_logeado',None)
        session.pop('username',None)
        return redirect(url_for('views.home'))
    return redirect(url_for('tipo.login'))
