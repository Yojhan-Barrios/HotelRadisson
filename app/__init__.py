# Importar Flask y config
from flask import Flask
from app.config import Config

# Instancia de la clase Flask
appFlask = Flask(__name__)

# Leer archivo de configuracion
appFlask.config.from_object(Config)

# Importar el módulo con las rutas
from app import routes
