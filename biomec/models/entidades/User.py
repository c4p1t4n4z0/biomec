from werkzeug.security import check_password_hash   #generate_password_hash   # para encryptar el password

class User():
    
    #-----metodo constructor, reflejo de la tabla usuario de la base de datos BD_Lab-----
    def __init__(self, ID, Nombre, Contraseña, ID_Rol_,ID_persona):
        self.id = ID
        self.username = Nombre
        self.password = Contraseña
        self.id_rol = ID_Rol_
        self.id_persona = ID_persona

    # ---------------para poder ver el password encryptado--------------------------------
    # hashed_password = ahi estara la contraseña hasheada para guardarla en la base de datos
    #        password = es la contraseña en texto plano 
    @classmethod  # Lo decoro con metodo de clase para poder usar (instanciar) este metodo en otro archivo
    def check_password(self,hashed_password, password):

        return check_password_hash(hashed_password, password)


#print(generate_password_hash("admin"))
# Este es el hash creado para la prueba el usuario admin,debes de insertarlo en la DB_Lab
#pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e
#