from flask_login import UserMixin


class Rol(UserMixin):
    def __init__(self, ID,Descripcion):
        # comment: 
        self.id = ID
        self.descripcion = Descripcion
    # end alternate constructor