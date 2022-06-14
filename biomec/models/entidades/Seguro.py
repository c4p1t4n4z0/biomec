from flask_login import UserMixin


class Seguro(UserMixin):
    def __init__(self, Nro_Seguro,Nombre_Seguro):
        # comment: 
        self.nro_seguro = Nro_Seguro
        self.nombre_seguro = Nombre_Seguro
    # end alternate constructor