from ..models.entidades.Seguro import Seguro
from .connection import _fetch_all, _fecth_lastrow_id, _fetch_none,_fetch_one

def create(seguro: Seguro)->Seguro:
    # comment: 
    sql = """"insert into Seguro values(:Nro_Seguro, :Nombre_Seguro)"""

    parametros = seguro._asdict()
    _fetch_none(sql,parametros)
    return seguro
# end def

def update(seguro: Seguro)-> Seguro:
    sql = """"update Seguro set Nro_Seguro = Nro_Seguro, Nombre_Seguro=Nombre_Seguro"""
    # comment: 
# end def

def delete(seguro: Seguro)-> Seguro:
    # comment: 
    pass
# end def

def list_all():
    # comment: 
    sql = "SELECT * FROM seguro ORDER BY Nro_Seguro DESC"
    print(sql)
    seguro_lista_sql = _fetch_all(sql,None)

    seguros_lista = list(seguro_lista_sql)
    seguro_lista = []

    for x in range (len(seguros_lista)):
        id  = seguros_lista[x][0]
        nombre_seguro = seguros_lista[x][1]
        seguro_datos = {'nro_seguro':id, 'nombre_seguro': nombre_seguro}
        seguro_lista.append(seguro_datos)
    
    return seguro_lista
# end def