# Importar Flask y config
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instancia de la clase Flask
appFlask = Flask(__name__)

# Leer archivo de configuracion
appFlask.config.from_object(Config)

# Configurar la base de datos sqlite3
db = SQLAlchemy(appFlask)
migrate = Migrate(appFlask, db)

# Importar las rutas
from app import routes, models