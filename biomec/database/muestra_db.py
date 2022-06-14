from ...models.entidades.Muestra import Muestra
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(muestra: Muestra)->Muestra:
    # comment: 
    sql = """"insert into Muestra values(:ID, :Fecha, :Hora, 
                                        :ID_lb, :ID_pct, 
                                        :ID_TM, :ID_Met)"""

    parametros = muestra._asdict()
    _fetch_none(sql,parametros)
    return muestra
# end def

def update(muestra: Muestra)-> Muestra:
    sql = """"update Muestra set ID = ID, Fecha=Fecha, Hora=Hora, 
                                         ID_lb=ID_lb, ID_pct=ID_pct,
                                         ID_TM=ID_TM, ID_Met=ID_Met)"""
    # comment: 
# end def

def delete(muestra: Muestra)-> Muestra:
    # comment: 
    pass
# end def