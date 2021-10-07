# Importar Flask
from flask import Flask

# Instancia de la clase Flask
appFlask = Flask(__name__)

# Importar el módulo con las rutas
from app import routes
