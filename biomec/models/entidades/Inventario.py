from flask_login import UserMixin


class Inventario(UserMixin):
    def __init__(self, ID,Nombre,Cantidad):
        # comment: 
        self.id = ID
        self.nombre = Nombre
        self.cantidad = Cantidad
    # end alternate constructor