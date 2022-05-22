import os
from dotenv import load_dotenv #Instalar con pip install python-dotenv

load_dotenv() #cargar todo el cotenido de .env en variables de entorno

class Config:
    SERVER_NAME = "localhost:5500" 
    DEBUG = True

    
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/DB_Lab' # la parametres para postgres
    #SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_HOST = "localhost"
    DB_NAME = "DB_Lab"
    DB_USER = "postgres"
    DB_PASS = "root"

    #DATABASE_PATH = 'biomec/database/DB_Lab.sql'
    #DATABASE_PATH = (DB_NAME,DB_USER,DB_PASS)
    DB_TOKEN = os.environ.get("DB_TOKEN","") #Para encriptar la DB
    ENCRYPT_DB = True

    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'  #clave secreta para la proteccion del login


    TEMPLATE_FOLDER = "views/templates"  # defino las rutas para los archivos de vista 
    STATIC_FOLDER ="views/static"



