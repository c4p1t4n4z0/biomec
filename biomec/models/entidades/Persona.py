from flask_login import UserMixin                   #debe ser importante 

class Persona(UserMixin):
#class User():
    #-----metodo constructor, reflejo de la tabla usuario de la base de datos BD_Lab-----
    #def __init__(self, ID, Nombre, Contraseña, ID_Rol_,ID_persona):
    def __init__(self,CI, Nombre, ApellidoP, ApellidoM,Telefono,Correo,Fecha_Nacimiento) -> None:        
        self.ci = CI
        self.nombre = Nombre
        self.apellido_paterno = ApellidoP
        self.apellido_materno = ApellidoM
        self.telefono = Telefono
        self.correo = Correo
        self.fecha_nacimiento = Fecha_Nacimiento

