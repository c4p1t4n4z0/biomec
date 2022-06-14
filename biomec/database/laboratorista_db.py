from ..models.entidades.Laboratorista import Laboratorista
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(laboratorista: Laboratorista)->Laboratorista:
    # comment: 
    sql = """"insert into Laboratorista values(:ID_Laboratorista, :ID_Esp_med)"""

    parametros = laboratorista._asdict()
    _fetch_none(sql,parametros)
    return laboratorista
# end def

def update(laboratorista: Laboratorista)-> Laboratorista:
    sql = """"update Laboratorista set ID_Laboratorista = ID_Laboratorista, ID_Esp_med=ID_Esp_med"""
    # comment: 
# end def

def delete(laboratorista: Laboratorista)-> Laboratorista:
    # comment: 
    pass
# end def