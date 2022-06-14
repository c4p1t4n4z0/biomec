from flask_login import UserMixin


class Detalle_Analisis(UserMixin):
    def __init__(self, ID_Recibo,ID_L_Analisis):
        # comment: 
        self.id_recibo = ID_Recibo
        self.id_lista_analisis = ID_L_Analisis
    # end alternate constructor