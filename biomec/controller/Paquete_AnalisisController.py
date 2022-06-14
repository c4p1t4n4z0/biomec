from ..models.entidades.Paquete_Analisis import Paquete_Analisis
from ..database.db_entidades import paquete_analisis_db

def create(paquete_analisis: Paquete_Analisis)->Paquete_Analisis:
    # comment: 
    return paquete_analisis_db.create(paquete_analisis)
# end def

def update(paquete_analisis: Paquete_Analisis)->Paquete_Analisis:
    # comment: 
    return paquete_analisis_db.update(paquete_analisis)
# end def

def delete(paquete_analisis: Paquete_Analisis)->Paquete_Analisis:
    # comment: 
    return paquete_analisis_db.delete(paquete_analisis)
# end def