from ..models.entidades.Recibo_Analisis import Recibo_Analisis
from ..database.db_entidades import recibo_analisis_db

def create(recibo_analisis: Recibo_Analisis)->Recibo_Analisis:
    # comment: 
    return recibo_analisis_db.create(recibo_analisis)
# end def

def update(recibo_analisis: Recibo_Analisis)->Recibo_Analisis:
    # comment: 
    return recibo_analisis_db.update(recibo_analisis)
# end def

def delete(recibo_analisis: Recibo_Analisis)->Recibo_Analisis:
    # comment: 
    return recibo_analisis_db.delete(recibo_analisis)
# end def