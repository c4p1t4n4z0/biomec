from ...models.entidades.Privilegio import Privilegio
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(privilegio: Privilegio)->Privilegio:
    # comment: 
    sql = """"insert into Privilegio values(:ID, :Descripcion)"""

    parametros = privilegio._asdict()
    _fetch_none(sql,parametros)
    return privilegio
# end def

def update(privilegio: Privilegio)-> Privilegio:
    sql = """"update Privilegio set ID = ID, Descripcion=Descripcion"""
    # comment: 
# end def

def delete(privilegio: Privilegio)-> Privilegio:
    # comment: 
    pass
# end def
