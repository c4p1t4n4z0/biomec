from ...models.entidades.Paquete_Analisis import Paquete_Analisis
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(paquete_analisis: Paquete_Analisis)->Paquete_Analisis:
    # comment: 
    sql = """"insert into Paquete_Analisis values(:ID, :Nombre)"""

    parametros = paquete_analisis._asdict()
    _fetch_none(sql,parametros)
    return paquete_analisis
# end def

def update(paquete_analisis: Paquete_Analisis)->Paquete_Analisis:
    sql = """"update Paquete_Analisis set ID=ID, Nombre=Nombre"""
    # comment: 
# end def

def delete(paquete_analisis: Paquete_Analisis)->Paquete_Analisis:
    # comment: 
    pass
# end def