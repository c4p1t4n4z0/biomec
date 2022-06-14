from ..models.entidades.Rol import Rol
from ..database.db_entidades import rol_db

def create(rol: Rol)->Rol:
    # comment: 
    return rol_db.create(Rol)
# end def

def update(rol: Rol)->Rol:
    # comment: 
    return rol_db.update(Rol)
# end def

def delete(rol: Rol)->Rol:
    # comment: 
    return rol_db.delete(Rol)
# end def