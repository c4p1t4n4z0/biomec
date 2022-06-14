from flask_login import UserMixin


class Recibo_Analisis(UserMixin):
    def __init__(self, ID,Fecha,Monto_Total,ID_Per,CI_Paciente):
        # comment: 
        self.id = ID
        self.fecha_recibo = Fecha
        self.monto_total = Monto_Total
        self.id_personal = ID_Per
        self.ci_paciente = CI_Paciente
    # end alternate constructor