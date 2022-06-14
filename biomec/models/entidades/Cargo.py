from flask_login import UserMixin


class Cargo(UserMixin):
    def __init__(self, ID_Cargo,Nombre):
        # comment: 
        self.id_cargo = ID_Cargo
        self.nombre = Nombre
    # end alternate constructor