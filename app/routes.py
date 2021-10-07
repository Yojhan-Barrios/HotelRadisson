from flask import render_template
from app import appFlask


# Estructura por defecto, se cambiara en el futuro
@appFlask.route('/')
def index():
    render_template('index.html')
    