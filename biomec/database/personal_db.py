from ...models.entidades.Personal import Personal
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none, _fetch_one

def create(personal: Personal)->Personal:
    # comment: 
    sql = """"insert into Personal values(:ID_Persona, :ID_Crg)"""

    parametros = personal._asdict()
    _fetch_none(sql,parametros)
    return personal
# end def

def update(personal: Personal)-> Personal:
    sql = """"update Personal set ID_Persona = ID_Persona, ID_Crg=ID_Crg"""
    # comment: 
# end def

def delete(personal: Personal)-> Personal:
    # comment: 
    pass
# end def