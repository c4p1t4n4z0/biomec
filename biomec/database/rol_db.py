from ...models.entidades.Rol import Rol
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(rol: Rol)->Rol:
    # comment: 
    sql = """"insert into Rol values(:ID, :Nombre)"""

    parametros = rol._asdict()
    _fetch_none(sql,parametros)
    return rol
# end def

def update(rol: Rol)-> Rol:
    sql = """"update Rol set ID = ID, Nombre=Nombre"""
    # comment: 
# end def

def delete(rol: Rol)-> Rol:
    # comment: 
    pass
# end def
