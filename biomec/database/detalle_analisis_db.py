from ...models.entidades.Detalle_Analisis import Detalle_Analisis
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(detalle_analisis: Detalle_Analisis)->Detalle_Analisis:
    # comment: 
    sql = """"insert into detalle values(:ID_Recibo, :ID_L_Analisis)"""

    parametros = detalle_analisis._asdict()
    _fetch_none(sql,parametros)
    return detalle_analisis
# end def

def update(detalle_analisis: Detalle_Analisis)->Detalle_Analisis:
    sql = """"update detalle set ID_Recibo = ID_Recibo, ID_L_Analisis=ID_L_Analisis"""
    # comment: 
# end def

def delete(detalle_analisis: Detalle_Analisis)->Detalle_Analisis:
    # comment: 
    pass
# end def