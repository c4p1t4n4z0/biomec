from ...models.entidades.Lista_Analisis import Lista_Analisis
from ..connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(lista_analisis: Lista_Analisis)->Lista_Analisis:
    # comment: 
    sql = """"insert into Lista_Analisis values(:ID, :Nombre, :Precio, :ID_Pqa)"""

    parametros = lista_analisis._asdict()
    _fetch_none(sql,parametros)
    return lista_analisis
# end def

def update(lista_analisis: Lista_Analisis)->Lista_Analisis:
    sql = """"update Lista_Analisis set ID=ID, Nombre=Nombre, Precio=Precio, ID_Pqa=ID_Pqa"""
    # comment: 
# end def

def delete(lista_analisis: Lista_Analisis)->Lista_Analisis:
    # comment: 
    pass
# end def