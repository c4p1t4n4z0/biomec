from ..models.entidades.Personal import Personal
from ..database.db_entidades import personal_db

def create(personal: Personal)->Personal:
    # comment: 
    return personal_db.create(personal)
# end def

def update(personal: Personal)->Personal:
    # comment: 
    return personal_db.update(personal)
# end def

def delete(personal: Personal)->Personal:
    # comment: 
    return personal_db.delete(personal)
# end def