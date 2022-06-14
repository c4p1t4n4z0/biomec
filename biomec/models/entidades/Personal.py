from flask_login import UserMixin


class Personal(UserMixin):
    def __init__(self,ID_Persona,ID_Crg) -> None:
        self.id_persona =   ID_Persona
        self.id_crg =  ID_Crg     
