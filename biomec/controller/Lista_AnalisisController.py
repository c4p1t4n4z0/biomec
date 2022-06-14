from ..models.entidades.Lista_Analisis import Lista_Analisis
from ..database.db_entidades import lista_analisis_db

def create(lista_analisis: Lista_Analisis)->Lista_Analisis:
    # comment: 
    return lista_analisis_db.create(Lista_Analisis)
# end def

def update(lista_analisis: Lista_Analisis)->Lista_Analisis:
    # comment: 
    return lista_analisis_db.update(Lista_Analisis)
# end def

def delete(lista_analisis: Lista_Analisis)->Lista_Analisis:
    # comment: 
    return lista_analisis_db.delete(Lista_Analisis)
# end def