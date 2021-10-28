from flask import render_template, request, session, redirect, url_for, flash
from markupsafe import escape
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.models import Usuario
from app import appFlask, db


# Estructura por defecto, se cambiara en el futuro
@appFlask.route('/')
@appFlask.route('/home')
def home():
    if 'id' and 'name' in session:
        return render_template('home.html', username=session['name'])
    else:
        return render_template('home.html')

# Ruta para el login
@appFlask.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        # 
        if request.method == 'POST':
            # Obtenemos los datos del formulario
            # Verificamos que el usuario exista
            # Verificamos que la contraseña sea correcta
            # Si todo es correcto, iniciamos sesion
            # Si no, mostramos un mensaje de error 

            user = Usuario.query.filter_by(correo = request.form['email']).first()
            if user is None or not user.check_password(request.form['password']):
                flash('Correo incorrecto o contraseña incorrecta')
                return redirect(url_for('login'))
            login_user(user, remember=request.form.get('formCheck'))

            # Ir a la siguiente ruta
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('home')
            return redirect(next_page)
        else:
            # Si el metodo es GET, mostrar el formulario
            return render_template('login.html')

# Ruta para el registro
@appFlask.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        if request.method == 'POST':
            name = request.form['first_name'] + ' ' + request.form['last_name']
            password = request.form['password']
            repeat_password = request.form['password_repeat']
            email = request.form['email']
            # Sí el nombre es demasiado corto
            if len(name) < 3:
                flash('El nombre debe tener al menos 3 caracteres')
                return redirect(url_for('register'))

            # Sí alguno de los campos esta vacio
            if len(password) < 3 or len(repeat_password) < 3 or len(email) < 3:
                flash('Alguno de los campos esta vacio')
                return redirect(url_for('register'))
            
            if password != repeat_password:
                flash('Las contraseñas no coinciden')
                return redirect(url_for('register'))

            if Usuario.query.filter_by(correo = email).first() is None:
                user = Usuario(nombre=name, correo=email, rol='usuario')
                user.set_password(password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))
            else:
                flash('Correo ya registrado')
                return redirect(url_for('register'))
                
        if request.method == 'GET':
            return render_template('register.html')

# Ruta para el perfil
@appFlask.route('/profile/')
def profile():
    if 'id' in session:
        return render_template('profile.html', username=session['name'])
    else:
        return render_template('login.html')
        


@appFlask.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error), 404

# Ruta para la habitación
@appFlask.route('/room/')
def room():
    if 'id' and 'name' in session:
        return render_template('room.html', username=session['name'])
    else:
        return render_template('room.html')

# Ruta para el dashboard adminisrativo
@appFlask.route('/dashboard/')
@login_required
def dashboard():
    if current_user.is_authenticated() and current_user.rol == 'admin':
        return render_template('dashboard.html')
    return redirect(url_for('home'))

# Ruta para la tabla del dashboard
@appFlask.route('/table/')
@login_required
def table():
    if current_user.is_authenticated() and current_user.rol == 'admin':
        return render_template('table.html')
    else:
        return redirect(url_for('home'))

# Ruta para la reserva de habitación
@appFlask.route('/reservation/')
def reservation():
    return render_template('reservation.html')

# Ruta room_details
@appFlask.route('/room_details/')
def room_details():
    # Dict de fotos
    photos = [
        {'url': 'https://www.eltiempo.com/files/article_multimedia/uploads/2020/07/15/5f0f7308626e6.jpeg', 'title': 'Habitación 1'},
        {'url': 'https://www.eltiempo.com/files/article_multimedia/uploads/2020/07/15/5f0f7308626e6.jpeg', 'title': 'Habitación 2'},
        {'url': 'https://www.eltiempo.com/files/article_multimedia/uploads/2020/07/15/5f0f7308626e6.jpeg', 'title': 'Habitación 3'},
    ]
    

    # Dict de room python
    # Keys: Name, description, capacity, price, image, available
    room = { 'name': 'Room 1', 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod, nisl eget consectetur tempor, nisl nunc ultrices eros, eu porttitor nisl nunc eget lorem. Donec euismod, nisl eget consectetur tempor, nisl nunc ultrices eros, eu porttitor nisl nunc eget lorem. Donec euismod, nisl eget consectetur tempor, nisl nunc ultrices eros, eu porttitor nisl nunc eget lorem. Donec euismod, nisl eget consectetur tempor, nisl nunc ultrices eros, eu porttitor nisl nunc eget lorem. Donec euismod, nisl eget consectetur tempor, nisl nunc ultrices eros, eu porttitor nisl nunc eget lorem. Donec euismod, nisl eget consectetur tempor, nisl nunc ultrices eros, eu porttitor nisl nunc eget lorem. Donec euismod, nisl eget consectetur tempor, nisl nunc ultrices eros, eu porttitor nisl nunc eget lorem. Donec euismod, nisl eget consectetur tempor, nisl nunc ultrices eros, eu porttitor nisl nunc eget lorem. Donec euismod, nisl eget consectetur tempor, nisl nunc ultrices eros, eu porttitor nisl nunc eget lorem. Donec euismod, nisl eget consectetur tempor, nisl nunc ultrices eros, eu porttitor nisl nunc eget lorem. Donec euismod, nisl eget consectetur tempor, nisl nunc ultrices eros, eu porttitor nisl nunc eget lorem. Donec euismod, nisl eget consectetur tempor, nisl nunc ultrices eros, eu',
                'capacity': '2', 'price': '$100', 'image': 'https://images.pexels.com/photos/929778/pexels-photo-929778.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260', 'available': 'True',
                'beds': 4 }

    return render_template('room_details.html', room = room, photos=photos)

@appFlask.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
