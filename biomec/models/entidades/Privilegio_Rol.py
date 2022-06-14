from flask_login import UserMixin


class Privilegio_Rol(UserMixin):
    def __init__(self, ID_Privilegio,ID_Rol):
        # comment: 
        self.id_privilegio = ID_Privilegio
        self.id_rol = ID_Rol
    # end alternate constructor