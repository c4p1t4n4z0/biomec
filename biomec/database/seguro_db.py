from ...models.entidades.Seguro import Seguro
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(seguro: Seguro)->Seguro:
    # comment: 
    sql = """"insert into Seguro values(:Nro_Seguro, :Nombre_Seguro)"""

    parametros = seguro._asdict()
    _fetch_none(sql,parametros)
    return seguro
# end def

def update(seguro: Seguro)-> Seguro:
    sql = """"update Seguro set Nro_Seguro = Nro_Seguro, Nombre_Seguro=Nombre_Seguro"""
    # comment: 
# end def

def delete(seguro: Seguro)-> Seguro:
    # comment: 
    pass
# end def