from flask_login import UserMixin


class Paquete_Analisis(UserMixin):
    def __init__(self, ID,Nombre):
        # comment: 
        self.id = ID
        self.nombre = Nombre
    # end alternate constructor