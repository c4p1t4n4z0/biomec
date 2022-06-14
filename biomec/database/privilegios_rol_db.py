from ...models.entidades.Privilegio_Rol import Privilegio_Rol
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(privilegio_rol: Privilegio_Rol)->Privilegio_Rol:
    # comment: 
    sql = """"insert into Privilegio_Rol values(:ID_Cargo, :Nombre)"""

    parametros = privilegio_rol._asdict()
    _fetch_none(sql,parametros)
    return privilegio_rol
# end def

def update(privilegio_rol: Privilegio_Rol)-> Privilegio_Rol:
    sql = """"update Privilegio_Rol set ID_Cargo = ID_Cargo, Nombre=Nombre"""
    # comment: 
# end def

def delete(privilegio_rol: Privilegio_Rol)-> Privilegio_Rol:
    # comment: 
    pass
# end def
