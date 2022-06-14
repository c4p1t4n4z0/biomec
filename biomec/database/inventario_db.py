from ...models.entidades.Inventario import Inventario
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(inventario: Inventario)->Inventario:
    # comment: 
    sql = """"insert into inventario values(:ID, :Nombre, :Cantidad, :ID_lb)"""

    parametros = inventario._asdict()
    _fetch_none(sql,parametros)
    return inventario
# end def

def update(inventario: Inventario)->Inventario:
    sql = """"update inventario set ID = ID, Nombre=Nombre, ID_lb=ID_lb"""
    # comment: 
# end def

def delete(inventario: Inventario)->Inventario:
    # comment: 
    pass
# end def