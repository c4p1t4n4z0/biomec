from flask_login import UserMixin


class Tipo_Muestra(UserMixin):
    def __init__(self, ID,Nombre):
        # comment: 
        self.id_muestra = ID
        self.nombre = Nombre
    # end alternate constructor