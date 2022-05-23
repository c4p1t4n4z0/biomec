from ..models.entidades.Persona import Persona 
from .connection import _fetch_all,_fecth_lastrow_id,_fetch_none,_fetch_one  #las funciones 
# usuario de tipo USER que apunta a User
def create(usuario: Persona) -> Persona:
    # falta implementar los metodos de validacion asi que hay que ingresar datos correctos sino genera error
    sql = """ INSERT INTO Usuario VALUES(:ID,:Nombre,:Contraseña,
                                         :ID_Rol_,:ID_persona)"""   

    parametros = usuario._asdict()

    _fetch_none(sql,parametros)
    return usuario

def update(usuario: Persona) -> Persona:
    sql = """ UPDATE Usuario SET ID = ID, Nombre = Nomnre, Contraseña = Contraseña,
                                      ID_Rol_ = ID_Rol_, ID_persona = ID_persona """
def delete(usuario: Persona) -> Persona:
    pass

def list_all(): #LISTO FUNCIONA
    sql = "SELECT * FROM Persona"
    print(sql) 
    persona_lista_sql = _fetch_all(sql,None)
    print(persona_lista_sql)
    persona_lista = [] #Tupla que devolvera todos los datos de la tabla Persona

    for atributo in persona_lista_sql:
        # Se guardan los datos de la fila N[1,2,3] las cuales tienen los atributos de la tabla Usuario
        persona_fila = Persona(CI = atributo[0], Nombre= atributo[1], ApellidoP= atributo[2],
                            ApellidoM = atributo[3], Telefono = atributo[4],Correo = [5], Fecha_Nacimiento = [6])
        print(persona_fila)

        persona_lista.append(persona_fila)

    return persona_lista


#Existe el usuario, retorna booleano      ejemplo  if user_exists("Nombre", user.nombre):
# field: los campos                   def user_existe(field: str, value: str) -> bool:
# value: atributo a buscar             
def user_existe(atributo: str, value: str) -> bool:
    sql = "SELECT  * FROM Persona WHERE {}  = '{}' ".format(atributo,value)
    print(sql)
    boleano = _fetch_one(sql,None)
    return bool(boleano)


def obtener_persona(atributo: str, value: str) -> Persona:
    sql = """ SELECT CI, Nombre, ApellidoP, ApellidoM, Telefono, 
            Correo, Fecha_Nacimiento FROM Persona WHERE {}  = '{}' """ .format(atributo,value) #la variable del modelo persona
    row = _fetch_one(sql,None)
    if row !=None:
        persona = Persona(row[0],row[1],row[2], row[3],row[4],row[0],row[0])
        return persona  # El usuario se encuentra en la BD_Lab
    else:
        return None # no hay usuario