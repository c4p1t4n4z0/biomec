
from flask_login import UserMixin


class Privilegio(UserMixin):
    def __init__(self, ID, Descripcion):
        # comment: 
        self.id = ID
        self.descripcion =Descripcion
    # end alternate constructor