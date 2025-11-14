from flask import Flask, render_template, request, redirect, url_for, flash, session
from dotenv import load_dotenv
import os
from Helpers import mongoDB, ElasticSearch, Funciones

#cargar variables de entorno
load_dotenv()

app=Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY",'Okmnbhu123*+')

# Configuración de la base de datos MongoDB
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION","usuario_roles")

# Configuración de ElasticSearch
ELASTIC_CLOUD_URL = os.getenv("ELASTIC_CLOUD_URL")
ELASTIC_API_KEY = os.getenv("ELASTIC_API_KEY")

# versión de la aplicación
APP_VERSION = "1.0.0"
CREATOR_APP = "JETV"

# Inicializar conexiones
mongo = MongoDB(MONGO_URI, MONGO_DB)
elastic = ElasticSearch(ELASTIC_CLOUD_URL, ELASTIC_API_KEY)

# ==================== RUTAS ====================
@app.route('/')
def landing():
    """Landing page pública"""
    return render_template('landing.html', version=VERSION_APP, creador=CREATOR_APP)

# ==================== MAIN ====================
if __name__ == '__main__':
    # Crear carpetas necesarias
    Funciones.crear_carpeta('static/uploads')
    
    # Verificar conexiones
    print("\n" + "="*50)
    print("VERIFICANDO CONEXIONES")

    if mongo.test_connection():
        print("✅ MongoDB Atlas: Conectado")
    else:
        print("❌ MongoDB Atlas: Error de conexión")
    
    if elastic.test_connection():
        print("✅ ElasticSearch Cloud: Conectado")
    else:
        print("❌ ElasticSearch Cloud: Error de conexión")