from ...models.entidades.Paciente import Paciente
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(paciente: Paciente)->Paciente:
    # comment: 
    sql = """"insert into Paciente values(:ID_Paciente, :Nro_Sg)"""

    parametros = paciente._asdict()
    _fetch_none(sql,parametros)
    return paciente
# end def

def update(paciente: Paciente)-> Paciente:
    sql = """"update Paciente set ID_Paciente = ID_Paciente, Nro_Sg=Nro_Sg"""
    # comment: 
# end def

def delete(paciente: Paciente)-> Paciente:
    # comment: 
    pass
# end def