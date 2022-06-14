from ..models.entidades.Cargo import Cargo
from ..database.db_entidades import cargo_db

def create(cargo: Cargo)->Cargo:
    # comment: 
    return cargo_db.create(cargo)
# end def

def update(cargo: Cargo)->Cargo:
    # comment: 
    return cargo_db.update(cargo)
# end def

def delete(cargo: Cargo)->Cargo:
    # comment: 
    return cargo_db.delete(cargo)
# end def
