from ..models.entidades.Tipo_Muestra import Tipo_Muestra
from ..database.db_entidades import tipo_muestra_db

def create(tipo_muestra: Tipo_Muestra)->Tipo_Muestra:
    # comment: 
    return tipo_muestra_db.create(tipo_muestra)
# end def

def update(tipo_muestra: Tipo_Muestra)->Tipo_Muestra:
    # comment: 
    return tipo_muestra_db.update(tipo_muestra)
# end def

def delete(tipo_muestra: Tipo_Muestra)->Tipo_Muestra:
    # comment: 
    return tipo_muestra_db.delete(tipo_muestra)
# end def