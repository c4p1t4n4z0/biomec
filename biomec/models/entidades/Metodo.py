from flask_login import UserMixin


class Metodo(UserMixin):
    def __init__(self, ID,Nombre):
        # comment: 
        self.id_metodo = ID
        self.nombre = Nombre
    # end alternate constructor