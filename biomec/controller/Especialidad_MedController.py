from ..models.entidades.Especialidad_Med import Especialida_Med
from ..database.db_entidades import especialidad_med_db

def create(especialidad_med: Especialida_Med)->Especialida_Med:
    # comment: 
    return especialidad_med_db.create(especialidad_med)
# end def

def update(especialidad_med: Especialida_Med)->Especialida_Med:
    # comment: 
    return especialidad_med_db.update(especialidad_med)
# end def

def delete(especialidad_med: Especialida_Med)->Especialida_Med:
    # comment: 
    return especialidad_med_db.delete(especialidad_med)
# end def