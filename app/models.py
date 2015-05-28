from app import db

class Event(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    creador        = db.Column(db.String(128))
    nombre         = db.Column(db.String(128))
    descripccion   = db.Column(db.String(256))
    ubicacion      = db.Column(db.String(256))
    fecha          = db.Column(db.String(10))
    capacidad      = db.Column(db.Integer)
    disponibilidad = db.Column(db.Integer)
    afiche         = db.Column(db.Binary)

    def __repr__(self):
        return '<Event %r>' % (self.nombre)

class Usuario(db.Model):
    id                = db.Column(db.Integer, primary_key=True)
    unickname         = db.Column(db.String(64), index=True, unique=True)
    ucontrasena       = db.Column(db.String(16))


class Person(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    nombres    = db.Column(db.String(128))
    apellidos  = db.Column(db.String(128))
    nickname   = db.Column(db.String(64), index=True, unique=True)
    contrasena = db.Column(db.String(16))
    edad       = db.Column(db.Integer)
    telefono   = db.Column(db.String(11))
    correo     = db.Column(db.String(120), index=True, unique=True)
    admin      = db.Column(db.Boolean)

    def __repr__(self):
        return '<Person %r>' % (self.nombres) % (self.apellidos)
