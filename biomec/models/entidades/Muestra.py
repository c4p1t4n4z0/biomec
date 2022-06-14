from flask_login import UserMixin

class Muestra(UserMixin):
        def __init__(self,ID, Fecha, Hora, ID_lb,ID_pct,ID_TM,ID_Met) -> None:
                self.id = ID
                self.fecha = Fecha
                self.hora = Hora
                self.id_laboratorista = ID_lb
                self.id_paciente = ID_pct
                self.id_toma_muestra = ID_TM
                self.id_metodo = ID_Met
