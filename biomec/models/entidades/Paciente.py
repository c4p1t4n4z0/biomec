from flask_login import UserMixin


class Paciente(UserMixin):
    def __init__(self, ID_Paciente,Nro_Sg):
        # comment: 
        self.id_paciente = ID_Paciente
        self.nro_sg = Nro_Sg
    # end alternate constructor