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
def list_all(usuario: User) -> User:
    sql = """ SELECT ID,Nombre,Contraseña,ID_Rol_,ID_persona 
                      from Usuario 
                      where Nombre = '{}' """.format(usuario)       
    pass


#-----------------------  LOGIN --------------------------------
def login(usuario: User) -> User:
    if user_existe("Nombre",usuario.username):
        #falta implementar el usuario no encontrado, ponerle mensaje
        print('Existe el nombre de usuario en la Base de datos')
    else:
        print("NO existe el nombre de usuario en la Base de datos")

    sql = """ SELECT * from Usuario 
                    where Nombre = '{}' """.format(usuario.username) #la variable del modelo User
    
    #parametros = usuario.username
    parametros =[]

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
    sql = """ SELECT  * from Usuario 
                    where '{}'  = '{}' """.format(field,value)

    boleano = _fetch_one(sql)
    return bool(boleano)
