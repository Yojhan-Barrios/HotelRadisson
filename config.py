import os

class Config(object):
    # Clave secreta para encriptar el token
    SECRET_KEY = os.environ.get('SECRET_KEY') or '5h,^,+r#$5x*"&+T0,,+,'
    # Configuracion de la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False