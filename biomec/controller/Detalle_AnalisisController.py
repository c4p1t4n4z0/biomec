from ..models.entidades.Detalle_Analisis import Detalle_Analisis
from ..database.db_entidades import detalle_analisis_db

def create(detalle_analisis: Detalle_Analisis)->Detalle_Analisis:
    # comment: 
    return detalle_analisis_db.create(detalle_analisis)
# end def

def update(detalle_analisis: Detalle_Analisis)->Detalle_Analisis:
    # comment: 
    return detalle_analisis_db.update(detalle_analisis)
# end def

def delete(detalle_analisis: Detalle_Analisis)->Detalle_Analisis:
    # comment: 
    return detalle_analisis_db.delete(detalle_analisis)
# end def