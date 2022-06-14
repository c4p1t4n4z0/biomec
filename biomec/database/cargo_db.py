from ...models.entidades.Cargo import Cargo
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(cargo: Cargo)->Cargo:
    # comment: 
    sql = """"insert into Cargo values(:ID_Cargo, :Nombre)"""

    parametros = cargo._asdict()
    _fetch_none(sql,parametros)
    return cargo
# end def

def update(cargo: Cargo)-> Cargo:
    sql = """"update Cargo set ID_Cargo = ID_Cargo, Nombre=Nombre"""
    # comment: 
# end def

def delete(cargo: Cargo)-> Cargo:
    # comment: 
    pass
# end def