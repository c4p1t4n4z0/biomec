#####################################################################################
# aqui se crea el proyecto web, se inicia la conexiones de la base y configuraciones
#####################################################################################

from flask import Flask
from config import Config  # traemos las configuraciones del archivo => config.py
from flask_wtf.csrf import CSRFProtect #para la proteccion del login, importante crear la SECRET_KEY


#rutas
from .routers import global_scope,login_scope  #aqui se importa los archivos de la carpeta  =>  routers



#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()       # creamos una instancia para la base de datos => db
csrf = CSRFProtect()    # creamos una instancia para la proteccion    => csrf

#####################################################################################
# Creando el proyecto, con las rutas de las carpetas las cuales estan en => config.py
#####################################################################################
biomec = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
biomec.config.from_object(Config)
csrf.init_app(biomec)

# aqui ya iniciamos la conexion con la base de posgres
#db = SQLAlchemy(biomec)
#db.init_app(biomec) 
'''
try:
    conexion_db = psycopg2.connect(database = Config.DB_NAME, user = Config.DB_USER, password = Config.DB_PASS)
    cursor = conexion_db.cursor()  

    print('Conexion con la base de datos "Exitosa"')
    
    cursor = conexion_db.cursor()    
    cursor.execute("SELECT * FROM Usuario")
    rows = cursor.fetchall() 
    for row in rows:
        print(row)
 
except Exception as ex:
    print(ex)
finally:
    print("Conexión finalizada")

print (conexion_db) #imprimiendo los parametros de conexion
'''
#####################################################################################
# Rutas 
#####################################################################################
#aqui se llama a las rutas imprimiendo su template, osea la VISTA en la WEB
biomec.register_blueprint(global_scope, url_prefix="/")
biomec.register_blueprint(login_scope,url_prefix ="/admin")


    