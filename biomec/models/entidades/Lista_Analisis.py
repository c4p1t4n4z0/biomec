from flask_login import UserMixin


class Lista_Analisis(UserMixin):
    def __init__(self, ID,Nombre,Precio,ID_Pqa):
        # comment: 
        self.id = ID
        self.nombre = Nombre
        self.precio = Precio
        self.id_paquete = ID_Pqa
    # end alternate constructor