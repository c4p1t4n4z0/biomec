from ..models.entidades.User import User 
from .connection import _fetch_all,_fecth_lastrow_id,_fetch_none,_fetch_one  #las funciones 
# usuario de tipo USER que apunta a User
def create(usuario: User) -> User:
    # falta implementar los metodos de validacion asi que hay que ingresar datos correctos sino genera error
    sql = """ INSERT INTO Usuario VALUES( {},'{}','{}',{},{}) """.format(usuario.id,usuario.username,usuario.password,usuario.id_rol,usuario.id_persona) #la variable del modelo User

    _fetch_none(sql,None)
    return usuario

def update(usuario: User) -> User:
    sql = """ UPDATE Usuario SET ID = ID, Nombre = Nomnre, Contraseña = Contraseña,
                                      ID_Rol_ = ID_Rol_, ID_persona = ID_persona """
def delete(usuario: User) -> User:
    pass

def list_all(): #LISTO FUNCIONA
    sql = "SELECT * FROM Usuario Persona ORDER BY ID DESC"
    print(sql) 
    usuario_lista_sql = _fetch_all(sql,None)

    usuarios_lista = list(usuario_lista_sql)
    usuario_lista = [] #Tupla que devolvera todos los datos de la tabla Usuario
    id_roles =['','admin','Recepcionista','Laboratorista','Paciente'] #lista de roles, el primero es vacio porque es 0
    for x in range(len(usuarios_lista)):
        id = usuarios_lista[x][0]
        nombre = usuarios_lista[x][1]
        contraseña = usuarios_lista[x][2]
        id_rol = usuarios_lista[x][3]
        #Este es un ciclo para poder mostrar en string su tipo de rol y no mostrar numero
        for i in range(len(id_roles)):
            if i == id_rol:
                id_rol = id_roles[i]
        id_persona= usuarios_lista[x][4]
        # Creo un diccionario con su respectivo encabezado y asigno el atributo correspondiente
        print(contraseña)
        usuario_datos = { 'id':id, 'nombre':nombre,'contraseña':contraseña,'id_rol':id_rol,'id_persona':id_persona}
        # por cada interaccion lo guardo el diccionario de los datos de cada persona en la lista
        usuario_lista.append(usuario_datos)

    return usuario_lista


#-----------------------  LOGIN --------------------------------
def login(usuario: User) -> User:
    sql = " SELECT ID, Nombre, Contraseña, ID_Rol_,ID_persona FROM Usuario WHERE Nombre = '{}' ".format(usuario.username) #la variable del modelo User
    row = _fetch_one(sql,None)
    if row !=None:
        usuario = User(row[0],row[1], (User.check_password(row[2],(usuario.password))), row[3],row[4])
        print(usuario)
        return usuario  # El usuario se encuentra en la BD_Lab
    else:
        return None # no hay usuario

#Existe el usuario, retorna booleano      ejemplo  if user_exists("Nombre", user.nombre):
# field: los campos                   def user_existe(field: str, value: str) -> bool:
# value: atributo a buscar             
def user_existe(atributo: str, value: str) -> bool:
    sql = "SELECT  * FROM Usuario WHERE {}  = '{}' ".format(atributo,value)
    print(sql)
    boleano = _fetch_one(sql,None)
    return bool(boleano)


def sacar_el_ultimo_id():
    sql = "SELECT ID FROM Usuario ORDER BY ID DESC"
    persona_lista_sql = _fetch_all(sql,None)
    #print(int(persona_lista_sql[0][0])) #esta es mas directo

    id_= persona_lista_sql[0][0]
    return id_