from flask_login import UserMixin


class Resultado_Analisis(UserMixin):
    def __init__(self, ID,Descripcion,Fecha,Orden_Med,ID_lb,ID_pct):
        # comment: 
        self.id = ID
        self.descripcion = Descripcion
        self.fecha_emicion = Fecha
        self.orden_Medica = Orden_Med
        self.id_laboratorista = ID_lb
        self.id_paciente = ID_pct
    # end alternate constructor