from flask_login import UserMixin
from ..models.entidades.User import User 
from .connection import _fetch_all,_fecth_lastrow_id,_fetch_none,_fetch_one  #las funciones 
# usuario de tipo USER que apunta a User
def create(usuario: User) -> User:
    # falta implementar los metodos de validacion asi que hay que ingresar datos correctos sino genera error
    sql = """ INSERT INTO Usuario VALUES(:ID,:Nombre,:Contraseña,
                                         :ID_Rol_,:ID_persona)"""   

    parametros = usuario._asdict()

    _fetch_none(sql,parametros)
    return usuario

def update(usuario: User) -> User:
    sql = """ UPDATE Usuario SET ID = ID, Nombre = Nomnre, Contraseña = Contraseña,
                                      ID_Rol_ = ID_Rol_, ID_persona = ID_persona """
def delete(usuario: User) -> User:
    pass

def list_all():
    sql = "SELECT * FROM Usuario"
    print(sql) 
    usuario_lista_sql = _fetch_all(sql,None)

    usuario_lista = [] #Tupla que devolvera todos los datos de la tabla Usuario

    for atributo in usuario_lista_sql:
        # Se guardan los datos de la fila N[1,2,3] las cuales tienen los atributos de la tabla Usuario
        usuario_fila = User(ID = atributo[0], Nombre = atributo[1], Contraseña = atributo[2],
                            ID_Rol_ = atributo[3], ID_persona = atributo[4])
        print(usuario_fila)

        usuario_lista.append(usuario_fila)

    return usuario_lista


#-----------------------  LOGIN --------------------------------
def login(usuario: User) -> User:

    sql = """ SELECT * from Usuario 
                    where Nombre = '{}' """.format(usuario.username) #la variable del modelo User
    
    #parametros = usuario.username
    parametros = None

    row = _fetch_one(sql,parametros)
    if row !=None:
        usuario = User(row[0],row[1], User.check_password(row[2],usuario.password), row[3],row[4])
        return usuario  # El usuario se encuentra en la BD_Lab
    else:
        return None # no hay usuario

#Existe el usuario, retorna booleano      ejemplo  if user_exists("nombre", user.nombre):
# field: los campos                   def user_existe(field: str, value: str) -> bool:
# value: atributo a buscar             
def user_existe(field: str, value: str) -> bool:
    sql = "SELECT  * from Usuario where {}  = {} ".format(field,value)
    print(sql)
    boleano = _fetch_one(sql,None)
    return bool(boleano)
