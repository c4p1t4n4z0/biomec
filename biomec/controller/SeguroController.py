from ..models.entidades.Seguro import Seguro
from ..database.db_entidades import seguro_db

def create(seguro: Seguro)->Seguro:
    # comment: 
    return seguro_db.create(seguro)
# end def

def update(seguro: Seguro)->Seguro:
    # comment: 
    return seguro_db.update(seguro)
# end def

def delete(seguro: Seguro)->Seguro:
    # comment: 
    return seguro_db.delete(seguro)
# end def