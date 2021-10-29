# Importar Flask y config
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Configurar la base de datos sqlite3
db = SQLAlchemy()
migrate = Migrate()

# Configurar el login
login = LoginManager()
login.login_view = 'login'

def create_app(config_class=Config):
    # Instancia de la clase Flask
    appFlask = Flask(__name__)
    appFlask.config.from_object(config_class)

    db.init_app(appFlask)
    migrate.init_app(appFlask, db)
    login.init_app(appFlask)

    from app import routes, models

    return appFlask