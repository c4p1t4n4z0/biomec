from flask_login import UserMixin


class Laboratorista(UserMixin):
    def __init__(self, ID_Laboratorista,ID_Esp_med):
        # comment: 
        self.id_laboratorista = ID_Laboratorista
        self.id_esp_med = ID_Esp_med
    # end alternate constructor