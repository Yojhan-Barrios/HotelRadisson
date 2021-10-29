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
login.login_view = 'main.login'

# Crear app
def create_app(config_class=Config):
    # Instancia de la clase Flask
    appFlask = Flask(__name__)

    # Leer archivo de configuración
    appFlask.config.from_object(Config)

    db.init_app(appFlask)
    migrate.init_app(appFlask, db)
    login.init_app(appFlask)

    from app.main import bp as main_bp
    appFlask.register_blueprint(main_bp)

    return appFlask

# Importar las rutas
from app import models