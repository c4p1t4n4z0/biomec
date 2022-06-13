from ..models.entidades.Persona import Persona 
from .connection import _fetch_all,_fecth_lastrow_id,_fetch_none,_fetch_one  #las funciones 

from typing import List
# usuario de tipo USER que apunta a User
def create(usuario: Persona) -> Persona:
    # falta implementar los metodos de validacion asi que hay que ingresar datos correctos sino genera error
    sql = """ INSERT INTO Persona VALUES({},'{}','{}','{}',{},'{}','{}') """.format(usuario.ci, usuario.nombre,usuario.apellido_paterno, usuario.apellido_materno, usuario.telefono, usuario.correo, usuario.fecha_nacimiento) #la variable del modelo User

    _fetch_none(sql,None)
    return usuario

def update(usuario: Persona) -> Persona:
    sql = """ UPDATE Usuario SET ID = ID, Nombre = Nomnre, Contraseña = Contraseña,
                                      ID_Rol_ = ID_Rol_, ID_persona = ID_persona """
def delete(usuario: Persona) -> Persona:
    pass

def list_all()  -> List[Persona]: #LISTO FUNCIONA
    sql = "SELECT * FROM Persona ORDER BY CI DESC"
    #print(sql) 
    persona_lista_sql = _fetch_all(sql,None)
    print(persona_lista_sql[0][1])

    personas_lista = list(persona_lista_sql)
    persona_lista = [] #Tupla que devolvera todos los datos de la tabla Persona

    for x in range(len(personas_lista)):
        #Almaceno los respecitvos atributos de la tabla
        ci = personas_lista[x][0]
        nombre = personas_lista[x][1]
        apellidoP = personas_lista[x][2]
        apellidoM = personas_lista[x][3]
        telefono = personas_lista[x][4]
        email = personas_lista[x][5]
        fecha_nacimiento = personas_lista[x][6]
        # Creo un diccionario con su respectivo encabezado y asigno el atributo correspondiente
        persona_datos = { 'ci':ci, 'nombre':nombre,'apellidoP':apellidoP,'apellidoM':apellidoM,'telefono':telefono,'email':email,'fecha_nacimiento':fecha_nacimiento}
        # por cada interaccion lo guardo el diccionario de los datos de cada persona en la lista
        persona_lista.append(persona_datos)

    return persona_lista

#Existe el usuario, retorna booleano      ejemplo  if user_exists("Nombre", user.nombre):
# field: los campos                   def user_existe(field: str, value: str) -> bool:
# value: atributo a buscar             
def user_existe(atributo: str, value: str) -> bool:
    sql = "SELECT  * FROM Persona WHERE {}  = '{}' ".format(atributo,value)
    #print(sql)
    boleano = _fetch_one(sql,None)
    return bool(boleano)

def sacar_el_ultimo_id():
    sql = "SELECT CI FROM Persona ORDER BY CI DESC"
    persona_lista_sql = _fetch_all(sql,None)
    #print(persona_lista_sql[0][0]) #esta es mas directo
    ci_= persona_lista_sql[0][0]
    return ci_

def obtener_persona(atributo: str, value: str) -> Persona:
    sql = """ SELECT CI, Nombre, ApellidoP, ApellidoM, Telefono, 
            Correo, Fecha_Nacimiento FROM Persona WHERE {}  = '{}' """ .format(atributo,value) #la variable del modelo persona
    row = _fetch_one(sql,None)

    if row !=None:
        persona = Persona(row[0],row[1],row[2], row[3],row[4],row[0],row[0])
        return persona  # El usuario se encuentra en la BD_Lab
        
        
    else:
        return None # no hay usuario