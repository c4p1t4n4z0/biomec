from flask_login import UserMixin


class Especialida_Med(UserMixin):
    def __init__(self, ID,Nombre_Esp):
        # comment: 
        self.id = ID
        self.nombre_esp = Nombre_Esp
    # end alternate constructor