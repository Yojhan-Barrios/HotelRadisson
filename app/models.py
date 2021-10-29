from enum import unique
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

# Create a class for the database table
class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), index=True)
    correo = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    rol = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f'<User {self.nombre} - Correo {self.correo}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return Usuario.query.get(int(id))

# Clase habitacion
class Habitacion(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(64), index=True)
    detalles = db.Column(db.String, index=True)
    cantidad_calificaciones = db.Column(db.Integer)
    calificacionPromedio = db.Column(db.Float, index=True)
    cantidad_comentarios = db.Column(db.Integer)
    disponible = db.Column(db.Integer, index=True)

    def __repr__(self):
        return f'<Habitacion {self.nombre}>'

# Clase reservas
class Reserva_habitacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    id_habitacion = db.Column(db.Integer, db.ForeignKey('habitacion.id'))
    fecha_inicio = db.Column(db.String, index=True)
    fecha_fin = db.Column(db.String, index=True)
    calificacion_reserva = db.Column(db.Integer, index=True)
    precio_total = db.Column(db.Float, index=True)
    estado = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f'<Reserva {self.id}>'

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    id_habitacion = db.Column(db.Integer, db.ForeignKey('habitacion.id'))
    nombre_usuario = db.Column(db.String(64), index=True)
    comentario = db.Column(db.String, index=True)

    def __repr__(self):
        return f'<Comentario {self.id}>'

class Administrador(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    id_user = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=True)
    rol = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f'<Administrador {self.id}>'

