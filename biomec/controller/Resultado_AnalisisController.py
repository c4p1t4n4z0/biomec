from ..models.entidades.Resultado_Analisis import Resultado_Analisis
from ..database.db_entidades import resultado_analisis_db

def create(resultado_analisis: Resultado_Analisis)->Resultado_Analisis:
    # comment: 
    return resultado_analisis_db.create(resultado_analisis)
# end def

def update(resultado_analisis: Resultado_Analisis)->Resultado_Analisis:
    # comment: 
    return resultado_analisis_db.update(resultado_analisis)
# end def

def delete(resultado_analisis: Resultado_Analisis)->Resultado_Analisis:
    # comment: 
    return resultado_analisis_db.delete(resultado_analisis)
# end def