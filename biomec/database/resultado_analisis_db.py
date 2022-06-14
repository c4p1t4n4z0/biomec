from ...models.entidades.Resultado_Analisis import Resultado_Analisis
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(resultado_analisis: Resultado_Analisis)->Resultado_Analisis:
    # comment: 
    sql = """"insert into Resultado_Analisis values(:ID, :Descripcion, :Fecha, 
                                                    :Orden_Medico, :ID_lb, :ID_pct)"""

    parametros = resultado_analisis._asdict()
    _fetch_none(sql,parametros)
    return resultado_analisis
# end def

def update(resultado_analisis: Resultado_Analisis)->Resultado_Analisis:
    sql = """"update Resultado_Analisis set ID = ID, Descripcion=Descripcion,
                                            fecha=Fecha, Orden_Medico=Orden_Medico
                                            ID_lb=ID_lb, ID_pct=ID_pct"""
    # comment: 
# end def

def delete(resultado_analisis: Resultado_Analisis)->Resultado_Analisis:
    # comment: 
    pass
# end def