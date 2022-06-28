from ..models.entidades.Seguro import Seguro
from ..database import seguro_db




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

#Devuelve lista completa 
def list():
    return seguro_db.list_all()