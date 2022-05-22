from ..models.entidades.User import User 
from ..database import usuario_db

# usuario de tipo USER que tendra como resultado de tipo User
def create(usuario: User) -> User:
    # falta implementar los metodos de validacion asi que hay que ingresar datos correctos sino genera error
    return usuario_db.create(usuario)


def update(usuario: User) -> User:
    return usuario_db.update(usuario)


def delete(usuario: User) -> User:
    return usuario_db.delete(usuario)

#Devuelve lista completa 
def list():
    return usuario_db.list_all()        

def login(usuario: User) -> User:
    return usuario_db.login(usuario)

def existe(field: str, value: str) -> bool:
    return usuario_db.user_existe(field,value)


'''
class ModelUser():
    
    # self: hace referencia al mismo 
    # db  : para conectarse a la BD_Lab
    # user: el usuario que voy a comprobar si esta en la BD_Lab, es lo que escribimos en el formulario de login.html
    
    @classmethod # Lo decoro con metodo de clase para poder usar (instanciar) este metodo en otro archivo
    def login(self,db,user):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT ID,Nombre,Contraseña,ID_Rol_,ID_persona 
                      from Usuario 
                      where Nombre = '{}' """.format(user.username)
            
            cursor.execute(sql)
            row = cursor.fetchone() #El resultado de toda consulta es devuelta en una tupla

            if row != None:  #Si hay algun dato resultante
                # row[0] => ID , row[1] => Nombre, row[2] => uso el metodo para comprobar contraseña  hasheada con user.password que es el texto plano del formulario de login
                # row[3] =>es el rol, row[4]=>el id de persona
                user=User(row[0],row[1], User.check_password(row[2],user.password), row[3],row[4]  )
            else:
                return None

        except Exception as ex:
            raise Exception(ex)
'''            