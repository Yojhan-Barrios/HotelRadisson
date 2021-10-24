from flask import render_template, request
from app import appFlask


# Estructura por defecto, se cambiara en el futuro
@appFlask.route('/')
def index():
    return render_template('index.html')

@appFlask.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return render_template('login.html')