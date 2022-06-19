#Aqui centralizamos todos los blueprint, que se importaran al archivo  => __init__.py principal,de la carpeta biomec
#Es un atajo

from .tipo import tipo_scope #rutas del login 
from .routers import global_scope #rutas el inicio

from .seguro import seguro_scope #rutas del seguro
from .personal import personal_scope #ruta del personal del laboratorio