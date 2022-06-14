from ...models.entidades.Metodo import Metodo
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(metodo: Metodo)->Metodo:
    # comment: 
    sql = """"insert into metodo values(:ID, :Nombre)"""

    parametros = metodo._asdict()
    _fetch_none(sql,parametros)
    return metodo
# end def

def update(metodo: Metodo)->Metodo:
    sql = """"update metodo set ID = ID, Nombre=Nombre"""
    # comment: 
# end def

def delete(metodo: Metodo)->Metodo:
    # comment: 
    pass
# end def