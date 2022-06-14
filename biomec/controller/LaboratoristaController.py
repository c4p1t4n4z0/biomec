from ..models.entidades.Laboratorista import Laboratorista
from ..database import laboratorista_db

def create(laboratorista: Laboratorista)->Laboratorista:
    # comment: 
    return laboratorista_db.create(laboratorista)
# end def

def update(laboratorista: Laboratorista)->Laboratorista:
    # comment: 
    return laboratorista_db.update(laboratorista)
# end def

def delete(laboratorista: Laboratorista)->Laboratorista:
    # comment: 
    return laboratorista_db.delete(laboratorista)
# end def