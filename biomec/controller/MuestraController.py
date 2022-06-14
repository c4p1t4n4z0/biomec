from ..models.entidades.Muestra import Muestra
from ..database.db_entidades import muestra_db

def create(muestra: Muestra)->Muestra:
    # comment: 
    return muestra_db.create(muestra)
# end def

def update(muestra: Muestra)->Muestra:
    # comment: 
    return muestra_db.update(muestra)
# end def

def delete(muestra: Muestra)->Muestra:
    # comment: 
    return muestra_db.delete(muestra)
# end def