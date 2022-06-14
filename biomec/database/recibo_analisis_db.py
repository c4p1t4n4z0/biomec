from ...models.entidades.Recibo_Analisis import Recibo_Analisis
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(recibo_analisis: Recibo_Analisis)->Recibo_Analisis:
    # comment: 
    sql = """"insert into Recibo_Analisis values(:ID, :Fecha, :Monto_Total, :ID_Per, :CI_Paciente)"""

    parametros = recibo_analisis._asdict()
    _fetch_none(sql,parametros)
    return recibo_analisis
# end def

def update(recibo_analisis: Recibo_Analisis)->Recibo_Analisis:
    sql = """"update Recibo_Analisis set ID = ID, Fecha=Fecha, Monto_Total=Monto_Total
                                         ID_Per=ID_Per, CI_Paciente=CI_Paciente"""
    # comment: 
# end def

def delete(recibo_analisis: Recibo_Analisis)->Recibo_Analisis:
    # comment: 
    pass
# end def