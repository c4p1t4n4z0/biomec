from ..models.entidades.Privilegio import Privilegio
from ..database.db_entidades import privilegios_db

def create(privilegio: Privilegio)->Privilegio:
    # comment: 
    return privilegios_db.create(privilegio)
# end def

def update(privilegio: Privilegio)->Privilegio:
    # comment: 
    return privilegios_db.update(privilegio)
# end def

def delete(privilegio: Privilegio)->Privilegio:
    # comment: 
    return privilegios_db.delete(privilegio)
# end def

