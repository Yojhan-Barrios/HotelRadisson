from flask import render_template, request
from app import appFlask


# Estructura por defecto, se cambiara en el futuro
@appFlask.route('/')
def index():
    return render_template('home.html')

# Ruta para el login
@appFlask.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return render_template('login.html')

# Ruta para el registro
@appFlask.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        return render_template('register.html')

# Ruta para el perfil
@appFlask.route('/profile/')
def profile():
    return render_template('profile.html')


@appFlask.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error), 404

# Ruta para la habitación
@appFlask.route('/room/')
def room():
    return render_template('room.html')

# Ruta para el dashboard adminisrativo
@appFlask.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

# Ruta para la tabla del dashboard
@appFlask.route('/table/')
def table():
    return render_template('table.html')

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
