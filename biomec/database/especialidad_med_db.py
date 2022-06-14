from ...models.entidades.Especialidad_Med import Especialida_Med
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(especialidad_med: Especialida_Med)->Especialida_Med:
    # comment: 
    sql = """"insert into Especialida_Med values(:ID, :Nombre_Esp)"""

    parametros = especialidad_med._asdict()
    _fetch_none(sql,parametros)
    return especialidad_med
# end def

def update(especialidad_med: Especialida_Med)-> Especialida_Med:
    sql = """"update Especialida_Med set ID = ID, Nombre_Esp=Nombre_Esp"""
    # comment: 
# end def

def delete(especialidad_med: Especialida_Med)-> Especialida_Med:
    # comment: 
    pass
# end def