import os
from dotenv import load_dotenv  # Instalar con pip install python-dotenv

load_dotenv()                   # Cargar todo el cotenido de .env en variables de entorno

class Config:

    # Trabajar en la nube voladora. Estamos usando Heroku, es una plataforma como servicio en la nube 
    SERVER_NAME = "biomec.herokuapp.com" # Esto es el nombre del servidor, para mostrar ONLINE 
    DEBUG = True
    # IMPORTANTE
    # Tener instalado el posgretsql para poder conectarnos a la base de datos de Heroku y asi crear las tablas
    # No compartir los datos de la base de datos para proyectos rentables
    DB_HOST = "ec2-44-196-174-238.compute-1.amazonaws.com"
    DB_NAME = "degnorh0nb7ntq"
    DB_USER = "qaoqynpkztebra"
    DB_PASS = "7ad63486016b69a2055755ad4b307b79a7711fd154d10985c4f14aea1103078a"
    DB_PORT = "5432"
    '''
    # ---- Trabajar de manera Local ----
    SERVER_NAME = "localhost:5000"     # Esto es el nombre del servidor, para trabajar de manera LOCAL
    DEBUG = True
    DB_HOST = "localhost"
    DB_NAME = "db_lab"
    DB_USER = "postgres"
    DB_PASS = "root"
    DB_PORT = "5432"
    '''

    DB_TOKEN = os.environ.get("DB_TOKEN","") #Para encriptar la DB
    ENCRYPT_DB = True

    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'      #clave secreta para la proteccion del login


    TEMPLATE_FOLDER = "views/templates"      # defino las rutas para los archivos de vista 
    STATIC_FOLDER ="views/static"



